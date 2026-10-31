for j in range(0, 31):
    #if number is divisible by 3 or 5
    if j % 3 == 0 and j % 5 == 0:
        print("FizzBuzz")
    #if it divisible by 3
    elif j % 3 == 0:
        print("Fizz")
    #if it is divisible by 5
    elif j % 5 == 0:
        print("Buzz")
    else:
    #if none of those, just prints out the number
        print(j)
