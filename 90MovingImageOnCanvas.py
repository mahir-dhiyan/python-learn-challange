# 90. Moving Image on Canvas [09:24:05]----------------------------------------------------
from tkinter import *
# Pillow for image resize
from PIL import Image,ImageTk
def move_up(event):
    canvas.move(carImage,0,-10)
def move_down(event):
        canvas.move(carImage,0,10)
def move_left(event):
    canvas.move(carImage,-10,0)

def move_right(event):
        canvas.move(carImage,10,0)

window=Tk()
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)
canvas = Canvas(window,width=500,height=500)
canvas.pack()
# pil_img=Image.open('car.png')
# resize_img=pil_img.resize((100,100),Image.LANCZOS)
# photoImage = ImageTk.PhotoImage(resize_img)

# Compressed Code for copy paste-------------------
photoImage= ImageTk.PhotoImage(Image.open('car.png').resize((100,100),Image.LANCZOS))
carImage = canvas.create_image(0,0,image=photoImage,anchor=NW)





window.mainloop()