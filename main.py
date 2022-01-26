import tkinter
import tkinter.messagebox
from tkinter import *
window = tkinter.Tk()
label_title = tkinter.Label(window, font=("Arial", 25), text="Dog to Human age converter").grid(row=0, column=2)

#age text box
name_var = StringVar()
age_label = tkinter.Label(window, text="Age of dog :", font=("Arial", 12)).grid(row=1, column=0)
name_entry = tkinter.Entry(window, textvariable=name_var, font=("Arial", 10, "normal"))
name_entry.grid(row=1, column=2)

#calculation
def calc():
    tkinter.messagebox.showinfo("Human years", name_var.get())

calc_button = tkinter.Button(window, text="Calculate", command=calc)
calc_button.grid(row=6, column=2)

# main loop
window.mainloop()
