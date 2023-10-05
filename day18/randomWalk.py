import turtle as t
import random as rn


tim=t.Turtle()

def randomColour():
    red=rn.randint(0,255)
    green=rn.randint(0,255)
    blue=rn.randint(0,255)
    return (red,green,blue)

Colours=["red","green","blue","black","orange","cyan","aqua","brown"]
directions=[0,90,180,270]

tim.pensize(15)
tim.speed("fastest")
t.colormode(255)

for _ in range(1000):
    tim.color(randomColour())
    tim.forward(20)
    tim.setheading(rn.choice(directions))

screen=t.Screen()
screen.exitonclick()

