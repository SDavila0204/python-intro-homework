#if the integer is between 0 and 100
def is_valid_score(score):
    return 0 <= score <= 100

user_input = int(input("Please enter a score: "))

#if/else to find if score between 0 and 100
if is_valid_score(user_input):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")
