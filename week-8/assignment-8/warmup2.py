#initializes both numbers and asks for user input
num1 = float(input("please enter a number: "))
num2 = float(input("please enter another number: "))

try:
	#does the division of the numbers
	answer = num1/num2
	#prints out result (only a decimal) if not zero
	print(f"result: {answer:.2}")
except ZeroDivisionError:
	#will print out if user tries to divide by zero
	print("you can't divide a number by zero. Please try again")
