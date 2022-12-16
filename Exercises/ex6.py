#Exercise 6: If else statement
#hourly rate for hours worked above 40 hours
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

try:
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error pls enter numeric input!")
    quit()
if hours > 40 :
    #logic part
    pay = (hours - 40)*rate*1.5+40*rate
else:
    pay = hours * rate

print("Pay: ",pay)

#Nested-if
if(hours > 50):
    print("above 50")
    if(hours > 100):
        print("also above 100")
    else:
        print("also below 100")
else:
    print("Below 50")