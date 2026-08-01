from tkinter import *

window = Tk() #screen creating
window.title("first program") # title of the screen(on the top)
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text=" i am a label", font=("Aerial", 24, "bold"))# what is displayed inside the label(on screen)
my_label.grid(column=0, row=0) #makes the label to write on the left side
my_label.config(pady=50, padx=50)

my_label["text"] = "New Text"
my_label.config(text= "hello ajay")

# button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


def new_button2():
    print("hello new button")

new_button = Button(text="check", command=new_button2)
new_button.grid(row=0, column=2)






window.mainloop() #keep the window on screen