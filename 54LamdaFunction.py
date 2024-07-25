# 54. Lamda function [04:41:14]--------------------------------------

# def double(x):
#     return x*2
# print(double(6))
double = lambda x: x*2
multiply=lambda x,y:x*y
add= lambda x,y,z: x+y+z
full_name= lambda first_name,last_name: first_name +" " + last_name
age_check = lambda age: True if age>=18 else False

print(age_check(22))

print(full_name("mahir","dhiyan"))

print(add(3,4,3))

print(multiply(3,9))

print(double(6))