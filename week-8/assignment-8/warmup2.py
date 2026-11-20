num1 = float(input("please enter a number: "))
num2 = float(input("please enter another number: "))

try:
	answer = num1/num2
	print(f"result: {answer:.1}")
except ZeroDivisionError:
	print("you can't divide a number by zero. Please try again")
