from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans", 36, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.left_score == 10:
            self.write(f"Game Over! Left player has won!",
                       align="center", font=FONT)
        elif self.right_score == 10:
            self.write(f"Game Over! Right player has won!",
                       align="center", font=FONT)
