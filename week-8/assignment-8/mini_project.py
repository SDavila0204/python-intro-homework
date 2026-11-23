import csv

filePath = '../data/messy_data.csv'

#wrap file opening in try/except filenotfound
try:
	with open(filePath, mode='r', encoding= 'utf-8') as file:
		reader = csv.DictReader(file)
		#initializing things
		rowsAttempted = 0
		rowsParsed = 0
		rowsSkipped = 0
		
		#will be filled out later
		skippedRows = []
		cleanData = []
		
		#Goes through each row
		for rowNum, row in enumerate(reader, start=1):
			rowsAttempted += 1
			#Will skip rows
			if None in row:
				rowsSkipped += 1
				skippedRows.append(f"Row {rowNum} skipped")
				continue

			try: 	#the expected column from the file
				columnsExpected = ['name', 'category', 'amount']
				for c in columnsExpected:
					if c not in row:
						raise KeyError(c)

				name = row['name']
				category = row['category']
				amountStr = row['amount']
				#turns amount to float value
				amount = float(amountStr)
				
				#organizes clean data as such
				rowsParsed += 1
				cleanData.append({
					"name": name,
					"category": category,
					"amount": amount
				})

			#Will skip if there was a Value OR Key error and print it out
			except ValueError as e:
				rowsSkipped += 1

				valRep = repr(amountStr) if 'amountStr' in locals() else "''"
				skippedRows.append(f"Row {rowNum}: VallueError")

			except KeyError as e:
				rowsSkipped += 1
				skippedRows.append(f"Row {rowNum}: KeyError")

#prints this out if there was an error finding the file
except FileNotFoundError:
	print(f"Error: The file {filePath} not found")
	exit(1)

#printing out report
print("=== CSV Report ===")
print(f"Rows attempted:  {rowsAttempted}")
print(f"Rows parsed:      {rowsParsed}")
print(f"Rows skipped:     {rowsSkipped}")
print()
print("Skipped rows:")
for skipped in skippedRows:
    print(skipped)
print()
print("Clean data:")
for item in cleanData:
    print(item)
