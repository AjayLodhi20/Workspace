import random
from turtle import Turtle, Screen
import random
tim = Turtle()
color = ["blue", 'red', 'yellow']
for sides in range(3, 11):
    for i in range(sides):
        tim.color(random.choice(color))
        tim.forward(70)
        tim.right(360/sides)


screen = Screen()
screen.exitonclick()

# tim.shape('turtle')
# tim.color("sky blue")
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#     tim.fd(100)

# tim.pensize(2)
# tim.speed(5)
#
# for i in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)