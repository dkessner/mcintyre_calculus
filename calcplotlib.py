#!/usr/bin/env python
#
# calcplotlib.py
#


import turtle

# Get the window dimensions.
WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()
x_max = int(WIDTH / 2)
x_min = -x_max
y_max = int(HEIGHT / 2)
y_min = -y_max

# Hide the turtle while drawing.
turtle.hideturtle()

def draw_axis(x_start, y_start, x_end, y_end):
    """Draws an axis between two points"""
    turtle.tracer(False)
    # Set the drawing color.
    turtle.color("black")
    # Go to the start position.
    turtle.penup()
    turtle.goto(x_start, y_start)
    # Point towards the end position.
    heading = turtle.towards(x_end, y_end)
    turtle.seth(heading)
    # Draw the line.
    turtle.pensize(2)
    turtle.pendown()
    turtle.goto(x_end, y_end)
    # Stamp the turtle's shape.
    turtle.stamp()
    turtle.tracer(True)

def draw_axes():
    """Draws the x- and y-axes."""
    # x-axis
    draw_axis(x_min, 0, x_max - 11, 0)
    # y-axis
    draw_axis(0, y_min, 0, y_max - 3)

def draw_plot(f, color):
    """Plots a function in a given color"""
    turtle.tracer(False)
    turtle.penup()
    # Go to the starting point.
    x_start = x_min
    y_start = f(x_min)
    turtle.goto(x_start, y_start)
    # Plot the function.
    turtle.pencolor(color)
    turtle.pensize(3)
    turtle.pendown()
    for x in range(x_min, x_max, 1):
        y = f(x)
        turtle.goto(x, y)
    turtle.tracer(True)

def clear():
    """Clears the Turtle Graphics window."""
    turtle.tracer(False)
    turtle.home()
    turtle.clear()
    turtle.tracer(True)

def left_sum(f, x_start, x_end, dx=0.0001):
    """Estimates a function's integral with a left Riemann sum"""
    integral = 0
    x = x_start
    while x < x_end:
        integral += f(x) * dx
        x += dx
    return integral

def draw_rect(x, y, width, height, stroke, fill=None):
    """Draws a rectangle that can be filled with a given color"""
    turtle.pencolor(stroke)
    turtle.pensize(1)
    if fill != None:
        turtle.fillcolor(fill)
        turtle.begin_fill()
    turtle.begin_poly()
    turtle.goto(x, y)
    turtle.goto(x, y + height)
    turtle.goto(x + width, y + height)
    turtle.goto(x + width, y)
    turtle.goto(x, y)
    turtle.end_poly()
    if fill != None:
        turtle.end_fill()


def draw_riemann(f, x_start, x_end, dx, stroke, fill=None):
    """Fills the area beneath a curve with rectangles """
    turtle.tracer(False)
    # Go to the starting point.
    turtle.penup()
    turtle.goto(x_start, 0)
    turtle.pendown()
    # Draw the rectangles.
    x = x_start
    y = 0
    while x < x_end:
        width = dx
        height = f(x)
        draw_rect(x, y, width, height, stroke, fill)
        x += dx
    turtle.tracer(True)


