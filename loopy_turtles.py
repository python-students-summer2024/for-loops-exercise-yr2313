"""
This file contains a few incomplete function definitions that use the turtle module.  
The turtle module is included in the default Python distribution and documented here: https://docs.python.org/3/library/turtle.html
Your task is to complete the incomplete function definitions so that they behave as indicated in the documentation.

Do not run this file directly.
Rather, call any of these functions from main.py and run that file.
"""

# import the turtle module, which is included in the regular Python distribution
import turtle


def create_turtle(stroke_color, bg_color):
    """
    Creates a turtle object, and sets the stroke and background colors.
    This code is given to you for use by the other functions.

    :param stroke_color: The color of the trail the turtle leaves behind as it moves.
    :param bg_color: The background color of the window.
    :returns: The turtle object with the color settings applied.
    """

    # create the turtle and set its trial color
    t = turtle.Turtle()
    t.shape("turtle")  # make it look like a turtle
    t.color(stroke_color)  # set the color of the trail left by the turtle

    # set the window color
    window = turtle.Screen()  # get access to the window where the turtle will appear
    window.bgcolor(bg_color)  # set the window's background color

    return t  # return the turtle


def pick_up_and_move_turtle(t, x, y):
    """
    Pick up and move the turtle to a specific position on the screen.
    The turtle does not leave a trail behind it when picked up and moved.
    This code is given to you to use in the other functions.

    :param t: The turtle object to pick up and move.
    :param x: The destination x coordinate.
    :param y: The destination y coordinate.
    """

    t.penup()  # lift up the turtle's 'pen', so it doesn't draw yet.
    t.setposition(x, y)  # move the turtle to the target position
    t.pendown()  # put down the turtle's 'pen', so it is ready to draw


def print_turtle_position(t):
    """
    Prints out the turtle's x and y coordinataes and degree of rotation on the screen.
    This code is given to you to use in the other functions.

    :param t: The turtle of interest.
    """
    print(
        "Turtle at", t.position(), "rotated", t.heading(), "degrees"
    )  # print out the turtle's current position


def draw_square(t, start_x, start_y, length, rotation_direction, fill_color):
    """
    Draw a square of a given side length, starting from a given position.
    - Use the 'pick_up_and_move_turtle' function definied in this file to move the turtle to its starting position.
    - Use the turtle's 'forwards' function to move the turtle forwards.
    - Use the turtle's 'left' or 'right' functions to rotate the turtle in the appropriate direction.
    - Use the turtle's 'fillcolor' to set the fill color, and 'begin_fill', and 'end_fill' to control which lines drawn by the turtle should be filled with color.
    - Use the 'print_turtle_position' function defined in this file to print the turtle's current position at the beginning of each loop iteration.
    - Use a for loop to repeat the process of drawing a side and rotating 90 degrees four times until the square is drawn.

    :param t: The turtle to use to draw.
    :param start_x: The x coordinate from which to start the square.
    :param start_y: The y coordinate from which to start the square.
    :param length: The length of each side of the square in pixels - dots on the screen.
    :param rotation_direction: Either 'left' or 'right', indicating the direction the turtle should rotate after it completes each line of the rectangle.
    :param fill_color: The color with which to fill in the area drawn by the turtle.
    """
    pick_up_and_move_turtle(t, start_x, start_y)
    t.fillcolor(fill_color)
    t.begin_fill()
    for i in range(4):
        print_turtle_position(t)
        t.forward(length)
        if rotation_direction == "left":
            t.left(90)
        elif rotation_direction == "right":
            t.right(90)
    t.end_fill()
        

def draw_star(
    t, start_x, start_y, length, angle, initial_rotation_direction, fill_color
):
    """
    Draw a five-pointed star, starting from a given position.
    - Use the 'pick_up_and_move_turtle' function definied in this file to move the turtle to its starting position.
    - Use the turtle's 'forwards' function to move the turtle forwards.
    - Use the turtle's 'left' and 'right' functions to rotate the turtle in the appropriate directions to draw each line.
    - Use the turtle's 'fillcolor' to set the fill color, and 'begin_fill', and 'end_fill' to control which lines drawn by the turtle should be filled with color.
    - Use the 'print_turtle_position' function defined in this file to print the turtle's current position at the beginning of each loop iteration.
    - Use a for loop to repeat the process of drawing each of the five points of the star (each point is made up of two lines).

    :param t: The turtle to use to draw.
    :param start_x: The x coordinate from which to start the square.
    :param start_y: The y coordinate from which to start the square.
    :param length: The length of each line of the stra in pixels - dots on the screen.
    :param angle: The larger of the two angles used to connect lines.  The smaller angle should be calculated as the larger angle minus 72.
    :param initial_rotation_direction: The direction of the first rotation the turtle should make when drawing each point, either 'left' or 'right'.
    :param fill_color: The color with which to fill in the area drawn by the turtle.
    """
    pick_up_and_move_turtle(t, start_x, start_y)
    t.fillcolor(fill_color)
    t.begin_fill()
    for i in range(5):
        print_turtle_position(t)
        t.forward(length)
        if initial_rotation_direction == "right":
            t.right(angle)
            t.forward(length)
            t.left(angle - 72)
        else:
            t.left(angle)
            t.forward(length)
            t.right(angle - 72)
    t.end_fill()