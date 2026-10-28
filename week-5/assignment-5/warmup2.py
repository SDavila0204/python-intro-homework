while True:
    user_input = input("Please enter a positive number: ")
    try:
        num = int(user_input)
        #if the number is greater than 0, it's good
        if num > 0:
            print("Thank you")
            #if it inputs this, it will break and stop the loop
            break
        else:
            #if the number is not positive
            print("That is not positive :( try again.")
    #if there is a value that is not a number, it will print this out
    except ValueError:
        print("This is not a valid input. Please try again.")
