from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Stuff')

# r = IntVar()  # this is kind of like r.get(), when the button is pressed it will either get the value 1 or 2
# r.set("2") #will set the value of r to something

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    # so we are looping through MODES and the the first value will be text and the second value will be modes
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1, command = lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command = lambda: clicked(r.get())).pack()


myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()
