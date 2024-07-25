# 55. Sort Iterable is python [ 04:45:55]-----------------------------------------------------

# sort() method = used with lists
# sort() function = used with iterables

# students = ['Mahir', 'Shajid', 'Efty', 'Sami', 'Sadman']
# students.sort()
# # students.sort(reverse=True)
# for i in students: 
#     print(i)

# students2=('Mahir', 'Shajid', 'Efty', 'Sami', 'Sadman')
# sorted_students = sorted(students2,reverse=True)
# for i in sorted_students:
#     print(i)

# students = [
#     ("Squidward","F",60),
#     ("Sandy","A",33),
#     ("Patric","D",36),
#     ("Spongebob","B",20),
#     ("Mr. Krabs","C",78)

# ]
# grade = lambda grades:grades[1]
# students.sort(key=grade,reverse=True)
# for i in students:
#     print(i)

students1 = (
    ("Squidward","F",60),
    ("Sandy","A",33),
    ("Patric","D",36),
    ("Spongebob","B",20),
    ("Mr. Krabs","C",78)

)
age= lambda ages:ages[2]
sorted_students = sorted(students1,key=age,reverse=True)
for i in sorted_students:
    print(i)