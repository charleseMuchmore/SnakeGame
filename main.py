from turtle import Screen
import time
from snake import Snake
from food import SetFood
from scoreboard import Scoreboard
from grid import Grid

# Snake #
snake = Snake()
# Screen #
screen = Screen()
screen.setup(width=596, height=620)
screen.tracer(n=0, delay=0)
screen.bgcolor("black")
screen.title("Snake Game")
# Screen Listening #
screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
# Scoreboard #
scoreboard = Scoreboard()
# Grid #
grid_turtle = Grid()
grid_turtle.grid(580, 14)
grid_turtle.retrace()
grid_turtle.left(90)
grid_turtle.grid(580, 14)
grid_turtle.retrace()
grid_turtle.hideturtle()
# Food Bits #
food = SetFood()
food.hideturtle()
food_objects = food.set_food_num(2)
# Game Loop #
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    for item in food_objects:
        if snake.head.distance(item) < 18:
            item.refresh()
            snake.extend()
            scoreboard.increase_score()
            scoreboard.show_score()

    if snake.head.xcor() > 276 or snake.head.xcor() < -286 or snake.head.ycor() > 282 or snake.head.ycor() < -298:
        scoreboard.reset()
        snake.reset()

    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
  


screen.exitonclick()
