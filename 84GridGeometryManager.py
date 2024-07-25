# 84. Grid Geometry Manager[08:31:00]--------------------------------
from tkinter import *
window=Tk()
# grid() = geometry manager that organizes widgets in a table-like structure in a parent
titleLabel = Label(window,text="Enter you into", font=("Arial",25)).grid(row=0,column=0,columnspan=2)
firstNameLabel = Label(window,text="First Name: ",bg='red',width=20).grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)
lastNameLabel = Label(window,text="Last Name: ",bg='green').grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)
emailLabel = Label(window,text="Email: ",bg='blue',width=30).grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)
submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)


window.mainloop()
