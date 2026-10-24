students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
#loop to find top score
highestScore = float()
stuName = ""
subject = ""

for studentInformation in students:
    if studentInformation["score"] > highestScore:
        highestScore = studentInformation["score"]
        stuName = studentInformation["name"]
        stuSubject = studentInformation["subject"]

print(f"name: {stuName}, score: {highestScore}")

#calculates class average

#setting score to 0
totalScore = 0

for studentInformation in students:
    totalScore += studentInformation["score"]

#finds the average
classAve = totalScore/len(students)

print(f"Class average: {classAve}")

#lists all unique subjects

#stores subjects
subjectList = []

#finds them in data set
for studentInformation in students:
    subjectList.append(studentInformation['subject'])

#filters them out and removes duplicates
subjectList = set(subjectList)

#prints them out
print(f"subjects offered: {subjectList}")


#lists all scores higher than a 75

#will store names of students scoring above a 75
highScores = []

#for loop to collect the names of students scoring above a 75
for studentInformation in students:
    if studentInformation['score'] > 75:
        highScores.append(studentInformation['name'])

print(f"Smartest students: {highScores}")
