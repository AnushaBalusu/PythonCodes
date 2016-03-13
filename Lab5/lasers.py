__author__ = 'anusha_balusu, pankhuri_roy'

"""
CSCI-603: Lab 2
Author: Anusha Balusu (ab5136@rit.edu), Pankhuri Roy (pr6538@rit.edu)
Computes the best possible laser placements
"""

import rit_sort_py as sort_lasers
import sys

GRID_ROWS = 0
GRID_COLS = 0
DIRECTION = ['east', 'west', 'north', 'south']
from collections import namedtuple
Point = namedtuple('Point', 'x y')
Laser = namedtuple('Laser', 'Point direction score')


def read_file(file_name):
    """
    Reads the file and stores them in the grid
    :param file_name: name of file (String)
    :return: list of lists of numbers
    """
    grid = []
    with open(file_name) as file:
        for line in file:
            # split line based on space and convert the string elements in list to integers
            grid.append([int(str_list) for str_list in line.rstrip('\n').split(' ')])
            global GRID_ROWS
            GRID_ROWS += 1
        global GRID_COLS
        GRID_COLS = len(grid[0])
    return grid


def find_lasers(grid):
    """
    Finds all possible lasers for the grid with repeating centers
    :param grid: 2d matrix
    :return: list of all possible named tuple Laser(named tuple Point, orientation, score)
    """
    laser_placements = []

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            # middle elements
            if 0 < row < GRID_ROWS-1 and 0 < col < GRID_COLS-1:
                laser_placements.append(Laser(Point(col, row), DIRECTION[0], grid[row][col+1] + grid[row-1][col] + grid[row+1][col]))
                laser_placements.append(Laser(Point(col, row), DIRECTION[1], grid[row][col-1] + grid[row-1][col] + grid[row+1][col]))
                laser_placements.append(Laser(Point(col, row), DIRECTION[2], grid[row-1][col] + grid[row][col-1] + grid[row][col+1]))
                laser_placements.append(Laser(Point(col, row), DIRECTION[3], grid[row+1][col] + grid[row][col-1] + grid[row][col+1]))

            # top edge elements has south facing lasers
            elif row == 0 and 0 < col < GRID_COLS-1:
                laser_placements.append(Laser(Point(col, row), DIRECTION[3], grid[row+1][col] + grid[row][col-1] + grid[row][col+1]))

            # bottom edge elements
            elif row == GRID_ROWS-1 and 0 < col < GRID_COLS-1:
                laser_placements.append(Laser(Point(col, row), DIRECTION[2], grid[row-1][col] + grid[row][col-1] + grid[row][col+1]))

            # left edge elements
            elif col == 0 and 0 < row < GRID_ROWS-1:
                laser_placements.append(Laser(Point(col, row), DIRECTION[0], grid[row][col+1] + grid[row-1][col] + grid[row+1][col]))

            # right edge elements
            elif col == GRID_COLS-1 and 0 < row < GRID_ROWS-1:
                laser_placements.append(Laser(Point(col, row), DIRECTION[1], grid[row][col-1] + grid[row-1][col] + grid[row+1][col]))
    return laser_placements


def get_lasers(laser_list, laser_count):
    """
    Gives a number of lasers prompted by user.
    :param laser_list: list of laser details (named tuple Point, orientation, score) including same centers
    :param laser_count: number of lasers required (int)
    :return: laser_count list of lasers with non-repeating centers
    """
    final_lasers = []
    count = 0
    for data in laser_list:
        if data.Point not in (item.Point for item in final_lasers):
            final_lasers.append(data)
            count += 1
        if count == laser_count:
            break
    return final_lasers


def print_lasers(lasers):
    """
    Prints the positions and orientations of lasers
    :param lasers: list of lasers (named tuple Point, orientation, score)
    :return: None
    """
    for item in lasers:
        print("(" + str(item.Point.x) + "," + str(item.Point.y) + ")" + " facing " + item.direction)


def main():
    """
    The main program. Accepts a grid and number of lasers as user input
    :return: None
    """
    try:
        file_name = input("Enter the file name: ")
        grid = read_file(file_name)                                     # store the grid
        laser_count = int(input("Enter number of lasers: "))
        laser_placements = find_lasers(grid)                            # all possible orientations
        sorted_lasers = sort_lasers.testMergeSort(laser_placements)     # sort based on score
        required_lasers = get_lasers(sorted_lasers, laser_count)        # get number of lasers prompted
        if not 0 < laser_count:
            print("Give atleast 1 laser")
        elif not laser_count < GRID_ROWS * GRID_COLS - 4:
            # maximum number of lasers with non-repeating center
            # maximum number possible with repeating centers = len(sorted_lasers)
            print("Maximum number of lasers possible", GRID_ROWS * GRID_COLS - 4)
        else:
            print_lasers(required_lasers)
    except FileNotFoundError as fe:
        print(fe, file=sys.stderr)
    except ValueError as ve:
        print(ve, file=sys.stderr)


if __name__ == '__main__':
    main()

