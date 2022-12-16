num = int(input("Enter an integer 3 digits only!"))

x = num
y = num
list1 = []
list2 = []

i = 0
while y>=1:
    y = int(y/10)
    i+=1
y = i

if(num>=0 and num<=1000):
    i=0
    while(i<y):
        z = x % 10
        x = int(x/10)
        list1.append(z)

        i+=1
    i=y-1
    while(i>=0):
        if(list1[i]==0):
            list2.append("zero")
        elif (list1[i] == 1):
            list2.append("one")
        elif (list1[i] == 2):
            list2.append("two")
        elif (list1[i] == 3):
            list2.append("three")
        elif (list1[i] == 4):
            list2.append("four")
        elif (list1[i] == 5):
            list2.append("five")
        elif (list1[i] == 6):
            list2.append("six")
        elif (list1[i] == 7):
            list2.append("seven")
        elif (list1[i] == 8):
            list2.append("eight")
        elif (list1[i] == 9):
            list2.append("nine")
        i-=1

    for j in range(y):
        print(list2[j],end="")
else:
    print("Invalid input!")
