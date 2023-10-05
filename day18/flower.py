import turtle as t
from random import randint

tim=t.Turtle()

tim.speed("fastest")

for _ in range(1000):
    tim.speed(20)
    tim.color("black","Yellow")
    tim.begin_fill()

    for i in range(50):
        tim.forward(300)
        tim.left(170)

    tim.end_fill()
    tim.penup()
    tim.goto(randint(-150,0),randint(0,150))
    tim.pendown()

screen=t.Screen()
screen.exitonclick()