num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))
num3 = int(input("Enter the third value: "))

if(num1>num2 and num1>num3):
    print("The Largest value is ",num1)
elif(num2>num1 and num2>num3):
    print("The Largest value is ",num2)
else:
    print("The Largest value is ",num3)

if(num1<num2 and num1<num3):
    print("The Smallest value is ",num1)
elif(num2<num1 and num2<num3):
    print("The Smallest value is ",num2)
else:
    print("The Smallest value is ",num3)