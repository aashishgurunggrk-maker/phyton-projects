todo_dict ={} #this is a variable of type dict thats goning to store the todo
time = ""
todo = ""
for i in range(1,8,2):
    time = input("enter the time")
    todo = input("enter the task")
    todo_dict[time]= todo
print(todo_dict)

for x,y in todo_dict.items():
    print(x,y)
