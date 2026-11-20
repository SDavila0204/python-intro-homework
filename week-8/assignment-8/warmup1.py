while True:
	#asks user to enter number
	userInput = input("Please enter a valid number: ")
	try:	
		#initializes number and determines whether it is valid
		num = float(userInput)
		print(f"You entered {num}. This is a valid number")
		#Will break sequence if correct answer is given
		break
	except ValueError:
		#will print out if incorrect result is given and continue asking until correct choice is given
		print("that's not a valid number! Please try again")
