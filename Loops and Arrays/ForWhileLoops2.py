#WAP to reverse a string
str = input("Input a word to reverse: ")

for i in range(len(str) - 1, -1, -1):
  print(str[i], end="")
print("\n")

# output
# nohtype