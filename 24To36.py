# # 24. Nested Function Calls[2:07:15]-------------------------------------------------------------
# # print('Hellow world')
# print(round(abs(float((input('Enter a whole number: '))))))


# # 25. Variable Scope[2:09:50]---------------------------------------------------------------
# name='Dhiyan'
# def display_name(): 
#     name="Code"
#     print(name)
# display_name()
# print(name)


# # 26. Args parameter[2:13:31]------------------------------------------------------------------

# def add(*args):
#     sum=0
#     args = list(args)
#     args[0]=6
#     for i in args: 
#         sum+=i
#     return sum
# print(add(1,2,3,4,5))


# # 27. Kwargs [2:17:05]----------------------------------------------------------------------

# def hellow(**kwargs):
#     # print('Hellow '+kwargs['first']+" "+kwargs['last'])
#     print('Hellow',end=" ")
#     for key,values in kwargs.items(): 
#         print(values,end=" ")
# hellow(title="Mr", first="Mahir", middle="Dhiyan", last="Chowdhury")


# # 28. Formate Method[02:21:25]----------------------------------------------------------------------
# animal ="Cow"
# item="Moon"
# # print("The {} jumped over the {}".format(animal,item))
# #  #Positional Arguments
# # print("The {0} jumped over the {1}".format(animal,item))
# # #Keyword Arguments
# # print("The {animal} jumped over the {item}".format(animal="Cow",item="Moon")) 
# # print("The {item} jumped over the {animal} and {item} is very cool".format(animal="Cow",item="Moon")) 
# text="The {} jumped over the {}"
# print(text.format(animal,item))
# name="Dhiyan"
# print("Hellow my name is {:10}. Nice to meet you".format(name))
# print("Hellow my name is {0:10}. Nice to meet you".format(name))
# print("Hellow my name is {name:10}. Nice to meet you".format(name="Mahir"))
# print("Hellow my name is {:<10}. Nice to meet you".format(name))
# print("Hellow my name is {:>10}. Nice to meet you".format(name))
# print("Hellow my name is {:^10}. Nice to meet you".format(name))

# # Number format

# pi=3.1415789
# number=1000000
# print("The pi is {}".format(pi))
# print("The pi is {:.3f}".format(pi))
# print('The number is {:,}'.format(number))
# print('The number is {:b}'.format(number)) #binary
# print('The number is {:o}'.format(number)) #octal
# print('The number is {:x}'.format(number)) #hexadecimal
# print('The number is {:X}'.format(number)) #hexadecimal
# print('The number is {:e}'.format(number)) #scientific
# print('The number is {:E}'.format(number)) #scientific

# # 29. Random Module[02:33:30]-------------------------------------------------------------------

# import random
# x=random.randint(1,6)
# y=random.random()
# myList=['Rock','Paper','Scissors']
# z=random.choice(myList)
# cards=[1,2,3,4,5,6,7,8,9,"j","q","k","a"]
# random.shuffle(cards)
# print(x)
# print(y)
# print(z)
# print(cards)


# # 30. Exception Handling[02:36:50]-------------------------------------------------


# try:
#     numerator=int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divided by: "))
#     result = numerator/denominator
   
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't devide by zero you idiot")
# except ValueError as e: 
#     print(e)
#     print("Please only provide interger numbers ")
# except Exception as e: 
#     print(e)
#     print('Something went wrong :( ')
# else: 
#      print(result)
# finally: 
#     print("This block of code will always execute")


# # 31. Basic file detection[02:43:51]----------------------------------------------------

# import os
# path="E:\\BorCodePython\\.vscode\\fileManipulation\\folder"
# if os.path.exists(path):
#     print('This location exists')
#     if os.path.isfile(path):
#         print('This is a file')
#     elif os.path.isdir(path):
#         print("This is a directory")
# else: 
#     print("This location doesn't exist")

# # 32. Reading a file[02:47:35]----------------------------------------------------

# try:
#     with open('fileManipulation\\test.tx') as file: #Instead of .txt I wrote .tx
#         print(file.read())
# # print(file.closed)
# except FileNotFoundError: 
#     print("File was not found :(")

# # 33. Writing and appending files[02:51:10]---------------------------------------------------------

# text="Yoooo!\n Wassup bros. This is\n Mahir Dhiyan\n in the house.\nThis Text has been overwritten\n"
# with open("fileManipulation\\test.txt","w") as file:
#     file.write(text)
# # textAppend="This line is appended"
# # with open("fileManipulation\\test.txt","a") as file:
# #     file.write(textAppend)

# # 34. Copying Files[02:53:55]  ------------------------------------------------

# import shutil
# shutil.copyfile("fileManipulation\\copyThis.txt","fileManipulation\\folder\\copy.txt")
# #copy() = copyfile() + permission mode + destination can be a directory
# #copy2() = copy() ++ copies metadata (files's creation and modification times)

# # 35. Moving files [02:57:15]------------------------------------------------------------------

# import os
# source="fileManipulation\\folderMove"
# destination = "fileManipulation\\folder\\folderMove"
# # source="fileManipulation\\move.txt"
# # destination = "fileManipulation\\folder\\move.txt"
# try: 
#     if os.path.exists(destination):
#         print("There is already a file there.")
#     else: 
#         os.replace(source,destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+ " was not found")
# except Exception: 
#     print("Something went wrong")

# 36. Deleting Files [03:01:30]---------------------------------------------------------

import os
import shutil
path="fileManipulation\\delete.txt"
try: 
    os.remove(path)
except FileNotFoundError:
    print("This file was not found")
path="fileManipulation\\not_emptyFolder"
# path="fileManipulation\\empty_folder"
try: 
    # os.remove(path)   #Remove a file
    # os.rmdir(path)    #Remove an empty directory
    shutil.rmtree(path)  #Remove a directory containing files
    
except FileNotFoundError: 
    print("Folder Was not found")
except PermissionError: 
    print("You don't have permission to delete this")
except OSError: 
    print("You can't delete that using that function")
else: 
    print(path+" was deleted")