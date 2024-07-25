# 69. Buttons[06:24:32]-----------------------------------------------------------------
from tkinter import *
window = Tk()
photo = PhotoImage(file='logo.png')
count = 0
def click():
    global count
    count+=1
    print("You clicked the button~! ",count," times")
button=Button(window,
              text=('Click Me!!!'),
              font=("Comic Sans",30,"bold","italic"),
              command=click,
              fg="#00FF00",
              bg="black",
              activeforeground="#00FF00",
              activebackground="black",
              state="active",
              image=photo,
              compound="bottom"
              )
button.pack()
window.mainloop()