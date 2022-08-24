from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setheading(float(randint(0, 360)))
        self.sleep_time = 0.1
        self.move_x = 10
        self.move_y = 10

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.move_y *= -1

    def bounce_paddle(self):
        self.move_x *= -1
        self.sleep_time *= 0.95

    def reset_ball(self):
        self.setposition(0, 0)
        self.sleep_time = 0.1
        self.move_x *= -1
