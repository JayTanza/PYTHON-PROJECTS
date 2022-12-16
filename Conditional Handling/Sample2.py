
num = int(input("Enter an integer: "))

if(num>0 and num!=0):
    if(num%2==0):
        print(num,"is an positive even number!")
    else:
        print(num, "is an positive odd number!")
elif(num<0 and num!=0):
    if (num % 2 == 0):
        print(num, "is an negative even number!")
    else:
        print(num, "is an negative odd number!")
else:
    print(num,"is an zero number!")