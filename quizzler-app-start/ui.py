from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.true = PhotoImage(file="./images/true.png")
        self.false = PhotoImage(file="./images/false.png")
        self.canvas = Canvas(height=500, width=500, bg=THEME_COLOR, highlightthickness=0)
        self.canvas.grid(row=0,column=0, columnspan=2)

        self.score_label = Label(text=f"Score: 0")
        self.score_label.grid(row=0, column= 1)


        # buttons
        self.true_button = Button(image=self.true, )
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false)
        self.false_button.grid(row=2, column=1)



        self.window.mainloop()

