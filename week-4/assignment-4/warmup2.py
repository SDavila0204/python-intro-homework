# A student record
studentInfo = {
    "name": "Carlos",
    "grade": "A",
    "subjects": "95"
}

for student, info in studentInfo.items():
    print(f"Student info: {student}: {info}")

studentInfo["graduated"] = False

print()
for student, info in studentInfo.items():
    print(f"Student info: {student}: {info}")
