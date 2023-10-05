import random as rn
import turtle as t

tim=t.Turtle()
t.colormode(255)
tim.speed("fastest")

def randomColour():
    red=rn.randint(0,255)
    green=rn.randint(0,255)
    blue=rn.randint(0,255)
    return (red,green,blue)

for _ in range(100):
    tim.color(randomColour())
    tim.circle(100)
    tim.setheading(tim.heading()+10)

screen=t.Screen()
screen.exitonclick()