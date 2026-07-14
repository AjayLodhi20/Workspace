import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

turtle.colormode(255)

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

tim.speed(0)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(get_random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
