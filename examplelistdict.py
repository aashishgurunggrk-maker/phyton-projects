my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

for i in range(len(my_list)):
    print(my_list[i])
print("-------------------")
for i in my_list:
    print(i)
print("-------------------")
# use loop both for and for each 
# make use of len() function to know the length of the list

my_dict = {"math":70, "science" : 67.5, "social" : 78}

for x in my_dict:
    print(x, my_dict[x])
print("-------------------")

for x in my_dict.values():
    print(x)
print("-------------------")

for x in  my_dict.keys():
    print(x)
print("-------------------")

for x, y in my_dict.items():
    print(x,y)

# use for each 
# use .values(), .keys(), .items() and print the answers