import math
from tkinter import *

root = Tk()


def myClick():
    myLabelfunction = label(root, text="Look! I clicked a button!!")
    myLabelfunction.pack()

#You cannot do a pack and grid or grid and pack, except for some circumstances

# creating a label widget
mylabel1 = Label(root, text="Hello World!")
mylabel2 = Label(root, text="Hello World!")
# shoving it on to the screen
# mylabel.pack()

# places them precicisly
mylabel1.grid(row=0, column=1)
mylabel2.grid(row=1, column=1)

# buttons
myButton = Button(root, text="Click Me!")
# can also do myButton = Button(root,text="Click Me!",state=DISABLED,padx = 50, pady= 50,command=myClick(),fg="blue",bg="red") to make the button disabled so it cannot be clicked
# padx = height pady = width
# command=myClick() button is connected to the function myClick
# fg="blue" color of text is blue, bg="red" background of button is red
myButton.pack()

# Entry widget
e = Entry(
    root)  # size can be changed by doing ,width or height. bg and fg can be used. borderwidth can be used as well.
e.pack()  # bascially a text box
e.get()  # cin >> for python

root.mainloop()
