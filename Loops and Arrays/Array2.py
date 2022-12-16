name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
gender = str(input("Enter your gender: "))

Drinks = ["Coke","Tandauay","Sprite","RedHorse","JuicyLemon","Empirador"]

if(gender == "Male" or gender == "male"):
    if(age >= 18):
        print("You are now an adult you can drink",Drinks)
    else:
        print("You are now an adult you can drink"+Drinks[0],Drinks[2],Drinks[4])
elif(gender == "Female" or gender == "female"):
    if(age >= 18):
        print("You are now an adult you can drink"+Drinks)
    else:
        print("You are now an adult you can drink" + Drinks[0],Drinks[2],Drinks[4])




