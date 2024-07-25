temp = int(input("What is the temperature today? "))
if temp>=0 and temp <=30:
    print("The temperature is good!")
    print("Go outside")
elif temp < 0 or temp > 30:
    print("The temperature is bad!")
    print("Stay inside")