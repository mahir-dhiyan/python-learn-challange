# 68. Labels [06:14:47]--------------------------------------------------
# label = an area widget that holds text and/or and image within a window
from tkinter import *
window= Tk()
window.title("Another GUI for Labels")
# window.geometry("420x420")
photo = PhotoImage(file="logo.png")
# window.config(background="black")
label = Label(window,
              text="Hello World. Do you know how to code?",
              font=('Arial',49,'bold'),
              fg='#00FF00',
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
# label.place(x=0,y=0)
window.mainloop()