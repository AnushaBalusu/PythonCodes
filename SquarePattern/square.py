__author__ = 'Anusha_Balusu'

import turtle as t

BOUNDARY = 400
THICK_PEN = 4
THIN_PEN = 1


def init():
    """
    Initialize the canvas
    :pre: relative (0,0), heading east, up
    :post: relative (0,0), heading east, up
    :return: None
    """
    t.setworldcoordinates(-BOUNDARY/2, -BOUNDARY/2, BOUNDARY, BOUNDARY)
    t.title("SQUARES")
    t.speed(0)


def square(depth, length, pen_width):
    """
    Draws a square
    :pre: relative (0,0), heading east, up
    :post: relative (0,0), heading east, up
    :return: distance travelled by turtle
    """
    t.down()
    t.pensize(pen_width)
    distance = 0
    for _ in range(1,5):
        t.forward(length)
        distance += length
        t.left(90)
    t.up()
    return distance


def draw_square_rec(depth, length, pen_width):
    """
    Draws squares recursively
    :pre: relative (0,0), heading east, up
    :post: relative (0,0), heading east, up
    :return: distance travelled by turtle
    """
    distance = 0
    if depth <= 0:
        return 0
    if depth == 1:
        distance += square(depth, length, pen_width)
        return distance

    two_third_length = 2 * length/3

    distance += square(depth, length, pen_width)
    if pen_width == THICK_PEN:
        pen_width = THIN_PEN
    else:
        pen_width = THICK_PEN

    distance += draw_square_rec(depth-1, length/3, pen_width)
    t.forward(two_third_length)
    distance += two_third_length

    distance += draw_square_rec(depth-1, length/3, pen_width)
    t.left(90)
    t.forward(two_third_length)
    distance += two_third_length
    t.right(90)

    distance += draw_square_rec(depth-1, length/3, pen_width)
    t.back(two_third_length)
    distance += two_third_length

    distance += draw_square_rec(depth-1, length/3, pen_width)
    t.right(90)
    t.forward(two_third_length)
    distance += two_third_length
    t.left(90)
    return distance


def main():
    """
    The main program. Accepts only positive depths and lengths.
    :pre: relative (0,0), heading east, up
    :post: relative (0,0), heading east, up
    :return: None
    """
    try:
        depth = int(input("Enter depth: "))
        if depth > 0:
            length = int(input("Enter length of largest square: "))
            if length > 0:
                init()
                distance = draw_square_rec(depth, length, THICK_PEN)
                print("Total distance: ", distance)
                t.done()
            else:
                print("Zero or Negative length not allowed")
        else:
            print("Zero or Negative depth not allowed")
    except ValueError:
        print("Invalid Input. Input not an integer")


if __name__ == '__main__':
    main()
