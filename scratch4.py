from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Stuff')

frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
# the padding will increase padding inside the frame

frame.pack(padx=10, pady=10)
# the padding will increase padding of the whole window

b = Button(frame, text="Dont Click Here!")
b.pack()

root.mainloop()
