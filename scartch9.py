from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Stuff')
root.geometry("400x400")  # size of the main screen

vertical = Scale(root, from_=0, to=200)
# vertical slide bar, from and to is the cordinates to slide to. Do not use .pack() diretly on this
vertical.pack()


def slide(): #if function is giving an error do slide(var)
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=slide)
horizontal.pack()

my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
