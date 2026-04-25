fruits = ["Apple", "Banana", "Mango"]
print("Without loop")
print(fruits[0])
print(fruits[1])
print(fruits[2])

print("--------------------------")
print("For loop using range")
for i in range(3):
    print(fruits[i])

print("--------------------------")
print("for each loop")
for fruit in fruits:
    print(fruit)
print("--------------------------")


student = ["asshih", 10, 75.6, True]

for i in range(len(student)):
    print(student[i])
print("--------------------------")


for item in student:
    print(item)

print("--------------------------")
