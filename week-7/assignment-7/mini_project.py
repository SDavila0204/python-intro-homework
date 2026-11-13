import csv
import os
from datetime import date

dataExpenses = "../data/expenses.csv"
foodReport = "food_report.txt"

#verifies that Expenses exists
if not os.path.exists(dataExpenses):
	print(f"Error!! The file {dataExpenses} was not found")
	exit()

foodExpenses = []

#reads csv file
with open(dataExpenses, mode='r', encoding='utf-8') as file:
	reader = csv.DictReader(file)
	#filters list down to 'food'
	for row in reader:
		if row['category'].strip == 'Food':
			#converts amount into float
			row['Amount'] = float(row['amount'])
			foodExpenses.append(row)
			totalFood += row['amount']

#gets today's date
todayDate = date.today().strftime('%B%d, %Y')

totalFood = 0.0

#writes the report
with open(foodReport, 'w', encoding='utf-8') as report:
	report.write(f"Food Expense Report:")

	for expense in foodExpenses:
		report.write(f"{expense['date']}: {expense['amount']:.2f}\n")
	report.write(f"Total: {totalFood:.2f}\n")

#prints out actual report
print(f"Report has been written to {foodReport}")
