from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make Your Bet", prompt="Which Turtle Will Win the Race? Enter A Color:")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtles_pos in range(6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.color(colors[turtles_pos])
    new_turtle.penup()
    new_turtle.goto(-230,y_positions[turtles_pos])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"Congratulations!!The winner is {winning_color} turtle")
            else:
                print(f"So sorry!!The winner is {winning_color} turtle")
        turtle.forward(random.randint(1,10))






screen.exitonclick()
