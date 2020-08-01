from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Title stuff')

my_img0 = ImageTk.PhotoImage(Image.open("images/Photo0.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("images/Photo1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/Photo2.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/Photo4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/Photo5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/Photo6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/Photo7.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("images/Photo9.jpg"))

image_list = [my_img0, my_img1, my_img2, my_img4, my_img5, my_img6, my_img7, my_img9]

my_label = Label(image=my_img0, width=200, height=200).grid(row=0, column=0, columnspan=3)

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


# bd =1 makes a border with thickness 1, relief is how the broder will behave
# anchor=E , will make it go east


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    my_label = Label(image=image_list[image_number - 1], width=200, height=200)

    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    # Status Bar Update
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label = Label(image=image_list[image_number - 1], width=200, height=200)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    # Status Bar Update
    status = Label(root, text="Image " + str(image_number) + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=lambda: back(0), state=DISABLED)
# if you want to pass anything through a button you use lambda
button_exit = Button(root, text="X", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
button_back.grid(row=1, column=0, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)
# sticky = W+E will strecth from west to east
root.mainloop()
