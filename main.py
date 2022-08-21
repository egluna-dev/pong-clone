from turtle import Turtle, Screen
from paddle import Paddle
# from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Classic")
screen.tracer(0)

paddle = Paddle()
paddle.goto(350, 0)


screen.listen()
screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)

program_on = True
while program_on:
    screen.update()
screen.exitonclick()
