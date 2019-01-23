import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Welcome To the Student Management System")

tb = tk.Label(root, text="Student Management System", width=50)

tb.grid(row=0, columnspan=2, padx=(30,30), pady=(30, 0))

name1 = Entry(root)
college1 = Entry(root)
phone1 = Entry(root)
address1 = Entry(root)

name = tk.Label(root, text="Enter your name", width=40, anchor='w')\
    .grid(row=1, column=0, padx=(30,0), pady=(30, 0))
name1.grid(row=1, column=1, padx=(0,50), pady=(30, 20))

college = tk.Label(root, text="Enter your college", width=40, anchor='w')\
    .grid(row=2, column=0, padx=(30,0))
college1.grid(row=2, column=1, padx=(0,50), pady = 20)

phone = tk.Label(root, text="Enter your phone number", width=40, anchor='w')\
    .grid(row=3, column=0, padx=(30,0))
phone1.grid(row=3, column=1, padx=(0,50), pady = 20)

address = tk.Label(root, text="Enter your address", width=40, anchor='w')\
    .grid(row=4, column=0, padx=(30,0))
address1.grid(row=4, column=1, padx=(0,50), pady = 20)

button = tk.Button(root, text="Take input")
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(root, text="Display result")
displayButton.grid(row=5, column=1)

root.mainloop()