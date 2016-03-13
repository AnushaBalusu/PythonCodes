__author__ = 'zjb, anusha_balusu, pankhuri_roy'

"""
CSCI-603: Lab 8
Author: Anusha Balusu (ab5136@rit.edu), Pankhuri Roy (pr6538@rit.edu)
Implementation of heap modified for Cathy and Harold Garage problem
"""

MINTYPE = "min" # harold min time
MAXTYPE = "max" # cathy max cost

class Heap(object):
    '''
    Heap that orders by a given comparison function, default to less-than.
    '''
    __slots__ = ('data','size','lessfn')

    def __init__(self,lessfn):
        '''
        Constructor takes a comparison function.
        :param lessfn: Function that takes in two heap objects and returns true
        if the first arg goes higher in the heap than the second
        '''
        self.data = []
        self.size = 0
        self.lessfn = lessfn

    def __parent(self,loc):
        '''
        Helper function to compute the parent location of an index
        :param loc: Index in the heap
        :return: Index of parent
        '''
        return (loc-1)//2

    def __bubbleUp(self,loc, indexList, heapType):
        '''
        Starts from the given location and moves the item at that spot
        as far up the heap as necessary
        Updates the min/max indices of jobs for each swap
        :param  loc: Place to start bubbling from
                indexList: list of jobs
                heapType: min of max (String)
        '''
        while loc > 0 and self.lessfn(self.data[loc],self.data[self.__parent(loc)]):
            self.updateIndex(loc, indexList, self.data[self.__parent(loc)], heapType)
            self.updateIndex(self.__parent(loc), indexList, self.data[loc], heapType)

            (self.data[loc], self.data[self.__parent(loc)]) = (self.data[self.__parent(loc)], self.data[loc])
            loc = self.__parent(loc)

    def __bubbleDown(self,loc, indexList, heapType):
        '''
        Starts from the given location and moves the item at that spot
        as far down the heap as necessary
        Updates the min/max indices of jobs for each swap/pop
        :param loc: Place to start bubbling from
               indexList: list of jobs
               heapType: min of max (String)
        '''
        swapLoc = self.__smallest(loc)
        while swapLoc != loc:
            self.updateIndex(loc, indexList, self.data[swapLoc], heapType)
            self.updateIndex(swapLoc, indexList, self.data[loc], heapType)

            (self.data[loc], self.data[swapLoc]) = (self.data[swapLoc], self.data[loc])
            loc = swapLoc
            swapLoc = self.__smallest(loc)

    def __smallest(self,loc):
        '''
        Finds the "smallest" value of loc and loc's two children.
        Correctly handles end-of-heap issues.
        :param loc: Index
        :return: index of smallest value
        '''
        ch1 = loc*2 + 1
        ch2 = loc*2 + 2
        if ch1 >= self.size:
            return loc
        if ch2 >= self.size:
            if self.lessfn(self.data[loc],self.data[ch1]):
                return loc
            else:
                return ch1
        # now consider all 3
        if self.lessfn(self.data[ch1],self.data[ch2]):
            if self.lessfn(self.data[loc],self.data[ch1]):
                return loc
            else:
                return ch1
        else:
            if self.lessfn(self.data[loc],self.data[ch2]):
                return loc
            else:
                return ch2

    def insert(self,item, indexList, heapType):
        '''
        Inserts an item into the heap. Updates the index after appending new item
        :param  item: Item to be inserted
                indexList: list of jobs
                heapType: min of max (String)
        '''
        self.data.append(item)
        self.updateIndex(self.size, indexList, item, heapType)
        self.size += 1
        self.__bubbleUp(self.size-1, indexList, heapType)

    def updateIndex(self, index, indexList, item, heapType):
        '''
        Updates the index of the job in the list of jobs
        :param index: index to update
        :param indexList: list of jobs
        :param item: the job whose index is to be updated
        :param heapType: min of max (String)
        :return:
        '''
        pos = indexList.index(item)
        if heapType is "min":
            indexList[pos].indexMin = index
        else:
            indexList[pos].indexMax = index

    def pop(self, indexList, heapType):
        '''
        Removes and returns top of the heap. Updates the index before popping the item
        :param  indexList: list of jobs
                heapType: min of max (String)
        :return: Item on top of the heap
        '''
        retjob = self.data[0]
        self.size -= 1
        # if we are popping the only element, assignment will fail,
        # but bubbling is unnecessary, so:
        if self.size > 0:
            self.updateIndex(-1, indexList, retjob, heapType)
            self.data[0] = self.data.pop(self.size)
            self.__bubbleDown(0, indexList, heapType)

        return retjob

    def popAt(self, index, indexList, heapType):
        '''
        Removes and returns item at index of the heap. Swaps the index item with root.
        Pops the root item ( i.e. last item is copied to root)
        Next root is swapped with item at index
        Now bubble down the item at index
        :param  index: index from which job is to be removed
                indexList: list of jobs
                heapType: min of max (String)
        :return: Item at index of the heap
        '''
        retjob = self.data[index]
        self.size -= 1
        # if we are popping the only element, assignment will fail,
        # but bubbling is unnecessary, so:
        if self.size > 0:
            # update indices and swap item at index with root item
            self.updateIndex(0, indexList, self.data[index], heapType)
            self.updateIndex(index, indexList, self.data[0], heapType)
            self.data[0], self.data[index] = self.data[index], self.data[0]

            # update indices and pop the last item
            self.updateIndex(-1, indexList, retjob, heapType)
            self.updateIndex(0, indexList, self.data[self.size], heapType)
            self.data[0] = self.data.pop(self.size)
            # no need of swapping / bubbling down if it is the last item
            if index < self.size:
                # update indices and swap item at index with root item again
                self.updateIndex(0, indexList, self.data[index], heapType)
                self.updateIndex(index, indexList, self.data[0], heapType)
                self.data[0], self.data[index] = self.data[index], self.data[0]

                self.__bubbleDown(index, indexList, heapType)

        return retjob

    def __len__(self):
        '''
        Defining the "length" of a data structure also allows it to be
        used as a boolean value!
        :return: size of heap
        '''
        return self.size

    def __str__(self):
        ret = ""
        for item in range(self.size):
            ret += str(self.data[item]) + " "
        return ret

def namecmp(n1, n2):
    '''
    Simple comparison function as an example. Assumes each name is (first, last) tuple
    :param n1: Name
    :param n2: Other name
    :return: True if n1 comes before n2
    '''
    return n1[0] < n2[0]

def main():
    # here's a min heap (comparison is less than)
    minh = Heap(lambda x,y: x<y)
    for num in (5,3,7,2):
        minh.insert(num)
    print("Heap is now: " + str(minh))
    print(minh.pop())
    minh.insert(1)
    minh.insert(8)
    print("Heap is now: " + str(minh))
    print("Emptying heap:")
    while minh:
        print(minh.pop())

    # here's a max heap
    maxh = Heap(lambda x,y: x > y)
    for num in (4,6,10,2,-1,3):
        maxh.insert(num)
    print("Emptying max heap:")
    while maxh:
        print(maxh.pop())

    # a heap of names, for some reason?
    nameheap = Heap(namecmp)
    nameheap.insert(('Sean','Strout'))
    nameheap.insert(('Zack','Butler'))
    nameheap.insert(('James','Heliotis'))
    nameheap.insert(('Alan','Turing'))
    print()
    print(nameheap.pop())
    print(nameheap.pop())
    print(nameheap.pop())
    nameheap.insert(('Ada','Lovelace'))
    nameheap.insert(('Grace','Hopper'))
    while nameheap:
        print(nameheap.pop())

if __name__ == '__main__':
    main()