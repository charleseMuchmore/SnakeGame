from turtle import Turtle
import random
COLORS = ("red", "green", "blue", "purple", "yellow", "orange", "cyan", "magenta")


class CreateFood(Turtle):

    def __init__(self):
        super().__init__()

    def regenerate_a_food(self):
        self.penup()
        self.shape("circle")
        self.color(self.food_color())
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def food_color(self):
        """ Returns a random color from the list at the top"""
        return COLORS[(random.randint(0, len(COLORS)-1))]

    def refresh(self):
        """ Randomly resets an object's position and color"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(self.food_color())


class SetFood(CreateFood):

    def __init__(self):
        super().__init__()

    def set_food_num(self, num_food):
        food_objects = []
        for num in range(0, num_food):
            food = CreateFood()
            food.regenerate_a_food()
            food_objects.append(food)
        return food_objects


