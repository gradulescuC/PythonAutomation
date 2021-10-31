from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Choose numbers!")
window.geometry("500x200")

def number1():
    if num1.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 1")

def number2():
    if num2.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 2")

def number3():
    if num3.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 3")

def number4():
    if num4.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 4")

def number5():
    if num5.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 5")

def number6():
    if num6.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 6")

def number7():
    if num7.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 7")

def number8():
    if num8.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 8")

def number9():
    if num9.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 9")

def number10():
    if num10.get() == 1:
        tkinter.messagebox.showinfo("Hello", "You choose number 10")

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()
num6 = IntVar()
num7 = IntVar()
num8 = IntVar()
num9 = IntVar()
num10 = IntVar()

c1 = Checkbutton(window, text="1", variable=num1, command=number1, height = 5, width = 10)
c1.grid(row=0, column=0)
c2 = Checkbutton(window, text="2", variable=num2, command=number2, height = 5, width = 10)
c2.grid(row=0, column=1)
c3 = Checkbutton(window, text="3", variable=num3, command=number3, height = 5, width = 10)
c3.grid(row=0, column=2)
c4 = Checkbutton(window, text="4", variable=num4, command=number4, height = 5, width = 10)
c4.grid(row=0, column=3)
c5 = Checkbutton(window, text="5", variable=num5, command=number5, height = 5, width = 10)
c5.grid(row=0, column=4)
c6 = Checkbutton(window, text="6", variable=num6, command=number6, height = 5, width = 10)
c6.grid(row=1, column=0)
c7 = Checkbutton(window, text="7", variable=num7, command=number7, height = 5, width = 10)
c7.grid(row=1, column=1)
c8 = Checkbutton(window, text="8", variable=num8, command=number8, height = 5, width = 10)
c8.grid(row=1, column=2)
c9 = Checkbutton(window, text="9", variable=num9, command=number9, height = 5, width = 10)
c9.grid(row=1, column=3)
c10 = Checkbutton(window, text="10", variable=num10, command=number10, height = 5, width = 10)
c10.grid(row=1, column=4)

window.mainloop()