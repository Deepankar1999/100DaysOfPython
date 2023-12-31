from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("My Snake Game")

snake=Snake()
food=Food()
score=Scoreboard()


screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")


game_is_on=True

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
 
    #Collision detector for food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.add_score()
    
    #Collision detector for wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        screen.update()
        score.game_over()
    
    #Collision detector for snake tail
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment)<10:
            game_is_on=False
            screen.update()
            score.game_over()

     



screen.exitonclick()