# 53. Higher Order Function [ 04:35:30]---------------------------------------------
# 1. Accepts function as an argument
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):   #This is a higher order function 
    text=func("Hello")
    print(text)

hello(loud)
hello(quiet)

# 2. Higher order function returns a function

def divisor(x):
    def dividend(y):
        return y/x
    return dividend
divide = divisor(2)
print(divide(10))