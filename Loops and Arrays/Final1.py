#1
Students = ["S1","S2","S3","S4","S5"]
Grades = [90,75,81,89,95]

for i in range(len(Students) and len(Grades)):
    print(Students[i],Grades[i])
print("\n")
#Output:
# S1 90
# S2 75
# S3 81
# S4 89
# S5 95

#2
score = [75,76,77,78,79]
names = ["a","b","c","d","e"]
for loop in range(5):
    print(names[loop],score[loop])
# a 75
# b 76
# c 77
# d 78
# e 79