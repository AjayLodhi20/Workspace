from tkinter import *

window = Tk()
window.minsize(width=400, height=200)
window.title("Mile to Km converter")
# is equal to label
equal_label = Label(text="is equal to")
equal_label.config(padx=100, pady=100)
equal_label.grid()

# calculate kms label
#
km_label = Label()

def km_calculate():
    number = input.get()
    number = int(number)
    km = int(number * 1.6)
    km_label.config((km))

button = Button(text="Calculate",command=km_calculate)
button.grid(column=1, row=1)

input = Entry(width=20)
input.grid(column= 2, row=3)

window.mainloop()