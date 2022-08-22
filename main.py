from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Classic")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

program_on = True
while program_on:
    screen.update()
    time.sleep(ball.sleep_time)
    ball.move_ball()
    # Detect collision with upper and lower boundaries
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 40 or ball.distance(left_paddle) < 40) and (ball.xcor() > 330 or ball.xcor() < -330):
        ball.bounce_paddle()
        ball.sleep_time -= 0.01

    # Detect paddle collision with upper and lower boundaries
    # if left_paddle.ycor() > 290 and left_paddle.ycor() < -290 and right_paddle.ycor() > 290 and right_paddle.ycor() < -290:
    #     left_paddle.backward(20)
    #     right_paddle.backward(20)

    # Detect if ball goes beyond left paddle
    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.increase_right_score()

    # Detect if ball goes beyond right paddle
    if ball.xcor() > 390:
        ball.reset_ball()
        scoreboard.increase_left_score()

screen.exitonclick()
