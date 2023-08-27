from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=paddle1.move_up)
screen.onkey(key="Down", fun=paddle1.move_down)
screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

    if ball.distance(paddle1) <= 50 and ball.xcor() >= 340 or ball.distance(paddle2) <= 50 and ball.xcor() <= -340:
        ball.bounce_paddle()
        ball.move_speed *= 0.9

    if ball.xcor() > 380 or ball.xcor() < -380:
        paddle1.goto(350, 0)
        paddle2.goto(-350, 0)
        if ball.xcor() > 380:
            ball.paddle1_miss()
            scoreboard.l_point()
        else:
            ball.paddle2_miss()
            scoreboard.r_point()
        ball.goto(0, 0)
