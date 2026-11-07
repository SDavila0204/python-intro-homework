#defining minimum
def find_min(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    #loop to find minimum
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

#defining maximum
def find_max(numbers):
    #if value not a number, will return none
    if not numbers:
        return None
    max_val = numbers[0]
    #loop to find maximum
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


def bubble_sort(numbers):
    arrange = list(numbers)
    n = len(arrange)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arrange[j] > arrange[j + 1]:
                arrange[j], arrange[j + 1] = arrange[j + 1], arrange[j]
    return arrange

#continously shows menu
def show_menu():
    print("\n=== number cruncher ===")
    print("1. Minimum Value")
    print("2. Maximum Value")
    print("3. Search for specific number")
    print("4. Sorted List")
    print("5. Exit")
    return input("Enter your choice (between 1 and 5): ")


def main():
    # Numbers list definition
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

    while True:
        #shows the menu on command line
        choice = show_menu()
	
	#when you give a number, it will correspond to the numbers on the menu
        if choice == '1':
            print(f"The minimum value is {find_min(numbers)}")
        elif choice == '2':
            print(f"The maximum value is {find_max(numbers)}")
        elif choice == '3':
            try:
                target = int(input("Enter a number from the list, please: "))
                index = search(numbers, target)
                if index != -1:
                    print(f"Found at index {index}")
                else:
                    print("Index not found ")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == '4':
            sorted_list = bubble_sort(numbers)
            print(f"Sorted list: {sorted_list}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
