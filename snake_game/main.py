# TODO: create a snake body
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# TODO: move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# detect collision with food
    if snake.head.distace(food) <15:
        food.refresh()











screen.exitonclick()