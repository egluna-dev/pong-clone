import turtle as t
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Classic")
screen.tracer(0)

user_scoreboard = Scoreboard()


screen.exitonclick()
