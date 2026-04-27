answer = {
    "1": ["What is my name" , "Dol", ["Aashish","Anish","Dol","bisul"] ], 
    "2" : ["What is the capital of Nepal" , "Kathmandu" , ["Gorkha","Pokhara","Mustang","Kathmandu"]], 
    "3" : ["What is the national animal of Nepal" , "Cow" , ["Tiger","Dog","Cat","Cow"]], 
    "4": ["What is the national color of Nepal" , "Crimson" , ["Blue","Red","Green","Crimson"]], 
    "5": ["How many district are there in Nepal" , "77" , ["11","22","33","77"]]
    }

result = []

# print(answer["1"][0])
# print("Question " + answer["1"][0] + "? " + "Answer " + answer["1"][1])
for i in range(1,6):
    print(answer[str(i)][0]+ "?")
    for item in answer[str(i)][2]:
        print(item, end=' ')
    print()
    ans = input("Type your answer ")
    if answer[str(i)][1].lower() == ans.lower(): # Case insensitive 
        result.append("Right")
    else:
        result.append("Wrong")


# printing the result
for item in result:
    print(item)