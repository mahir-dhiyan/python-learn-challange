# 58. Reduce Function [05:00:20]-------------------------------------------
# reduce() = apply a function to an iterable and reduce it to a single cumulative value. 
# Performs function of first two elements and
# repeats process until 1 value remain
import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y,letters)
print(word)
factorial =[5,4,3,2,1]
result=functools.reduce(lambda x,y:x*y,factorial)
print(result)