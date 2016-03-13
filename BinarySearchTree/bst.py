"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS, Anusha Balusu

This version modified for the practical exam (by removing
the main method) by Zack Butler.
"""

from btnode import BTNode

class BST:
    """
    A binary search tree consists of:
    :slot root: The root node of the tree (BTNode)
    :slot size: The size of the tree (int)
    """
    __slots__ = 'root', 'size'

    def __init__(self):
        """
        Initialize the tree.
        :return: None
        """
        self.root = None
        self.size = 0

    def __insert(self, val, node):
        """
        The recursive helper function for inserting a new value into the tree.
        :param val: The value to insert
        :param node: The current node in the tree (BTNode)
        :return: None
        """
        if val < node.val:                     # check if need to go left
            if node.left == None:              # if no left child
                node.left = BTNode(val)        # insert it here
            else:                              # otherwise 
                self.__insert(val, node.left)  # traverse with the left node
        else:                                  # need to go right
            if node.right == None:             # if no right child
                node.right = BTNode(val)       # insert it here                               
            else:                              # otherwise 
                self.__insert(val, node.right) # traverse with the right node

    def insert(self, val):
        """
        Insert a new value into the tree
        :param val: The value to insert
        :return: None
        """   
        if self.root == None:              # if tree is empty
            self.root = BTNode(val)        # create root node with the value
        else:                              # otherwise
            self.__insert(val, self.root)  # call helper function with root
        self.size += 1

    def __contains(self, val, node):
        """
        The recursive helper function for checking if a value is in the tree.
        :param val: The value to search for
        :param node: The current node (BTNode)
        :return: True if val is present, False otherwise
        """
        if node == None:      # if there is no node 
            return False      # we went past a leaf and the val is not there
        elif val == node.val: # if the values match
            return True       # return success
        elif val < node.val:  # if no match, but val is lesser
            return self.__contains(val, node.left)  # recurse with left node
        else:                 # otherwise
            return self.__contains(val, node.right) # recurse with right node

    def contains(self, val):
        """
        Returns whether a value is in the tree or not.
        :param val: The value to search for
        :return: True if val is present, False otherwise
        """
        # call the recursive helper function with the root node
        return self.__contains(val, self.root)

    def __height(self, node):
        """
        The recursive helper function for computing the height of a node
        :param node: The current node (BTNode)
        :return: The height of node (int)
        """
        if node == None: # if no node
            return -1    # the height is -1
        else:            # otherwise
            # add 1 to the greater of the left or right node's height
            return 1 + max(self.__height(node.left), self.__height(node.right))

    def height(self):
        """
        Return the height of a tree.  Recall:
            - The height of an empty tree is -1
            - The height of a tree with one node is 0
            - Otherwise the height is one plus the larger of the heights of
            the left or right children.
        :return: The height (int)
        """
        # just call the recursive helper function with the root node
        return self.__height(self.root)

    def __inorder(self, node):
        """
        The recursive inorder traversal function that builds a string
        representation of the tree.
        :param node: The current node (BTNode)
        :return: A string of the tree, e.g. "1 2 5 9 "
        """
        if node == None: # if we went past a leaf
            return ' '    # append a space
        else:             # otherwise
            # construct a string in order from left to current to right
            return self.__inorder(node.left) + \
                   str(node.val) + \
                   self.__inorder(node.right)

    def __str__(self):
        """
        Return a string representation of the tree.  By default this will
        be a string with the values in order.
        :return:
        """
        # call the recursive helper function with the root node
        return self.__inorder(self.root)

    def __depth(self, val, node):
        """
        The recursive helper function for calculating the depth of the value in the tree.
        :param val: The value whose depth is needed
        :param node: The current node (BTNode)
        :return: depth if val is present, otherwise depth if it were in the tree
        """
        if node == None:      # if there is no node
            return 0      # we went past a leaf and the val is not there
        elif val == node.val: # if the values match
            return 0       # return 0
        elif val < node.val:  # if no match, but val is lesser
            return 1 + self.__depth(val, node.left)  # recurse with left node
        else:                 # otherwise
            return 1 + self.__depth(val, node.right) # recurse with right node

    def depth(self, val):
        """
        Gives the depth that the value is in the tree
        :param val: The value whose depth is to be calculated
        :return: depth of value (int)
        """
        # just call the recursive helper function with the root node
        return self.__depth(val, self.root)

    def __numbetween(self, min, max, node):
        """
        The recursive helper function for calculating number of elements between min and max in the tree.
        :param min: lower limit of search (inclusive)
        :param max: upper limit of search (inclusive)
        :param node: The current node (BTNode)
        :return: Number of elements (int)
        """
        assert not min > max, "Expected numbers between " + str(min) + " and " + str(max) + \
                              " = min should be <= max"
        if node == None:
            return 0
        # print(node.val)
        if min == max:                                      # if min and max are same
            if self.contains(min) is True:
                return 1                                    # return 1 if value is present in tree
            else:
                return 0                                    # else return 0
        if min <= node.val <= max:                          # if value is between min and max
            return 1 + self.__numbetween(min, max, node.left) \
                   + self.__numbetween(min, max, node.right)    # recurse left and right and add result
        elif node.val < min:                                # if value is less than min
            return self.__numbetween(min, max, node.right)  # recurse with right node
        elif node.val > max:                                # if value is greater than max
            return self.__numbetween(min, max, node.left)   # recurse with left node

    def numbetween(self, min, max):
        """
        Gives the number of elements between min and max in the tree
        :param min: lower limit of search (inclusive)
        :param max: upper limit of search (inclusive)
        :return: Number of elements (int)
        """
        # just call the recursive helper function with the root node
        return self.__numbetween(min, max, self.root)


def main():
    t = BST()
    t.insert(5)
    t.insert(2)
    t.insert(12)
    t.insert(4)
    t.insert(9)
    t.insert(15)
    t.insert(7)
    t.insert(10)
    print("Tree: " + str(t))
    print()

    print("Expected depth of 5 = 0. Actual = " + str(t.depth(5)))
    print("Expected depth of 2 = 1. Actual = " + str(t.depth(2)))
    print("Expected depth of 10 = 3. Actual = " + str(t.depth(10)))
    print("Expected depth of 14 = 3. Actual = " + str(t.depth(14)))
    print("Expected depth of 11 = 4. Actual = " + str(t.depth(11)))
    print("Expected depth of 1 = 2. Actual = " + str(t.depth(1)))
    print()

    print("Expected numbers between 6 and 10 = 3. Actual = " + str(t.numbetween(6, 10)))
    print("Expected numbers between 15 and 20 = 1. Actual = " + str(t.numbetween(15, 20)))
    print("Expected numbers between 20 and 30 = 0. Actual = " + str(t.numbetween(20, 30)))
    print("Expected numbers between 2 and 7 = 4. Actual = " + str(t.numbetween(2, 7)))
    print("Expected numbers between 1 and 16 = 8. Actual = " + str(t.numbetween(1, 16)))
    print("Expected numbers between 2 and 2 = 1. Actual = " + str(t.numbetween(2, 2)))
    print("Expected numbers between 4 and 4 = 1. Actual = " + str(t.numbetween(4, 4)))
    print()
    try:
        print("Expected numbers between 5 and 4 = min shoud be <= max. Actual = " + str(t.numbetween(5, 4)))
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
