#Factorial of a number
n = int(input("Enter number: ")) # 5
if(n == 0 or n < 0):
    print("Value of n should be greater than 1")
else:
    fact = 1
    while(n):
        fact *= n
        n = n-1
    print(f"Factorial is {fact} ")
# output
# Factorial is 120