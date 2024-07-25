
# #2Variable [5:57]-------------------------------------------------------------------

# name= "Bro"
# print("Hello "+name)
# print(type(name))
# #int--
# age = 21
# age+=1
# print(age)
# print(type(age))
# print('Your age is: ' + str(age))
# #float--
# height = 250.5
# print(height)
# print('Type of height variable' +str(type(height)))
# #Boolean--
# human = True
# doggy_league = False
# print(type(human))
# print(human)
# print(doggy_league)


# #3.Multiple Assignment[17:53]----------------------------------------------------------------------------------------
# name,age,attractive= 'Dhiyan',23,True
# print(name,age,attractive)

# #4.String Methods[20:40]----------------------------------------------------------------------
# name='Dhiyan'
# print(len(name))
# print(name.find('y'))
# print(name.find('d'))
# print(name.find('D'))
# print(name.find('H'))
# print(name.find("N")) 
# cap_name = 'mahir dhiyan'
# print(cap_name.capitalize())
# print(cap_name.isdigit())
# print(cap_name.isalpha())
# print('I am sorry\n'*103)



# #5.TypeCasting[25:15]----------------------------------------------------------------------------
# x=1
# y=2.9
# z='7'
# print(int(y))
# print(y)
# print(type(int(y)))
# print(z*3)
# print(y*3)

# # 6.User Input [30:25]------------------------------------------------------------------------------------------------
# name=input('What is your name motherBroer?: ')
# print('Hellow '+name+' You are a legend')
# age=int(input('How old are you?: '))
# age+=1
# print('No!! You are '+str(age)+ ' years old')
# # reply=input('Reply: ')
# # if reply== 'Thanks':
# #     print('You are welcome')
# # else:
# #     print('Bro you')
# # 7.Useful Function Related to number[37:00]-----------------------------------------------------------------------
# import math
# pi= -3.14
# print(round(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# #8.String slicing [41:09]---------------------------------------------------------------
# # These are with indexing
# name='mahir dhiyan'
# # first_name= name[0:5]
# # also can be written as 
# first_name=name[:5]
# print(first_name)
# # last_name=name[6:12]
# last_name=name[6:]
# print(last_name)
# even_name = name[::2]
# print(even_name)
# reverse_name = name[::-1]
# print(reverse_name)
# # These are with slicing
# website="http://google.com"
# website2="http://xTwitter.com"
# # print(website[7:-4])
# slice=slice(7,-4)
# print(website[slice])
# print(website2[slice])


# # 9.If statements else if statements[52:00]-----------------------------------------------------
# age= int(input('How old are you?: '))
# if age>=18:
#     print('you are an adult')
# elif age<0:
#     print('You havent been born yet')

# else:
#     print('you are a child')
# # 10.Logical operator [58:30]------------------------------------------------------------
# temp = int(input('what is the temperature outside?:  '))
# # if temp >= 0 and temp <= 30:
# #     print('The temperater is good today')
# #     print('go outside')
# # elif temp<0 or temp >30:
# #     print('The temperature is bad today')
# #     print('Stay inside')
# if not(temp >= 0 and temp <= 30):
#     print('The temperature is bad today')
#     print('Stay inside')
# elif not(temp<0 or temp >30):
#     print('The temperater is good today')
#     print('go outside')
    
# # 11.While Loop[1:4:13]------------------------------------------------------------
# name=input('Enter your name: ')
# while len(name)==0:
#     name = input("Hey! You didn't Enter your name? Enter your name please: ")

# print("Hellow! "+name+" Hope you are doing well")


# # 12. For loops [1:7:37]------------------------------------------------------
# # sum=0
# # n=int(input("Enter final number: "))

# # for i in range(1,n+1):
# #     # sum=sum+i
# #     # print(sum)
# #     # iteration = n-i
# #     print(' '*(n-i)+'* '*i)
# # # print('Final sum is: '+str(sum))

