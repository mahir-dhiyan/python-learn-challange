age=int(input("How old are you?: "))
if age >= 18:
    print("You're an adult")
elif age <=0:
    print("You haven't been born yet")
elif age==100: 
    print("You are a century old!")
else:
    print("You're a child")