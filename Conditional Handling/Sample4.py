num = int(input("Enter an integer: "))

if(num>100 and num<1000):
    digit = num % 100
    num = num/10
    cdigit = num % 10
    if(cdigit != digit):
        print("You Lose!")
    else:
        print("Bingo! You Win!")
else:
    print(num,"is not a 3 digit number!")
