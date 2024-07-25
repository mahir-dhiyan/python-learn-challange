# 73. Sliding Scale [07:00:55]------------------------------------------------------
from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+" degree C")
window = Tk()
# firePhoto=PhotoImage(file="fire.png")
# fireLabel=Label(image=firePhoto)
# fireLabel.pack()

scale= Scale(window, from_=100,to=0,
             length=600,
             orient=VERTICAL,
             font=("Consolas",20),
             tickinterval=10,
            #  showvalue=0,
            resolution=5, #increment of slider
            troughcolor='#69EAFF',
            fg="#FF1C00",
            bg='black'
             )
# scale.set(69)
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()
# coolPhoto=PhotoImage(file="cool.png")
# coolLabel=Label(image=coolPhoto)
# coolLabel.pack()
button = Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()