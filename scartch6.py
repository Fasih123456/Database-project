from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Stuff')

def popup():
    response = messagebox.showinfo("This is my popup", "Hello World")
    #.showwarning, showerror, askquestion, askokcancel,, askyesno . Yes = 1, no = 0. ok = 1, cancel = 0. Clicking ok returns ok
    Label(root,text=response).pack()
    #if response == 1:
     #   Label(root, text="response yes").pack()
    #else:
    #    Label(root, text="response no").pack()

Button(root,text="Popup",command=popup).pack()

root.mainloop()