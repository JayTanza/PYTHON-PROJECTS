grade = int(input("Enter a Grade: "))

if grade >= 90:
    print("A grade")
    if grade >= 90 and grade <= 99:
        print("Very intellegent!")
    else:
        print("Higly intellegent!")
elif grade >= 80:
    print("B grade")

elif grade >= 70:
    print("C grade")

elif grade >= 65:
    print("D grade")

else:
    print("Failing grade")
