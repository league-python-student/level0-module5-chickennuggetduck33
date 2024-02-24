"""
Have the turtle draw a row of houses.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle
import random

cheese = turtle.Turtle()
cheese.penup()
cheese.speed(0)
def draw_pointy_house(hight):
    cheese.pendown()
    cheese.left(90)
    cheese.pencolor('black')
    cheese.forward(hight)
    cheese.right(90)
    cheese.forward(100)
    cheese.left(135)
    cheese.forward(71)
    cheese.left(90)
    cheese.forward(71)
    cheese.left(135)
    cheese.forward(100)
    cheese.right(90)
    cheese.forward(hight)
    cheese.right(90)
    cheese.forward(100)
    cheese.right(90)
    cheese.penup()
    cheese.right(90)
    cheese.forward(40)
    cheese.left(90)
    cheese.pendown()
    cheese.forward(40)
    cheese.right(90)
    cheese.forward(20)
    cheese.right(90)
    cheese.forward(40)
    cheese.penup()
    cheese.right(90)
    cheese.forward(90)
    cheese.right(180)
    cheese.pendown()
    cheese.pencolor('green')
    cheese.forward(160)


def draw_house(hight):
    cheese.pendown()
    cheese.left(90)
    cheese.pencolor('black')
    cheese.forward(hight)
    cheese.right(90)
    cheese.forward(100)
    cheese.right(90)
    cheese.forward(hight)
    cheese.right(90)
    cheese.forward(100)
    cheese.right(90)
    cheese.penup()
    cheese.right(90)
    cheese.forward(40)
    cheese.left(90)
    cheese.pendown()
    cheese.forward(40)
    cheese.right(90)
    cheese.forward(20)
    cheese.right(90)
    cheese.forward(40)
    cheese.penup()
    cheese.right(90)
    cheese.forward(90)
    cheese.right(180)
    cheese.pendown()
    cheese.pencolor('green')
    cheese.forward(160)
if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.


    cheese.goto(-440,-390)
    for i in range(7):
        g = random.randint(1, 3)
        b = 1
        d = random.randint(1, 2)
        if g == 1:
            b = 60
            draw_house(b)
        elif g == 2:
            b = 120
            draw_house(b)
        elif g == 3:
            b = 250
            draw_pointy_house(b)
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.daw
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    turtle.done()
