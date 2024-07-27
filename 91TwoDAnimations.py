# 91. Simple 2D animations in python[09:29:25]------------------------------
from tkinter import *
import time
from PIL import Image,ImageTk
WIDTH=500
HEIGHT=500
xVelocity=3
yVelocity=2
window=Tk()

canvas=Canvas(window,width=WIDTH,height=HEIGHT, bg="black")
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('space.png').resize((500,500),Image.LANCZOS))
background=canvas.create_image(0,0,image=background_image,anchor=NW)

photo_image = ImageTk.PhotoImage(Image.open('ufo.png').resize((100,100),Image.LANCZOS))
my_image=canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height=photo_image.height()
while True: 
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0:
        xVelocity= -xVelocity
    if coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0:
        yVelocity= -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()