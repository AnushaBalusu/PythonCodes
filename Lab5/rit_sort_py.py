"""
CSCI-603: Wk 7 Sorting
Author: Sean Strout @ RIT CS, Anusha Balusu, Pankhuri Roy

Implementations of in-place sorts for selectionSort and
mergeSort.
"""

# test case data
DATA1 = ( [], [0], [0,1], [1,0], [5, 4, 3], [1,9,4,2,0,3,7] )
DATA2 = ( [], [0], [0,1], [1,0], [5, 4, 3], [1,9,4,2,0,3,7] )


def _findMinIndex(data, mark):
    """
    A helper routine for selectionSort which finds the index
    of the smallest value in data at the mark index or greater.
    :param data: a list of data
    :param mark: an index which is in range 0..len(data)-1 inclusive
    :return: An index which is in range 0..len(data)-1 inclusive
    """

    # assume the minimum value is at initial mark position
    minIndex = mark

    # loop over the remaining positions greater than the mark
    for mark in range(mark+1, len(data)):
        # if a smaller value is found, record its index
        if data[mark] < data[minIndex]:
            minIndex = mark
    return minIndex

def selectionSort(data):
    """
    Perform an in-place selection sort of data.
    :param data: The data to be sorted (a list)
    :return: None
    """
    for mark in range(len(data)-1):
        minIndex = _findMinIndex(data, mark)
        # swap the element at marker with the min index
        data[mark], data[minIndex] = data[minIndex], data[mark]


def _split(data):
    """
    Split the data into halves and return the two halves
    :param data: The list to split in half
    :return: Two lists, cut in half
    """
    return data[:len(data)//2], data[len(data)//2:]


def _merge(left, right):
    """
    Merges two sorted list, left and right, into a combined sorted result
    :param left: A sorted list
    :param right: A sorted list
    :return: One combined sorted list
    """

    # the sorted left + right will be stored in result
    result = []
    leftIndex, rightIndex = 0, 0
    # loop through until either the left or right list is exhausted
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex][2] >= right[rightIndex][2]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    # take the un-exhausted list and extend the remainder onto the result
    if leftIndex < len(left):
        result.extend(left[leftIndex:])
    elif rightIndex < len(right):
        result.extend(right[rightIndex:])

    return result


def mergeSort(data):
    """
    Performs a merge sort and returns a newly sorted list.
    :param data: A list of data
    :return: A sorted list
    """

    # an empty list, or list of 1 element is already sorted
    if len(data) < 2:
        return data
    else:
        # split the data into left and right halves
        left, right = _split(data)
        # return the merged recursive mergeSort of the halves
        return _merge(mergeSort(left), mergeSort(right))


def testSelectionSort():
    """
    A test function for the selection sort.
    :return: None
    """
    print('Testing seletion sort...')
    for data in DATA1:
        print('data:', data, end='')
        selectionSort(data)
        print(', sorted:', data)


def testMergeSort(laser_placements):
    """
    A test function for merge sort.
    :return: None
    """
    # print(laser_placements)
    # print('Testing merge sort...')
    # for data in laser_placements:
    #    print(data)
    # print('data:', laser_placements, ', sorted:', mergeSort(laser_placements))
    return mergeSort(laser_placements)

def main():
    """
    Main function.
    :return: None
    """
    testSelectionSort()
    testMergeSort()

if __name__ == '__main__':
    main()