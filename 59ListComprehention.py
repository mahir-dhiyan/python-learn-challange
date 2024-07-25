# 59. List Comprehention [ 05:05:05]-----------------------------------------------
# list comprehention= way to create new list with less syntax
#                       can mimic certain lambda functions, easier to read
# Formula: 
# list = [(expression) (for item in iterable) (if conditional)]
# list = [(expression) (if/else conditional) (for item in iterable)]
# Here the paranthesis or first bracket doesn't mean anything. Only for seperating the formula
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)
square=[i*i for i in range(1,11)]
print(square)

students = [100,90,80,70,60,50,40,30,0]
passed_students = list(filter(lambda x: x>=60,students))
print(passed_students)
passed_students1 = [i for i in students if  i>=60]
print(passed_students1)
passed_students2=[i if i>=60 else "Failed" for i in students]
print(passed_students2)