filePath = "../data/missing.txt"

try:
	with open(filePath, "r") as file:
		fileContent = file.read()
		print(fileContent)
except FileNotFoundError:
	print(f"ERROR. File not found at {filePath}. Try again later.")
