import os

#1. prints the working directory
print("Current Work Directory:", os.getcwd())

#3. builds path
target_path = os.path.join("..", "data", "expenses.csv")
print("Path: ", target_path)


#2. checks if path exists
if os.path.exists(target_path):
	print("expenses.csv found!")
else:
	print("expenses.csv not found")
