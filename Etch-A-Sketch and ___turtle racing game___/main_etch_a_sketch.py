from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(5)

def clockwise():
    tim.right(5)

def clear_Screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(fun= move_forwards, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_Screen, key="c")
screen.exitonclick()