import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.width(10)
tim.speed(1)
turtle.colormode(255)

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
directions = [0, 90, 180, 270]
while True:
    tim.color(get_random_color())
    chosen_direction = random.choice(directions)
    tim.setheading(chosen_direction)
    tim.forward(25)
screen = Screen()
screen.exitonclick()