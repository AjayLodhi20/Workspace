from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()


    def create_paddle(self, x, y):
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(x,y)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)







