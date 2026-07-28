import turtle
import pandas
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
score = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="what is the state name?")
    guess = answer_state.title()

    data = pandas.read_csv("50_states.csv")
    if data["state"].eq(guess).any():
        name = data[data["state"] == guess]
        x_cor = name.x
        y_cor = name.y
        score += 1
        t.penup()
        t.goto(x_cor,y_cor)
        t.write(name["state"])
        print(name)
    else:
        continue


screen.exitonclick()