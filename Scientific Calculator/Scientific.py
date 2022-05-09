from tkinter import *
import math
import tkinter.messagebox

root = Tk()

root.title("Scientific Calculator")

root.configure(background = "red")

root.resizable(width = False, height = False)
root.geometry ("480*568")

calc = Frame(root)
calc.grid()

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Standard")
filemenu.add_command(label = "Scientific")
file.add_seperator()
filemenu.add_command(label = "Exit")


root.configure(menu = menubar)
root.mainloop()
