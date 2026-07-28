import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="what's another state's name?").title()


    if answer_state == "Exit":
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)
missing_states = []
for i in all_states:
    if i not in guessed_states:
        missing_states.append(i)

states = {
    "Missing states": missing_states
}
data = pandas.DataFrame(states)
data.to_csv("missing states")
screen.exitonclick()