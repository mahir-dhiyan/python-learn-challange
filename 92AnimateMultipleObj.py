# 92. Animate multiple objects in python[09:41:42]-------------------------------------
from tkinter import *
from Ball import *
import time
from PIL import Image, ImageTk
window =Tk()

WIDTH=500
HEIGHT=500
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball=Ball(canvas,0,0,100,4,2,"white")
tennis_Ball=Ball(canvas,0,0,50,5,3,"yellow")
basket_ball=Ball(canvas,0,0,125,2,1,"orange")


while True:
    volley_ball.move()
    tennis_Ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()