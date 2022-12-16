#Program to separate +ve and -ve
x = [23,4,-6,23,-9,21,3,-45,-8]
pos = []
neg = []
for i in range(len(x)):
    if x[i] < 0:
        neg.append(x[i])
    else:
        pos.append(x[i])
print("Positive numbers are: ",pos)
print("Negative numbers are: ",neg)

# output
# Positive numbers are:  [23, 4, 23, 21, 3]
# Negative numbers are:  [-6, -9, -45, -8]