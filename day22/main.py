from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#TODO 1. Setting Up Screen
#TODO 2. Create and move  paddles
#TODO 3. Create another paddle
#TODO 4. Create the ball and make it move
#TODO 5. Detect collision with wall and bounce
#TODO 6. Detect collision with paddle
#TODO 7. Detect when paddle misses
#TODO 8. Keep score
 
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))


screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

ball=Ball()
score=Scoreboard()

game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #detection collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()
    
    #detect collision with 
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor() < -320: 
        ball.bounce_x()
    
    #detect right paddle misses
    if ball.xcor()>380:
        ball.reset_positions()
        score.l_point()

    
    if ball.xcor() < -380:
        ball.reset_positions()
        score.r_point()

    

screen.exitonclick()