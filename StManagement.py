# Entry Program
#import ClassroomProject as st
import tkinter as tk
import DatabaseSample as dt
from tkinter import messagebox

#First Window
mainWindow = tk.Tk()
mainWindow.title("Welcome To the Student Management System")

heading_label = tk.Label(mainWindow, text="Student Management System")
heading_label.configure(background='grey')
heading_label.config(width=50)
heading_label.config(font=("Courier", 33))
heading_label.pack()

# name_field = tk.Entry(mainWindow)
# name_field.pack()

# Name
name_label = tk.Label(mainWindow, text="Enter Your Name : ")
name_label.pack()
name_field = tk.Entry(mainWindow)
name_field.pack()

# College
college_label = tk.Label(mainWindow, text="College")
college_label.pack()
college_field = tk.Entry(mainWindow)
college_field.pack()

#Address
address_label =tk.Label(mainWindow, text="Address")
address_label.pack()
address_field = tk.Entry(mainWindow)
address_field.pack()

# Phone
phone_label = tk.Label(mainWindow, text="Phone Number")
phone_label.pack()
phone_field = tk.Entry(mainWindow)
phone_field.pack()

#Second Window

def secWindow():
    secondWindow = tk.Tk()
    secondWindow.title("Student Information You Are Looking For")
    heading_label = tk.Label(secondWindow, text="Student Management System")
    heading_label.config(width=50)
    heading_label.config(font=("Courier", 33))
    heading_label.pack()

    # Name
    name_label = tk.Label(secondWindow, text="Name is : ")
    name_label.pack()
    name_field = tk.Label(secondWindow, text=obj.name)
    name_field.pack()

    # Phone
    phone_label = tk.Label(secondWindow, text="Phone Number is : ")
    phone_label.pack()
    phone_field = tk.Label(secondWindow, text=obj.phone)
    phone_field.pack()

    # College
    college_label = tk.Label(secondWindow, text="College")
    college_label.pack()
    college_field = tk.Label(secondWindow, text=obj.college)
    college_field.pack()
    secondWindow.mainloop()

#obj = st.StudentRecord()

def takeValueInput():

    # name = name_field.get()
    # phone = phone_field.get()
    # college = college_field.get()
    # obj.addRecord(name, phone, college)

    name = name_field.get()
    phone = int(phone_field.get())
    college = college_field.get()
    address = address_field.get()
    dt.datab(name, college, address, phone)

    messagebox.showinfo("Update", "Value Saved Successfully!!")
    name_field.delete(first=0, last="end")
    phone_field.delete(first=0, last="end")
    college_field.delete(first=0, last="end")

def showInfo():
    secWindow()

def retrieve():
    dt.ret()



button = tk.Button(mainWindow, text="Get Value", command=lambda: takeValueInput())
button.pack(side=tk.LEFT, pady=20)

displaybutton = tk.Button(mainWindow, text="Display Value", command=lambda: showInfo())
displaybutton.pack(side=tk.RIGHT, pady=20)

button = tk.Button(mainWindow, text="Retrieve value", command=lambda: retrieve())
button.pack(side=tk.LEFT, pady=20)

mainWindow.mainloop()
