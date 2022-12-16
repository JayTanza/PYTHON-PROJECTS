#Arrays
lang1 = "Python"
lang2 = "Java"
lang3 = "C#"
lang4 = "Javascript"

languages = [lang1,lang2,lang3]
languages.append(lang4)
languages.pop(0)

for x in languages:
    print(x)

if "Python" in languages:
    print("Best Language!")
