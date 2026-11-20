while True:
	userInput = input("Please enter a valid number: ")
	try:
		num = float(userInput)
		print(f"You entered {num}. This is a valid number")
		break
	except ValueError:
		print("that's not a valid number! Please try again")
