from turtle import *

tim=Turtle()

def drawLine(turtle):
    tim=turtle
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()

for _ in range(5):
    drawLine(tim)

screen=Screen()
screen.exitonclick()

