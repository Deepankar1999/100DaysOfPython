import turtle as t
import random as r

tim=t.Turtle()

def randomColor():
    Colors=["red","green","blue","black","orange","cyan","aqua","brown"]
    return r.choice(Colors)

def drawShape(num_sides):
    angle=360/num_sides
    color_draw=randomColor()
    tim.pencolor(color_draw)
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)



for num_sides in range(3,11):
    drawShape(num_sides)

screen=t.Screen()
screen.exitonclick()