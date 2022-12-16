try:
    grade = int(input("Enter Grade: "))
except:
    print("Error pls enter numeric input!")

if(grade < 0 or grade > 100):
    print("Grade is out of range!")
if(grade >= 90):
    print("You Pass!")
    if(grade >= 96):
        print("A+")
    elif(grade <= 94):
        print("A-")
elif(grade >= 80):
    print("You Pass!")
    if(grade >= 86):
        print("B+")
    elif(grade <= 84):
        print("B-")
elif(grade >= 70):
    print("You Pass!")
    if(grade >= 76):
        print("C+")
    elif(grade <= 74):
        print("C-")
elif(grade >= 60):
    print("You Fail!")
    if(grade >= 66):
        print("D+")
    elif(grade <= 64):
        print("D-")
elif(grade >= 50):
    print("You Fail!")
    if(grade >= 56):
        print("D+")
    elif(grade <= 54):
        print("D-")
elif(grade >= 40):
    print("You Fail!")
    if(grade >= 46):
        print("F+")
    elif(grade <= 44):
        print("F-")
else:
    print("Fail Grade!")

