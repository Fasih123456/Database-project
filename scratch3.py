from tkinter import *
from PIL import ImageTK,Image

root = Tk()
root.title('Title stuff')
#root.iconbitmap('c:/gui/codemy.ico') will give an icon to your program on the top left side

my_img = ImageTK.PhotoImage(Image.open("aspen.png")) #image uploaded
my_label = Label(image=my_img).pack()

button_quit = Button(root,text="Exit Program", command=root.quit).pack() #a quite button

root.mainloop()