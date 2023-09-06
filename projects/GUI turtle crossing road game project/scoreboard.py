from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(-295,265)
        self.update()

    def update(self):
        self.clear()
        self.write(f"LEVEL: {self.level}",align="left",font=FONT)

    def levelupp(self):
        self.level += 1
        self.update()

    def gameover(self):
        self.goto(0,0)
        self.write("GMAE OVER",align="center",font=FONT)


