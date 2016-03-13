__author__ = 'Anusha'

"""
CSCI-603: Lab 1
Author: Anusha Balusu (ab5136@rit.edu)

This program draws the characters K R I S H N A V E N I
"""

import turtle
import math

#global constants for window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
CHAR_WIDTH = 30
CHAR_HEIGHT = 40
CHAR_HYPOT = math.hypot(CHAR_WIDTH,CHAR_HEIGHT/2)
CHAR_GAP = 10

def init():
    """
    Initialize for drawing, (-50, -200) is in the lower left and
    (500, 200) is in the upper right
    :pre: pos (0,0), heading (east), up
    :pos: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/20, -WINDOW_HEIGHT/2,
                               WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(0)
    turtle.title('Typography')
    turtle.speed(1)

def drawK():
    """
    Draw the alphabet K
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.backward(CHAR_HEIGHT/2)
    angleK = math.degrees(math.atan(2 * CHAR_WIDTH/CHAR_HEIGHT))
    turtle.right(angleK)
    #turtle.forward(math.sqrt(CHAR_HEIGHT^2 + CHAR_WIDTH^2)/2)

    turtle.forward(CHAR_HYPOT)
    turtle.backward(CHAR_HYPOT)
    turtle.right(180 - 2 * angleK)
    turtle.forward(CHAR_HYPOT)
    turtle.backward(CHAR_HYPOT)
    turtle.right(angleK)
    turtle.forward(CHAR_HEIGHT/2)
    turtle.left(90)
    turtle.up()
    turtle.forward(CHAR_WIDTH + CHAR_GAP)

def drawR():
    """
    Draw the alphabet R
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    drawK()
    turtle.backward(CHAR_WIDTH + CHAR_GAP)
    turtle.down()
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.right(90)

    turtle.forward(CHAR_WIDTH)
    turtle.backward(CHAR_WIDTH)
    turtle.right(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)
    turtle.up()
    turtle.forward(CHAR_WIDTH + CHAR_GAP)

def drawI(width, height):
    """
    Draw the alphabet I
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.down()
    turtle.forward(width)
    turtle.backward(width/2)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width/2)
    turtle.backward(width)
    turtle.up()
    turtle.forward(CHAR_WIDTH + CHAR_GAP)

def drawH():
    """
    Draw the alphabet H
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.right(180)
    drawI(CHAR_HEIGHT, CHAR_WIDTH)
    turtle.left(90)
    turtle.forward(CHAR_WIDTH + CHAR_GAP)

def drawS():
    """
    Draw the alphabet S
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    angle = math.degrees(math.atan(CHAR_HEIGHT/(3 * CHAR_WIDTH)))
    #length = math.sqrt( math.pow(CHAR_WIDTH,2) + math.pow(CHAR_HEIGHT/3,2))
    length = math.hypot(CHAR_WIDTH, CHAR_HEIGHT/3)
    turtle.down()
    turtle.left(angle)
    turtle.forward(length)
    turtle.left(180 - 2 * angle)
    turtle.forward(length)
    turtle.right(180 - 2 * angle)
    turtle.forward(length)
    turtle.up()
    turtle.right(angle)
    turtle.backward(CHAR_WIDTH)
    turtle.right(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)
    turtle.forward(CHAR_WIDTH + CHAR_GAP)

def drawN():
    """
    Draw the alphabet N
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    turtle.left(90)
    turtle.down()
    turtle.forward(CHAR_HEIGHT)
    angleN = math.degrees(math.atan(CHAR_WIDTH/CHAR_HEIGHT))
    turtle.right(180 - angleN)
    lengthN = math.sqrt(math.pow(CHAR_WIDTH,2) + math.pow(CHAR_HEIGHT,2))
    turtle.forward(lengthN)
    turtle.left(180 - angleN)
    turtle.forward(CHAR_HEIGHT)
    turtle.up()
    turtle.backward(CHAR_HEIGHT)
    turtle.right(90)
    turtle.forward(CHAR_GAP)

def drawA():
    """
    Draw the alphabet A
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    turtle.down()
    angleA = math.degrees(math.atan((2 * CHAR_HEIGHT)/CHAR_WIDTH))
    turtle.left(angleA)
    lengthA = math.sqrt(math.pow(CHAR_WIDTH/2,2) + math.pow(CHAR_HEIGHT,2))
    turtle.forward(lengthA)
    turtle.right(2 * angleA)
    turtle.forward(lengthA)
    turtle.backward(lengthA/2)
    turtle.left(angleA)
    turtle.backward(CHAR_WIDTH/2)
    turtle.left(angleA)
    turtle.backward(lengthA/2)
    turtle.right(angleA)
    turtle.up()
    turtle.forward(CHAR_WIDTH + CHAR_GAP)

def drawV():
    """
    Draw the alphabet V
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    angleA = math.degrees(math.atan((2 * CHAR_HEIGHT)/CHAR_WIDTH))
    turtle.right(90 + angleA)
    turtle.down()
    lengthA = math.sqrt(math.pow(CHAR_WIDTH/2,2) + math.pow(CHAR_HEIGHT,2))
    turtle.forward(lengthA)
    turtle.left(2 * angleA)
    turtle.forward(lengthA)
    turtle.up()
    turtle.backward(lengthA)
    turtle.right(angleA)
    turtle.forward(CHAR_WIDTH/2 + CHAR_GAP)

def drawE():
    """
    Draw the alphabet E
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.right(90)
    for i in [0,1]:
        turtle.forward(CHAR_WIDTH)
        turtle.backward(CHAR_WIDTH)
        turtle.right(90)
        turtle.forward(CHAR_HEIGHT/2)
        turtle.left(90)
    turtle.forward(CHAR_WIDTH)
    turtle.up()
    turtle.forward(CHAR_GAP)


def renderName():
    """
    Render a name
    :pre: pos(0,0), heading (east), up
    :post: (relative) pos(CHAR_WIDTH + CHAR_GAP,0), heading (east), up
    :return: None
    """
    drawK()
    drawR()
    drawI(CHAR_WIDTH, CHAR_HEIGHT)
    drawS()
    drawH()
    drawN()
    drawA()
    drawV()
    drawE()
    drawN()
    drawI(CHAR_WIDTH, CHAR_HEIGHT)
    turtle.hideturtle()

def main():
    """
    The main function.
    :pre: pos(0,0), heading (east), up
    :post: pos( (CHAR_WIDTH + CHAR_GAP) * No. of characters,0), heading (east), up
    :return:
    """
    init()
    h = math.sqrt(math.pow(CHAR_HYPOT,2) - math.pow(CHAR_HEIGHT/2,2))
    print(h)
    renderName()

    input('Hit enter to close...')
    turtle.bye()


if __name__ == '__main__':
    main()
