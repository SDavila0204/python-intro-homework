# A student record
studentInfo = {
    "name": "Carlos",
    "grade": "A",
    "subject": 95
}

for student, info in studentInfo.items():
    print(f"Student info: {student}: {info}")

studentInfo["Graduated"] = False

print()
for student, info in studentInfo.items():
    print(f"Student info: {student}: {info}")
