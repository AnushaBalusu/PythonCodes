__author__ = 'anusha_balusu, pankhuri_roy'

LOAD_FACTOR = 0.75
INITIAL_SIZE = 3

from set import SetType
from collections.abc import Iterable, Iterator

class Node():
    """
    A data slot with next and previous as the chain links and orderNext and orderPrevious as
    the ordering links
    """
    __slots__ = "data", "next", "previous", "orderNext", "orderPrevious"

    def __init__(self, data=None, next=None, previous=None, orderNext=None, orderPrevious=None):
        self.data = data
        self.next = next
        self.previous = previous
        self.orderNext = orderNext
        self.orderPrevious = orderPrevious




class LinkedHashTable(SetType):
    """
    This Linked hash map table is a list of linked lists. Each node
    in each linked list contains an entry in the map.
    There are two lists: chain list and order list
    The order list keeps track of the order in which the objects are added
    """
    __slots__ = "table", "rear", "front", "node", "link", "rearLink", "size"

    def __init__(self, rear=None, front=None, link=None, rearLink=None, size=0):
        self.table = [None for _ in range(INITIAL_SIZE)]
        self.rear = rear
        self.front = front
        self.link = link
        self.rearLink = rearLink
        self.size = size

    def getHashCode(self, obj):
        """
        Calculates the hashcode
        :param obj: Object whose hash code is to be computed
        :return: hascode
        """
        objNode = Node(obj)
        return hash(objNode.data) % len(self.table)

    def contains( self, obj ):
        objNode = Node(obj)
        hashCode = self.getHashCode(obj)
        node = self.table[hashCode]
        isPresent = False
        while node != None:
            node = node.next
            if node is not None and node.data is not None and node.data == objNode.data:
                isPresent = True
                break
        return isPresent

    def _rehash(self, type):
        """
        Rebuild the map in a larger table. The current map is not changed
        in any way that can be seen by its clients, but internally its table is
        grown.
        :return: None
        """
        if type:
            rehashSize = 2 * len(self.table)
        else:
            rehashSize = len(self.table)//2
        self.table=[None for _ in range(rehashSize)]
        self.size=0
        for item in self:
            self.add(item)

    def add(self, obj):
        """
        Adds an object to the linked hash table
        :param obj: object to be added
        :return: None
        """
        if float(self.size)/float(len(self.table))>LOAD_FACTOR:
            self._rehash(True)
        if not self.contains(obj):
            hashCode = self.getHashCode(obj)
            node = Node(obj)
            if self.table[hashCode] is None:
               self.table[hashCode] = Node()
            if self.table[hashCode].next is not None:
                node.next = self.table[hashCode].next
                self.table[hashCode].next.previous = node
            self.table[hashCode].next = node
            # print( "Added " + str(obj) + " at index " + str(hashCode))
            self.size += 1
            # add the order links
            if self.size == 1:
                self.front = node
                self.rear = node
            else:
                self.rear.orderNext = node
                node.orderPrevious = self.rear
                self.rear = node

    def remove( self, obj ):
        """
        Removes an object from the linked hash table
        :param obj: object to be removed
        :return:None
        """
        hashCode = self.getHashCode(obj)
        node = self.table[hashCode]
        objNode = Node(obj)
        while node is not None and node.next is not None:
            if node.next.data == objNode.data:
                orderTempObj = node.next
                if node.next.next is not None:
                    node.next.next.previous = node  # set the back link
                node.next = node.next.next          # set the next link
                # rearrange order links
                if self.front.data == obj:      # first element
                    self.front = orderTempObj.orderNext
                    if orderTempObj != None and orderTempObj.orderNext is not None:
                        orderTempObj.orderNext.orderPrevious = None
                elif self.rear.data == obj:
                    self.rear = orderTempObj.orderPrevious
                    if orderTempObj.orderPrevious is not None:
                        orderTempObj.orderPrevious.orderNext = None
                else:
                    if orderTempObj != None and orderTempObj.orderNext is not None:
                        orderTempObj.orderNext.orderPrevious = orderTempObj.orderPrevious  # set the back link
                        orderTempObj.orderPrevious.orderNext = orderTempObj.orderNext          # set the next link

                self.size -= 1
                if (1-LOAD_FACTOR) >= float(self.size)/float(len(self.table)):
                    self._rehash(False)
                break
            else:
                node = node.next

    def __iter__( self ):
        return LinkedHashTable.Iterator(self.front)

    def iterateInOrder(self):
        for item in self:
            print(item)

    class Iterator(Iterator):
        """
        Class that implements iterator
        """
        __slots__ = "it"

        def __init__(self, iterator):
            self.it = iterator

        def __next__(self):
            if self.it is None:
                raise StopIteration()
            else:
                value = str(self.it.data)
                self.it=self.it.orderNext
                return value
