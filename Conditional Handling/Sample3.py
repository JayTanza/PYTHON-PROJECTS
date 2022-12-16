num = int(input("Enter a 3 digit number: "))

if num >= 100 and num <= 1000:
    if num == 111 or num == 222 or num == 333 or num == 444 or num == 555 or num == 666 or num == 777 or num == 888 or num == 999:
        print("Bingo! You win!")
    else:
        print("You lose! Try again!")
else:
    print(num,"is not a 3 digit number!")