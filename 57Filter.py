# 57. Filter function [04:57:30]--------------------------------------------------------------
# filter() = creates a collection of elements from an iterable for which a function returns True

friends =[
    ("Rachel",19),
    ("Monica",18),
    ("Phoebe",17),
    ("Joey",16),
    ("Chandler",21),
    ("Ross",22)
]
age = lambda data:data[1]>=18
drinking_buddies = list(filter(age,friends))
print(drinking_buddies)
for i in drinking_buddies: 
    print(i)