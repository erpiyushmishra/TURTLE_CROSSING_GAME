from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()

        self.level=1
        self.update()
    def update(self):
        self.clear()
        self.goto(-240, 260)
        self.write("LEVEL", align="center", font=FONT)
        self.goto(-180,260)
        self.write(self.level, align="center", font=FONT)
        self.hideturtle()
    def scoreboard_update(self):
        self.level+=1
        self.update()
    def game_finish(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=FONT)

