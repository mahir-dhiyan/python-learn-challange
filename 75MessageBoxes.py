# 75. Message Boxes in python [ 07:24:50]------------------------------------------
from tkinter import *
from tkinter import messagebox
def click():
    # messagebox.showinfo(title="This is an info message box", message="You are a person")
    # while True:
    # messagebox.showwarning(title="WARNING!!!",message="You have a virus")
    # messagebox.showerror(title="Error!!!",message="Something went very wrong")
    # if messagebox.askokcancel(title="Ask ok cancel",message="Do you want to do this thing?"):
    #     print("You did something")
    # else: 
    #     print("You did nothing")
    # if messagebox.askretrycancel(title="Ask retry cancel",message="Do you want to retry this thing?"):
    #     print("You retried something")
    # else: 
    #     print("You canceled")
    # if messagebox.askyesno(title="ask yes or no",message="Do you like cake?"):
    #     print("I like cake too")
    # else: 
    #     print("Why do you not like cake?")
    # answer = messagebox.askquestion(title="ask question",message="Do you like pie?")
    # if answer=="yes":
    #     print("I like pie too")
    # else: 
    #     print("Why don't you like pie?")
    answer=messagebox.askyesnocancel(title="Yes no and cancel",message="Do you like to code?",icon='error')
    if(answer==True):
        print("You like to code :)")
    elif(answer==False):
        print("Then why are you watching a video on coding?")
    else: 
        print("You dodged the question. ")
window = Tk()

button = Button(window,text="Click Me",command=click)
button.pack()


window.mainloop()