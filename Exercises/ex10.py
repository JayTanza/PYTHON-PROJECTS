# Implement Python Switch Case Statement using Dictionary

def monday():
    return "Monday"
def tuesday():
    return "Tuesday"
def wednesday():
    return "Wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print(switch(num1))
print(switch(num2))