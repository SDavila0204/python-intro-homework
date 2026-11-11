with open(r'data\notes.txt', 'r') as file:
    for lineNum, line in enumerate (file, start=1): #the 'start' dictates what num it starts from
        print(f"Line {lineNum}: {line.strip()}")  # .strip() removes the newline character at the end

