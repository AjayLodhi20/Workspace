from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card = {}
to_learn = {}


try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_vocabulary.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient = "records")



def next_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(to_learn)
    word = card["word"]
    canvas.itemconfig(title, text= "french", fill= "black")
    canvas.itemconfig(main_word, text=word, fill = "black")
    canvas.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill= "white")
    canvas.itemconfig(main_word, text= card["meaning"], fill= "white")
    canvas.itemconfig(card_background, image= card_back)


def is_known():
    to_learn.remove(card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index= False)


    next_card()

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

tick_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image= card_front)


title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
main_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0 , row= 0, columnspan=2)


unknown_button = Button(image=wrong_img, command=next_card)
unknown_button.grid(row=1, column=0)
known_button = Button(image=tick_img, command= is_known)
known_button.grid(row=1, column=1)

next_card()



window.mainloop()

