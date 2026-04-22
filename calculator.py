num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
result = 0 
operator = input("enter the operator")

if operator == "+":
   result = num1 + num2
   print(result)

if operator == "-":
    result = num1 - num2
    print(result)

if operator == "*":
    result = num1 * num2
    print(result)

if operator == "/":
    result = num1 / num2
    print(result)