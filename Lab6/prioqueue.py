"""
CSCI-603: Lab 6
Author: Anusha Balusu (ab5136@rit.edu), Pankhuri Roy (pr6538@rit.edu)

This program implements a priority queue based on the priority criteria (after function) given by the client
It includes a test method to test the methods of the priority queue

If taskmaster is the main program then the items are inserted based on time left (least first)
If prioqueue is the main program then the items are inserted based on the values (smallest first)
"""

from node import LinkedNode


class PriorityQueue:

    __slots__ = "front", "back","after"

    def __init__(self, after):
        """
        Initialize a new empty priority queue.
        :param after: an ordering function. See definition of dequeue method.
        :return: None (constructor)
        """
        self.front = None
        self.back = None
        self.after = after

    def __str__(self):
        """
        Return a string representation of the contents of
        this priority queue, front value first.
        """
        result = "Queue["
        n = self.front
        while n is not None:
            result += " " + str( n.value )
            n = n.link
        result += " ]"
        return result

    def dequeue(self):
        """
        Remove one of the values v from the queue such that,
        for all values u in the queue, after(v,u) is False.
        If more than one value satisfies the requirement,
        the value chosen should be the one that has
        been in the queue the longest.
        :pre: not isEmpty()
        :return: None
        """
        assert not self.isEmpty(), "Dequeue from empty queue"
        self.front = self.front.link
        if self.front is None:
            self.back = None

    def enqueue(self, newValue):
        """
        Enter a new value into the queue.
        :param newValue: the value to be entered into the queue
        :return: None
        """
        newNode = LinkedNode(newValue)
        if self.front is None:
            self.front = newNode
            self.back = newNode
        else:
            currentNode = self.front
            previousNode = None
            while currentNode is not None and not self.after(currentNode, newNode):
                previousNode = currentNode
                currentNode = currentNode.link
            newNode.link = currentNode
            if previousNode is not None:
                previousNode.link = newNode
            else:
                self.front = newNode

    def isEmpty(self):
        """
        :return: True iff there are no elements in the queue.
        """
        return self.front is None

    def peek(self):
        """
        Find in the queue the value that would be removed were the dequeue
        method to be called at this time.
        :pre: not isEmpty()
        :return: the value described above
        """
        assert not self.isEmpty(), "peek on empty stack"
        return self.front.value

    insert = enqueue
    remove = dequeue


# def after(v, u):
    # return len(v.value) > len(u.value)
    # return v.value > u.value


def test():
    """
    Test program to test the methods of Priority Queue
    :return: None
    """
    # s = PriorityQueue(after)
    # s = PriorityQueue(lambda v, u: True)
    s = PriorityQueue(lambda v, u: v.value > u.value)  # after function passed
    print( s )
    for value in 1, 2, 3:
        s.enqueue( value )
        print( s )
    print( "Dequeueing:", s.peek() )
    s.dequeue()
    print( s )
    for value in 15, 16:
        s.insert( value )
        print( s )
    print( "Removing:", s.peek() )
    s.remove()
    print( s )
    while not s.isEmpty():
        print( "Dequeueing:", s.peek() )
        s.dequeue()
        print( s )
    print( "Trying one too many dequeues... ", end="" )
    try:
        s.dequeue()
        print( "Problem: it succeeded!" )
    except Exception as e:
        print( "Exception was '" + str( e ) + "'" )


if __name__ == "__main__":
    test()
