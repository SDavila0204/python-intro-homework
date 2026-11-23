#file path that computer will try to pull info from (doesn't actually exist)
filePath = "../data/missing.txt"

try:
	#will attempt to read the file and print out its contents
	with open(filePath, "r") as file:
		fileContent = file.read()
		print(fileContent)
except FileNotFoundError:
	#will print this out if it cannot find the file path
	print(f"ERROR. File not found at {filePath}. Try again later.")
