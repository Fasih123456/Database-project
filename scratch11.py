from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Stuff')
root.geometry("400x400")

#Drop Down Boxes
def show():
    myLabel = Label(root,text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
clicked.set(options[0]) #Default value

drop = OptionMenu(root, clicked, *options)
#if you dont put the star is will just print the whole thing
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
