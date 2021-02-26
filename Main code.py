import tkinter
import tkinter.messagebox
from tkinter import *
import string as st

bg_colour ='blue'
if bg_colour =='blue':
    calc_colour = 'royal blue'
    input_colour = 'royalblue1'

calc_lock = True
# Let's create the Tkinter window
window = tkinter.Tk()
window.configure(bg=bg_colour)
window.iconbitmap('/Users/111117/Desktop/icon/yes.ico')
window.title("Shipley Painters")

Label(window, bg=bg_colour, text = "Name").grid(row = 0)
name = Entry(window)
name.grid(row = 0, column = 1)
name.configure(bg=input_colour)

Label(window, bg=bg_colour, text = "Email").grid(row = 1)
email = Entry(window)
email.grid(row = 1, column = 1)
email.configure(bg=input_colour)

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

Label(window, bg=bg_colour, text = "ISBN No.").grid(row = 6, column = 0)
isbn = Entry(window)
isbn.grid(row = 6, column = 1)
isbn.configure(bg=input_colour)

Label(window, bg=bg_colour, text = "P. No.").grid(row = 6, column = 2)
page = Entry(window)
page.grid(row = 6, column = 3)
page.configure(bg=input_colour)

def check_info():
    global calc_lock
    nname = name.get()
    mail = email.get()
    pnum = page.get()
    hheight = height.get()
    ISBN = isbn.get()
    if len(name.get()) <2:
        tkinter.messagebox.showinfo("Invalid Name Entry", "Name too short")
    elif not nname.isalpha():
        tkinter.messagebox.showinfo("Invalid Name Entry", "Name must not contain numbers")
    elif mail.find("@") <0:
        tkinter.messagebox.showinfo("Invalid Email Entry", "Invalid Email")
    elif not ISBN.isdigit():
        tkinter.messagebox.showinfo("Invalid ISBN Entry", "ISBN should be numerical")
    elif len(isbn.get()) !=10:
        isbn_len = len(isbn.get())
        tkinter.messagebox.showinfo("Invalid ISBN Number", f"ISBN needs to include 10 Numbers, not {isbn_len} ")
    elif not pnum.isdigit():
        tkinter.messagebox.showinfo("Invalid Page Entry", "Page should be a number")
    elif not pnum.find("0", 0, 1):
        tkinter.messagebox.showinfo("Invalid Page Entry", "Page should be a number that's above 0")
    elif not hheight.isdigit():
        tkinter.messagebox.showinfo("Invalid Height Entry", "Height field should be numerical")
    elif len(height.get()) < 1:
        tkinter.messagebox.showinfo("Invalid Height", "Height field is required and can't be blank")
    elif not l1.get().isdigit() or not l2.get().isdigit() or not l3.get().isdigit() or not l4.get().isdigit():
        tkinter.messagebox.showinfo("Invalid Length input", "Lengths must be numerical")
    elif len(l1.get()) < 1 or len(l2.get()) < 1 or len(l3.get()) < 1 or len(l4.get()) < 1:
        tkinter.messagebox.showinfo("Invalid Lengths", "4 lengths are needed")
    else:
        tkinter.messagebox.showinfo("Perfect!", "All requirements are set!")
        calc_lock = False
        if calc_lock ==False:
            tkinter.Button(window, bg=calc_colour, text = "Calculate", command = perform_calc).grid(row = 15, column = 2)

tkinter.Button(window, bg=calc_colour, text = "Check info", command = check_info).grid(row = 15, column = 1)

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
if calc_lock ==False:
    tkinter.Button(window, bg=calc_colour, text = "Calculate", command = perform_calc).grid(row = 15, column = 2)

window.mainloop()
