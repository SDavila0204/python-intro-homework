nameList = ["Bruce", "Diana", "Clark", "Oliver", "John"]
enterName = input("Please enter a name: ")

#placeholders
List = False
index = 0

#Loop to find if name is in list
for i in range(len(nameList)):
    if nameList[i] == enterName:
        List = True
        index = i
        break

#If the name is on the list
if List:
    print(f"{enterName} was found at index {index}")
else:
    print(f"{enterName} was not found in list")
