from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        readfile = open("HIGH_score.txt", mode="r")
        self.highs = readfile.read()
        self.highscore = int(self.highs)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} high score :{self.highscore} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            newhigh = open("HIGH_score.txt", mode="w")
            newhigh.write(f"{self.score}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1

        self.update_scoreboard()
