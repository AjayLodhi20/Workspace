from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()


    def create_paddle(self, x, y):
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(x,y)
        self.shapesize(stretch_wid=4, stretch_len=1)

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)




