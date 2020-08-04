from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title('Stuff')
root.geometry("400x400")

# database

# Create a database or connect to a database
conn = sqlite3.connect('address_book.db')

# Create curor
c = conn.cursor()

#create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
) """)

# commit changes
conn.commit()
# close connection
conn.close()

root.mainloop()
