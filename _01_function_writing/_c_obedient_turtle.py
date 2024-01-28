"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle
import webbrowser

def makesquare():
    for i in range(4):
        cheese.forward(100)
        cheese.right(90)
def maketri():
    for i in range(3):
        cheese.forward(100)
        cheese.right(120)
def makespin():
    cheese.circle(100)

def play_video(url):
    webbrowser.open(url)
if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    window = turtle.Screen()
    window.bgcolor('white')

    cheese = turtle.Turtle()
    WHATSHAPE = simpledialog.askstring(None, prompt="give me shape now")
    if WHATSHAPE == 'circle':
        makespin()
    elif WHATSHAPE == 'square':
        makesquare()
    elif WHATSHAPE == 'triangle':
        maketri()
    elif WHATSHAPE == 'chip':
        play_video('https://www.youtube.com/watch?v=coaN2VBNgYA')
    elif WHATSHAPE =='jynxzi':
        play_video('https://www.youtube.com/shorts/qNrBZy4brw8')
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass
