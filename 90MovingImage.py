# 90. Moving Image[09:18:27]-----------------------------------------------
from tkinter import *

window=Tk()

# window.geometry("500X500")

myimage=PhotoImage(file='car.jpeg')
label=Label(window,image=myimage,bg="red")
label.place(x=0,y=0)


window.mainloop()