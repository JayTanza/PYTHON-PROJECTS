#1 - Index Count starts from 0
animals = ["Cat","Dog","Bird"]
numbers = [1,2,3]

index1 = animals.index("Cat")
index2 = numbers.index(2)

print(index1)
print(index2)

#2 - Append

animals.append("Tiger")
numbers.append(4)

print(animals)
print(numbers)

#3 - Extended

animals.extend(numbers)
print(animals)