from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("May's Pong Game")
screen.tracer(0)
ball = Ball()
score = Score()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()