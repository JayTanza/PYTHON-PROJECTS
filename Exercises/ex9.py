def calculator(x, i, j):
    switcher={
              1 : (i + j),
              2 : (i - j),
              3 : (i * j),
              4 : (i / j),
              }

    print(switcher.get(x,"Wrong input"))
print("             Simple Calculator")
print("      1. Addition")
print("      2. Substraction")
print("      3. Multiplication")
print("      4. Division")
x = input("Please enter your action: ")
i = input("Please enter your number: ")
j = input("Please enter your number: ")
calculator(int(x), int(i), int(j))

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
