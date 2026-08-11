from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("french_vocabulary.csv")
to_learn = data.to_dict(orient = "records")
print(to_learn)



def next_card():
    random.choice(to_learn)



window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

tick_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image= card_front)


canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text= "word", font=("Ariel", 60, "bold"))

canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0 , row= 0, columnspan=2)


unknown_button = Button(image=wrong_img, command=next_card)
unknown_button.grid(row=1, column=0)
known_button = Button(image=tick_img, command= next_card)
known_button.grid(row=1, column=1)





window.mainloop()

