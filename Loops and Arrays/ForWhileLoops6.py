# WAP to filter even and odd number form a list
x = [10,23,24,35,65,78,90]
eve = []
odd = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        eve.append(x[i])
    else:
        odd.append(x[i])
print("Even numbers are: ",eve)
print("Odd numbers are: ",odd)

# output
# Even numbers are:  [10, 24, 78, 90]
# Odd numbers are:  [23, 35, 65]