student = {"name": "Aashsish", "rollno": 36, "percentage" : 70.5, "result" : True}
print(student)
print(type(student))
print(student["name"])
print(type(student["name"]))
print(student["rollno"])
print(type(student["rollno"]))
print(student["percentage"])
print(type(student["percentage"]))
print(student["result"])
print(type(student["result"]))

# for i in range(4):
#     print(student[i])

for x in student:
    print(x)
    print(student[x])


for x in student.values():
    print(x)


for x, y in student.items():
    print(x , y)