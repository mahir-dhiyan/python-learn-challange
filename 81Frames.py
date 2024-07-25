# 81. Frames [08:15:33]------------------------------------------------
from tkinter import *
window = Tk()
window.geometry("600x420")
# button = Button(window,text="W",font=("Consolas",25),width=3)
# button.pack()
frame=Frame(window,bg="pink",bd=5,relief=SUNKEN)
# frame.pack()
frame.place(x=100,y=100)
Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)


window.mainloop()