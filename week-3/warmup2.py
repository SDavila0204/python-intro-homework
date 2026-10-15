age = int(input("What is your age? "))

if age <= 12:
    print("You are a child.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
elif age >= 18 and age < 64:
    print ("you are an adult.")
elif age > 65:
    print("You are a senior.")
