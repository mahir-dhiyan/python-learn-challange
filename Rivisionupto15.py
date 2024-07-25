#human=False
#print(human)
#print(type(human))
#name=input("What is  my name?: ")
#age=int(input("What is your age?: "))
#age+=1
#print("Your age will be: "+str(age)+" next year.")
#name= "Bro Code"
#first_name=name[4:8]
#print(first_name)
#another= name[0:8:2]
#print(another)
#name=""
#while len(name)==0:
 #   name=input("Enter your name: ")
#print("Hello "+name)
#sum=0
#for i in range(1,101):
 #   sum=sum+i
#print(sum)
phone_number= "0171122-6335"
for i in phone_number:
    if i=="-":
        continue
    print(i, end="")