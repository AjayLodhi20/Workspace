from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.config(pady=20, padx=20)
# is equal to label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
# calculate kms label

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)
#
km_label = Label(text="km")
km_label.grid(column=2, row=1)

def km_calculate():
    miles = float(input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


button = Button(text="Calculate",command=km_calculate)
button.grid(column=1, row=2)

input = Entry(width=20)
input.grid(column= 1, row=0)

window.mainloop()