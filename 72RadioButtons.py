# 72. Radio Button in python[06:49:16]----------------------------------------------
from tkinter import *
food=["Pizza","Burger","Nachos","Meatbox"]
def order():
    if(x.get()==0):
        print("You ordered Pizza")
    elif(x.get()==1):
        print("You ordered Burger")
    elif(x.get()==2):
        print("You ordered Nachos")
    else:
        print("You orderd Meatbox")
window = Tk()
# pizza = PhotoImage(file="pizza.png")
# burger = PhotoImage(file="burger.png")
# nachos = PhotoImage(file="nachos.png")
# meatbox = PhotoImage(file="meatbox.png")

# food_images=[pizza,burger,nachos,meatbox]

x=IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x, #This groups raiobuttons together if they share the same variable
                              value=index,#assigns each radiobutton a different value
                              padx=25,
                              font=("Impact",50),
                            #   image=food_images[index],  
                              indicatoron=0,
                              width=30,
                              command=order, 
                            #   compound="left"               
                              )
    radiobutton.pack(anchor=W)

window.mainloop()