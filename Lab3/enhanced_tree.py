__author__ = 'anusha_balusu, pankhuri_roy'

"""
CSCI-603: Lab 2
Author: Anusha Balusu (ab5136@rit.edu), Pankhuri Roy (pr6538@rit.edu)

This program takes 4 inputs:
    1. number of layers
    2. height of tree
    3. Bushiness (no of sub branches from a branch and their likeliness )
    4. Leafiness (no of leafs at end of branch and their likeliness)
    and draws a tree with the following randomness:
        1. In leafs: different color, shapes, number
        2. In branches: number, angle between branches
"""

import turtle as t
import random
import math

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
LEAF_COUNTER = 0
HEIGHT_FACTOR = 1/2
COLORS = ['lime green', 'coral', 'yellow green', 'sea green', 'dark green']


def init():
    """
    Initialize for drawing, (-500, -250) is in the lower left and
    (500, 500) is in the upper right
    :pre: pos (0,0), heading (east), up
    :pos: pos (0,0), heading (north), up
    :return: None
    """
    t.setworldcoordinates(-WINDOW_WIDTH, -WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT)
    t.left(90)
    t.title('Enhanced Tree')
    t.speed(0)


def draw_tree(depth, height, branches, leafs, angle):
    """
    Draws the tree using recursion
    :pre: pos(0,0), heading east, up
    :post: pos(0,0), heading east, up
    :param depth: number of layers of sub branches (recursion depth)
    :param height: height of tree
    :param branches: number of branches
    :param leafs: number of leafs
    :param angle: angle between branches
    :return: None
    """
    if depth == 0:
        leafs = random.randint(0, leafs)
        draw_leaf(leafs)
        t.down()
        pass

    else:
        t.color('brown')
        t.forward(height)
        for i in range(1, branches+1):
            t.left(90 - i * angle)
            #random branches
            branches = random.randint(branches-1,branches+5)
            draw_tree(depth - 1, height * HEIGHT_FACTOR, branches, leafs, angle)
            t.right(90 - i * angle)
            #random angle
            angle = random.randint(angle-1, angle+1)
            if depth == 1:
                break
        t.color('brown')
        t.backward(height)


def draw_leaf(no_of_leafs):
    """
    Draws leafs at the end of branch. Min 0 and max = no_of_leafs
    :pre: pos(0,0), heading east, up
    :post: pos(0,0), heading east, up
    :param no_of_leafs: maximum number of leads drawn
    :return: None
    """
    for i in range(no_of_leafs):
        # draws random poylgon from triangle to hexagon
        sides = random.randint(3, 6)
        color = random.choice(COLORS)
        size = 10
        angle = 360/sides
        t.left(90 - i * angle)
        t.right(90)
        t.begin_fill()
        t.down()
        t.color(color)
        for _ in range(sides):
            t.forward(size)
            t.left(angle)
        t.left(90)
        t.up()
        t.end_fill()
        t.right(90 - i * angle)

    global LEAF_COUNTER
    LEAF_COUNTER += 1


def validate(tag, value):
    """
    Validates the user inputs
    :param tag: user input type i.e depth, height, bushiness, leafiness
    :param value: value of user input as string
    :return: input is valid or not, value of user input (in appropriate type)
    """
    is_valid = True
    val = 0
    try:
        if tag == 'depth':
            val = int(value)
            if val < 0:
                print("Not a positive integer")
                is_valid = False

        elif tag == 'height':
            val = int(value)
            if val < 1:
                print("Not a positive integer")
                is_valid = False
        else:
            val = float(value)
            if not 0 <= val <= 1:
                print("Not between 0 and 1")
                is_valid = False
    except ValueError:
        if tag == 'depth' or tag == 'height':
            print("Not an valid integer")
        else:
            print("Not a valid number. " + tag + " should be between 0 and 1")
        is_valid = False

    return is_valid, val


def prompt_user_input():
    """
    Takes user input
    :return: list of parameter values if valid otherwise empty list
    """
    parameters = [["depth","Enter number of layers:  "],
                      ["height", "Height of tree:  "],
                      ["bushiness", "Bushiness of tree:  "],
                      ["leafiness", "Leafiness of tree:  "]]
    params = []
    for item in parameters:
        user_input = input(item[1]);
        valid, value = validate(item[0], user_input)
        if valid:
            params.append(value)
        else:
            params = []
            break
    return params


def calculate_height(depth, tree_height):
    """
    Calculates the height of the trunk from the height of the tree
    :param depth: number of layers (recursion depth)
    :param tree_height: height of tree
    :return: trunk height
    """
    if depth == 0:
        return 1
    else:
        return int(tree_height / ((1-math.pow(HEIGHT_FACTOR,depth)) / (1-HEIGHT_FACTOR)))


def main():
    """
    The main function
    :pre: pos(0,0), heading east, up
    :post: pos(0,0), heading north, up
    :return:
    """
    inputs = prompt_user_input()
    if inputs:
        init()
        t.down()
        trunk_height = calculate_height(inputs[0], inputs[1])
        #convert to scale of 5
        branches = int(inputs[2] * 5)
        #convert to scale of 10
        leafs = int(inputs[3] * 10)
        #calculates angle between branches based on number of branches
        angle = int(180 / (branches + 1))

        draw_tree(inputs[0], trunk_height, branches, leafs, angle)
        t.done();
    print('Total Number of Leaves:   ' + str(LEAF_COUNTER))
    print("Done")


if __name__ == '__main__':
    main()
