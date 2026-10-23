#two lists with programming languages
listOne = ["Python", "Java", "C++", "HTML", "Ruby"]
listTwo = ["Python", "Java", "SQL", "Rust", "Javascript"]

#turning the lists into sets
setOne = set(listOne)
setTwo = set(listTwo)

#Union mixes both without including duplicates
union = setOne.union(setTwo)
print("Union:", union)

#Intersection shows only the languages in both lists
intersection = setOne.intersection(setTwo)
print("Intersection:", intersection)

#Difference shows languages only on the first list
difference = setOne.difference(setTwo)
print("Difference:", difference)
