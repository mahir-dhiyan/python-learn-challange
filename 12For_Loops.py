import time
for i in range(10,-1,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!")
sum=0
for i in range(1,101,1):
    sum=sum+i
print("The Sum of first 100 is "+ str(sum))