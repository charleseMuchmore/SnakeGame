from turtle import Turtle

GRID_COLOR = "gray"

class Grid(Turtle):

    grid_color = "gray"

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(296, 297)
        self.setheading(180)
        self.forward(10)
        self.right(90)
        self.forward(10)
        self.left(90)
        self.pencolor(GRID_COLOR)
        self.initialize()
        self.pendown()

    def initialize(self):
        self.forward(580)
        self.left(90)
        self.forward(20)
        self.left(90)

    def turn(self, right_left):
        if right_left == "right":
            self.right(90)
            self.forward(20)
            self.right(90)
        elif right_left == 'left':
            self.left(90)
            self.forward(20)
            self.left(90)

    def grid(self, forward_amount, times):
        for num in range(times + 1):
            self.forward(forward_amount)
            self.turn("right")
            self.forward(forward_amount)
            self.turn('left')

    def retrace(self):
        self.left(90)
        self.pencolor("black")
        self.forward(20)
        self.right(90)
        self.pencolor(GRID_COLOR)

