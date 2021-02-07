import tkinter
import tkinter.messagebox
from tkinter import *

bg_colour ='blue'
if bg_colour =='blue':
    calc_colour = 'royal blue'
    input_colour = 'royalblue1'


# Let's create the Tkinter window
window = tkinter.Tk()
window.configure(bg=bg_colour)
window.iconbitmap('/Users/111117/Desktop/icon/yes.ico')
window.title("Shipley Painters")

Label(window, bg=bg_colour, text = "Name").grid(row = 0)
name = Entry(window)
name.grid(row = 0, column = 1)
name.configure(bg=input_colour)

Label(window, bg= bg_colour, text = "Height").grid(row = 0, column = 15)
height = Entry(window)
height.grid(row = 0, column = 16)
height.configure(bg=input_colour)

Label(window, bg=bg_colour, text = "Length Wall 1").grid(row = 3, column = 15)
l1 = Entry(window)
l1.grid(row = 3, column = 16)
l1.configure(bg=input_colour)

Label(window, bg=bg_colour,text = "Length Wall 2").grid(row = 4, column = 15)
l2 = Entry(window)
l2.grid(row = 4, column = 16)
l2.configure(bg=input_colour)

Label(window, bg=bg_colour, text = "Length Wall 3").grid(row = 5, column = 15)
l3 = Entry(window)
l3.grid(row = 5, column = 16)
l3.configure(bg=input_colour)

tkinter.Label(window, bg=bg_colour, text = "Length Wall 4").grid(row = 6, column = 15)
l4 = tkinter.Entry(window)
l4.grid(row = 6, column = 16)
l4.configure(bg=input_colour)

paint_choice = IntVar()
paint_choice.set(2)
tkinter.Radiobutton(window, bg=bg_colour, text = "Luxury", variable = paint_choice, value = 1).grid(row = 4, column = 0)
tkinter.Radiobutton(window, bg=bg_colour, text = "Standard", variable = paint_choice, value = 2).grid(row = 4, column = 1)
tkinter.Radiobutton(window, bg=bg_colour, text = "Economy", variable = paint_choice, value = 3).grid(row = 4, column = 2)

use_undercoat = IntVar()
undercoat = Checkbutton(window, bg=bg_colour, text = "Undercoat", variable=use_undercoat)
undercoat.grid(row = 5, column = 1)


def perform_calc():
    paint_quality =  paint_choice.get()
    area = int(height.get()) * (int(l1.get()) + int(l2.get()) + int(l3.get()) + int(l4.get()))
    paint_cost = 0
    if paint_quality ==1:
        paint_cost = 1.90
    elif paint_quality ==2:
        paint_cost = 1.00
    else:
        paint_cost = 0.60

    if use_undercoat.get():
        paint_cost +=0.50

    total_paint_cost = paint_cost * area

    itemised_total = f"total area = {area} \n"
    itemised_total += f"Paint cost = {total_paint_cost}"

    tkinter.messagebox.showinfo("Alert Message", itemised_total)

tkinter.Button(window, bg=calc_colour, text = "Calculate", command = perform_calc).grid(row = 14, column = 1)

window.mainloop()
