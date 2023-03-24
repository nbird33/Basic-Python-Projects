# Programmer: Noah Bird
# Date: 3/15/21-first coded
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Output: Write a program with loop(s) to draw the 
# checkerboard design using turtle graphics

import turtle

def main():
    turtle.hideturtle()

    square(-50, 200, 50, 'black')
    square(0, 200, 50, 'white')
    square(50, 200, 50, 'black')
    square(100, 200, 50, 'white')
    square(150, 200, 50, 'black')

    square(-50, 150, 50, 'white')
    square(0, 150, 50, 'black')
    square(50, 150, 50, 'white')
    square(100, 150, 50, 'black')
    square(150, 150, 50, 'white')

    square(-50, 100, 50, 'black')
    square(0, 100, 50, 'white')
    square(50, 100, 50, 'black')
    square(100, 100, 50, 'white')
    square(150, 100, 50, 'black')

    square(-50, 50, 50, 'white')
    square(0, 50, 50, 'black')
    square(50, 50, 50, 'white')
    square(100, 50, 50, 'black')
    square(150, 50, 50, 'white')

    square(-50, 0, 50, 'black')
    square(0, 0, 50, 'white')
    square(50, 0, 50, 'black')
    square(100, 0, 50, 'white')
    square(150, 0, 50, 'black')

# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

def square(x, y, width, color):
    turtle.penup()            # Raise the pen
    turtle.goto(x, y)         # Move to the specified location
    turtle.fillcolor(color)   # Set the fill color
    turtle.pendown()          # Lower the pen
    turtle.begin_fill()       # Start filling
    for count in range(4):    # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # End filling

main()

# Potential update -- leave checkerboard on screen after drawing
