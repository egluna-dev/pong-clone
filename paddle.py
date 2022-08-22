from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coords)
        self.up()
        self.down()

    def set_coords(self):
        pass

    def up(self):
        new_y_pos = self.ycor() + 20
        self.goto(self.xcor(), new_y_pos)

    def down(self):
        new_y_pos = self.ycor() - 20
        self.goto(self.xcor(), new_y_pos)
