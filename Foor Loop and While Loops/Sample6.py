while True:
    user_input = int(input("Enter an integer: "))
    if(user_input %2 != 0):
        print("This number is odd")
        break
    else:
        print("This number is even")
#Sample Sol. it will stop when the number is odd
# Enter an integer: 2
# This number is even
# Enter an integer: 3
# This number is odd