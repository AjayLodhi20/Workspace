from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("The pong game")

paddle1 = Paddle()
paddle2 = Paddle()
screen.tracer(0)
paddle1.create_paddle(x=350, y=0)
paddle2.create_paddle(x= -350, y = 0)
screen.listen()


screen.onkey(paddle1.move_up, 'Up')
screen.onkey(paddle2.move_up, 'w')
screen.onkey(paddle1.move_down, 'Down')
screen.onkey(paddle2.move_down, 's')

screen.update()




screen.exitonclick()