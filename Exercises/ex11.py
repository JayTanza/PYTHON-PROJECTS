try:
    num1 = int(input("Enter a number: "))
except:
    print("Error pls enter numeric input!")
    quit()

if(num1==0):
    print(num1,"a zero number!")
elif(num1>0):
    if(num1%2==0):
        print(num1,"is an positive even number!")
    else:
        print(num1, "is an positive odd number!")
elif(num1<0):
    if(num1%2==0):
        print(num1,"is an negative odd number!")
    else:
        print(num1, "is an negative even number!")
