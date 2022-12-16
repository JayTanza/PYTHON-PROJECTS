def default():
    return "Incorrect input!"

def calculator(x,a,b):
    switcher = {
        1: (a + b),
        2: (a - b),
        3: (a * b),
        4: (a / b)
    }
    print(switcher.get(x, default()))
print("             Simple Calculator")
print("      1. Addition")
print("      2. Substraction")
print("      3. Multiplication")
print("      4. Division")
x = input("Please enter your action: ")
a = input("Please enter your number: ")
b = input("Please enter your number: ")

calculator(int(x), int(a), int(b))

while (10 >= 0):
    print("             Simple Calculator")
    print("      1. Addition")
    print("      2. Substraction")
    print("      3. Multiplication")
    print("      4. Division")
    x = input("Please enter your action: ")
    i = input("Please enter your number: ")
    j = input("Please enter your number: ")
    calculator(int(x), int(i), int(j))