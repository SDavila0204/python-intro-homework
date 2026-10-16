number =int(input("input a number: "))

#checks if number is pos or neg
if number < 0:
    print(f"{number} is a negative number")
elif number > 0:
    print(f"{number} is a positive number")

#checks if number is odd or even
if number % 2:
    print (f"{number} is odd")
elif number == 0:
    print("0 is neither positive nor negative.")
else:
    print(f"{number} is even")
