import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

is_race_on = False

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle are you betting on?")
colors = ["red", "orange", "yellow", "green", "blue"]
y_positions = [80, 40, 0, -40, -80]

all_turtles = []

for turtle_index in range(5):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():  # Added .lower() in case user types "Red" instead of "red"
                print(f"YOU WON... your {winning_color} turtle won!")
            else:
                print(f"You lost! The {winning_color} turtle won.")

screen.exitonclick()