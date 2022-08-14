from turtle import Turtle
SCOREBOARD_POS = (0, 286)
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(SCOREBOARD_POS)
        self.score = 0
        self.high_score = self.find_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.show_score()

    def increase_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))        
        self.score = 0
        self.clear()
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def find_highscore(self):
        with open("data.txt", mode="r") as file:
            new_high_score = file.read()
            return(int(new_high_score))