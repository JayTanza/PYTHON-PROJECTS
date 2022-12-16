num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation: ")

if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
    result = num1 / num2
    print(result)
else:
    print("You input Wrong Operation!")