# 61. Zip Function [05:19:10]-------------------------------------------------------------
# zip(multiple iterables) = aggregate elements from two or more iterables (list, tuples,sets etc.)
# creates a zip object with paired elements stored in tuples for each elements
usernames = ["Dude","Bro","Mister"]
passwords = ("P@ssword","abc123","Gue$1")
login_date=["1/1/2024","1/2/2024", "1/3/2024"]
users= list(zip(usernames,passwords))
print(type(users))
for i in users: 
    print(i)
users = dict(zip(usernames,passwords))
print(type(users))
print(users)
for key,values in users.items():
    print("Key: "+key+" Values: "+values)
# ----------------
users = zip(usernames,passwords,login_date)
for i in users: 
    print(i)