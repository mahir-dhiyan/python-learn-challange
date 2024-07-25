# 56. Map function [04:53:30]----------------------------------------------
# map() = applies a function to each item in an iterable (list,tuple, etc)

store = [
    ("Shirts",20.00),
    ("Pants",25.00),
    ("Jackets",50.00),
    ("Socks",10.00)
]
to_euros = lambda data: (data[0],data[1]*0.872)
store_euros = list(map(to_euros,store))
print(store_euros)
for i in store_euros: 
    print(i)