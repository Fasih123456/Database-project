from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Stuff')
root.geometry("400x400")

var = StringVar()
# StringVar(), IntVar() is also another type of var, cant be used here tho

c = Checkbutton(root, text="Check this box!", variable=var, onvalue="On", offvalue="Off")
# the CheckButton function has a small bug on the onvalue and offvalue, so there is a small work around
c.deselect() #Mandatory if onvalue or offvalue are used to avoid glitch
c.pack()


def show():
    myLabel = Label(root, text=var.get()).pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
