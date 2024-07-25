# 88. Mouse Events [09:06:00]-------------------------------------------------------------
from tkinter import *
def bro(event):
    print("You have pressed"+str(event.x)+","+str(event.y))
    # print("You pressed something")
window=Tk()
# window.bind("<Button-1>",bro)
# window.bind("<Button-2>",bro)
# window.bind("<Button-3>",bro)
# window.bind("<ButtonRelease>",bro)
# window.bind("<Leave>",bro)
# window.bind("<Enter>",bro)
window.bind("<Motion>",bro)


window.mainloop()