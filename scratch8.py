from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Stuff')

root.filename = filedialog.askopenfilename(
    intialdir="/Users/fashi/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/images",
    title="Select A file", filetypes=(("jpg files"),("*.jpg"),("all files","*.*")))

root.mainloop()
