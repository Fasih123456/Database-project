from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Stuff')
def opening():
    global my_img #if global is not used image will not be displayed but screen will open
    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open("images/photo1.jpg"))
    my_label = Label(top, image=my_img).pack()

btn = Button(root,text="Open Second Windo",command=opening).pack()



root.mainloop()