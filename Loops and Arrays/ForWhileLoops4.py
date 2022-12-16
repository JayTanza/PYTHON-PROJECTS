#Appending square to a new list
x = [2,3,4,5,6,7,8]
z = []
for i in range(len(x)):
    z.append(x[i]**2)
print("Result: ",z)

# output
# Result:  [4, 9, 16, 25, 36, 49, 64]