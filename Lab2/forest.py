__author__ = 'anusha_balusu, pankhuri_roy'

"""
CSCI-603: Lab 2
Author: Anusha Balusu (ab5136@rit.edu), Pankhuri Roy (pr6538@rit.edu)

This program takes 2 inputs: number of trees and whether house should be drawn or not. It draws the house and
trees and a star above the tallest tree which is the night scenario. For the day, the screen is reset and new house
and sun are drawn.
Wood for day house = sum of tree trunks + wood for night house.
"""

import turtle as t
import random
import math

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GAP = 100
PINE_TRUNK_MAX_HEIGHT = 200
MAPLE_TRUNK_MAX_HEIGHT = 150
TRUNK_MAX_HEIGHT = {'pine': 200, 'maple': 150, 'other': 120}
SIDE = {'pine': 3, 'maple': 0, 'other': 5}
ALL_TRUNK_MIN_HEIGHT = 50
NIGHT_HOUSE_WALL_HEIGHT = 100
STAR_HEIGHT_ABOVE_TREE = 10
SUN_HEIGHT_ABOVE_HOUSE = 150
SUN_RADIUS = 30


def init():
    """
    Initialize for drawing, (-50, -200) is in the lower left and
    (500, 200) is in the upper right
    :pre: pos (0,0), heading (east), up
    :pos: pos (0,0), heading (east), up
    :return: None
    """
    t.setworldcoordinates(-WINDOW_WIDTH/5, -WINDOW_HEIGHT/5, WINDOW_WIDTH, WINDOW_HEIGHT)
    t.up()
    t.setheading(0)
    t.title('Forest')
    t.speed(1)


def trunk(height):
    """
    Draws the trunk of tree.
    :pre: (relative) pos (0,0), heading east, up
    :post: (relative) pos (0, height), heading east, up
    :param height: trunk height (float)
    :return: None
    """
    t.down()
    t.left(90)
    t.forward(height)
    t.up()
    t.right(90)


def polygon(sides, size):
    """
    Draws a polygon.
    :pre: (relative) pos (0,0), heading east, up
    :post: (relative) pos (0, 0), heading east, up
    :param sides: number of sides (int)
    :param size: side length (float)
    :return: height of the polygon
    """
    t.down()
    for _ in range(sides):
        t.forward(size)
        t.left(360/sides)
    if sides % 2 == 0:
        height = size/math.sin(math.pi/sides)
    else:
        height = (size/2) * (1/math.tan(math.pi/sides) + 1/math.sin(math.pi/sides))
    t.up()
    return height


def tree(shape, trunk_height, sides, side_length):
    """
    Draws the tree
    :pre: (relative) pos (0,0), heading east, up
    :post: (relative) pos (0, 0), heading east, up
    :param shape: shape of the top of tree (String)
    :param trunk_height: height of tree trunk (float)
    :param sides: number of sides in the shape of tree (int)
    :param side_length: length of the side of tree top (float)
    :return: total height of tree i.e trunk + top
    """
    trunk(trunk_height)
    if shape is 'maple':
        radius = random.randint(20,40)
        t.down()
        t.circle(radius)
        t.up()
        top_height = 2 * radius
    else:
        t.backward(side_length/2)
        top_height = polygon(sides,side_length)
        t.forward(side_length/2)
    t.right(90)
    t.forward(trunk_height)
    t.left(90)
    return trunk_height + top_height


def house_tree(no_of_trees, house_required):
    """
    Draws the house (if required by user) and trees
    :pre: (relative) pos (0,0), heading east, up
    :post: (relative) pos (0, 0), heading east, up
    :param no_of_trees: number of trees input by user (int)
    :param house_required: yes/no input by user (char y/n)
    :return: total wood (float)
    """
    tallest_tree_height = 0
    tallest_tree_position = 0
    house_drawn = False
    wood = 0
    tree_counter = 1
    while tree_counter <= no_of_trees:
        tree_type = random.choice(['pine', 'maple', 'other'])
        trunk_height = random.randint(ALL_TRUNK_MIN_HEIGHT, TRUNK_MAX_HEIGHT[tree_type])
        tree_height = tree(tree_type, trunk_height, SIDE[tree_type], 50)
        wood += trunk_height
        if tree_height > tallest_tree_height:
            tallest_tree_height = tree_height
            tallest_tree_position = t.position()
        t.forward(GAP)

        # Checking if user wants house and house not created already then build house
        if house_required is 'y' and not house_drawn:
                house_position = random.randint(1, 2)
                if house_position is 1 or tree_counter is no_of_trees - 1:
                    house(NIGHT_HOUSE_WALL_HEIGHT)
                    wood += NIGHT_HOUSE_WALL_HEIGHT * (2 + math.sqrt(2))
                    t.forward(GAP)
                    house_drawn = True

        tree_counter += 1
    # Moving the turtle to top of the highest tree and drawing the star
    star_position = t.position()[0]
    star_position -= tallest_tree_position[0]
    t.backward(star_position)
    t.left(90)
    t.forward(tallest_tree_height + STAR_HEIGHT_ABOVE_TREE)
    t.right(90)
    star()
    # go back to start
    t.right(90)
    t.forward(tallest_tree_height + STAR_HEIGHT_ABOVE_TREE)
    t.left(90)
    t.backward(tallest_tree_position[0])
    return wood


def star():
    """
    Draws the star
    :pre: (relative) pos (0,0), heading east, up
    :post: (relative) pos (0, 0), heading east, up
    :return: None
    """
    t.down()
    n = 6
    for _ in range(n):
        t.right(360/n)
        t.forward(5)
        t.backward(5)

    t.up()


def house(wall_height):
    """
    Draws the house with roof angle 45 degrees
    :pre: (relative) pos (0,0), heading east, up
    :post: (relative) pos (wall_height, 0), heading east, up
    :param wall_height: height of the walls
    :return: None
    """
    slope = wall_height / math.sqrt(2)
    t.down()
    t.left(90)
    t.forward(wall_height)
    t.right(45)
    t.forward(slope)
    t.right(90)
    t.forward(slope)
    t.right(45)
    t.forward(wall_height)
    t.left(90)
    t.up()


def sun(house_height):
    """
    Draws the sun above the house
    :pre: (relative) pos (0,0), heading east, up
    :post: (relative) pos (0, 0), heading east, up
    :param house_height: height of house (float)
    :return: None
    """
    t.left(90)
    t.forward(house_height + 150)
    t.right(90)
    t.down()
    t.circle(SUN_RADIUS)
    t.up()
    t.right(90)
    t.forward(house_height + SUN_HEIGHT_ABOVE_HOUSE)
    t.left(90)


def main():
    """
    The main function.
    :pre: pos(0,0), heading east, up
    :post: pos(wall height,0), heading east, up
    :return: None
    """
    init()
    trees = int(input('Enter how many trees in your forest ? '))
    house_required = input('Is there a house in the forest (y/n) ? ')
    total_wood = house_tree(trees, house_required)
    input('Night is done, press enter for day')
    t.reset()

    day_house_height = total_wood / (2 + math.sqrt(2))
    print('We have', total_wood, 'units of lumber for building.')
    print('We will build house with walls',day_house_height, 'tall')
    house(day_house_height)
    sun(day_house_height)

    input('Day is done, house is built, press enter to quit...')

if __name__ == '__main__':
    main()
