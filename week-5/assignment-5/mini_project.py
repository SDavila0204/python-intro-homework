numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

#while conditions remain true, it will continue to show message
while True:
    print("=== number cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for specific number")
    print("4. Sort list")
    print("5. Quit")
    print()

    choose = input("Please choose one of the options above (1-5): ")

#finding minimum
    #if the user chooses '1'
    if choose == '1':
        if not numbers:
            print("try again.")
            continue

        #finds the minimum through the for loop
        mini = numbers[0]
        for num in numbers:
            #will go through list until it finds the smallest value
            if num < mini:
                mini = num
        print(f"minimum: {mini}")
        print()

#finding maximum
    #if the user chooses '2'
    elif choose == '2':
        if not numbers:
            print("try again.")
            continue

        maxi = numbers[0]
        for num in numbers:
            if num > maxi:
                maxi = num
        print(f"maximum: {maxi}")
        print()

#searching for a number
    elif choose == '3':
        if not numbers:
            print("try again.")
            continue

    #asks users to input an integer and if there is an error it asks them to try again
        try:
            val = int(input("Please enter an integer from list: "))
            print()
        except ValueError:
            print("Invalid. Please try again.")
            print()
            continue

    #loop to find searched for number and finds index
        foundNum = 0
        for i in range(len(numbers)):
            if numbers[i] == val:
                foundNum = i
                break

        if foundNum != 0:
            print(f"{val} found at index {foundNum}")
            print()
        else:
            print(f"{val} not found in the list :/")
            print()

#sorting out list
    elif choose == '4':
        if not numbers:
            print("try again.")
            continue

        arrange = list(numbers)
        j = len(arrange)
        numOrder = True

        while numOrder:
            numOrder = False
            for a in range(j - 1):
                if arrange[a] > arrange[a + 1]:
                    arrange[a], arrange[a + 1] = arrange[a + 1], arrange[a]
                    numOrder = True

        print(f"sorted list: {arrange}")
        print()

#Quit option
    elif choose == '5':
        print(" ⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹ Goodbye ⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹")
        print()
        break
    else:
        print("Error. Please enter number between 1 and 5.")