# # for i in "Mahir Dhiyan":
# #         print(i)
# import time
# for seconds in range(10,0,-1):
#         print(seconds)
#         time.sleep(1)

# print("Happy New Year!!")

# # 13.Nested Loop[1:13:05]-----------------------------------------------------------------

# rows=int(input("How many rows?: "))
# columns=int(input("How many columns?: "))
# symbol= input('What symbol do you wanna use?: ')
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end='')
#     print()

# # 14.Loop control statements [1:17:17]----------------------------------------------------
# while True: 
#     name=input('What is your name?: ')
#     if name!="":
#         break
# phone="017-11226-335"

# for i in phone: 
#     if i == "-":
#         continue
#     print(i,end="")
# print()
# for i in range(1,21):
#     if i == 13: 
#         pass
#     else:
#         print(i)

# # 15. Lists[1:21:10]--------------------------------------------------
# food=["Sushi","Burgir","Hotdog","Nachos"]
# food[0]="Pizza"

# for i in food: 
#     print(i)

# # Useful functions of lists
# food.append("Meatbox")
# # food.remove('Hotdog')
# # food.pop()
# food.insert(0,"Pringles")
# food.sort()
# # food.clear()
# print(food)


# # 16.2D Lists[1:27:00]----------------------------------------------------------

# dinner = ['Pizza','Burger','Nachos']
# drinks=['Coffee','Soda','Tea']
# desserts=['Cake','Ice Cream']
# food=[dinner,drinks,desserts]
# print(food[0][2])
# # 17. Tuples[1:30:55]------------------------------------------------------------------------------

# students = ('Bro',21,'Male')
# # students_list = ['Bro',21,'Male']
# print(students)
# for x in students: 
#     print(x)
# print('Number of time Bro is count '+str(students.count('Bro')))
# print(students[2])
# if 'Bror' in students:
#     print('Bro is here')
# # 18.Sets [ 1:33:58]--------------------------------------------------------------------------------------
# utensils = {'fork','spoon','knife'}
# dishes={'bowl','plate','cup','knife'}
# # utensils.update(dishes)
# dinner_table=utensils.union(dishes)
# # utensils.add('Napkin')
# # utensils.remove('fork')
# # utensils.clear()
# for x in dinner_table: 
#     print(x)
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
# # 19.Dictionaries[1:40:10]-----------------------------------------------------------------------------------------
# capitals={
#     'Germany':'Berlin',
#     'Usa': 'Washington DC',
#     'Ireland':'Dublin',
#     'UK': 'London',
#     'India': 'New Dehli'
# }
# # print(capitals)
# capitals.update({"India":"Mombay"})
# capitals.update({'Russia':'Moscow'})
# # print(capitals)
# # print(capitals['Germany'])
# # print(capitals.get('Ireland'))
# # print(capitals.get('china'))
# # for (key,values) in capitals: 
# # print(capitals.keys())
# # print(capitals.values())
# # print(capitals.items())
# capitals.pop('India')
# # capitals.clear()
# for keys,values in capitals.items(): 
#     print(keys,values)

# # 20.Indexing[1:47:30]-----------------------------------------------------------------
# name = 'mahir dhiyan'
# if name[0].islower(): 
#     name=name.capitalize()
# print(name)
# # 21. Fuctions[1:53:30]------------------------------------------------------------------------------

# def hello(first_name,last_name,age): 
#     print('Hellow from function!')
#     print('Have a nice day, '+first_name+" "+last_name)
#     print('You are '+str(age)+ " years old")
# hello('Mahir','Dhiyan',23)
# # 22.Return Statements[2:2:10]------------------------------------------------------------------
# def multiply(number1,number2): 
#     return number1*number2
# # print(multiply(6,9))
# x=multiply(6,9)
# print(x)
# # 23. Keyword arguments[2:05:00]--------------------------------------------------------
# def hello(first,middle,last):
#     print('Hellow '+first+" "+middle+" "+last)
# hello(middle='Dhiyan',last='Chowdhury',first='Mahir')