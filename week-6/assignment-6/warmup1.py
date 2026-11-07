def greet(name, greeting= "Hello"):
    print(f"{greeting} {name}!!")

#only the name
greet("Alex")

#name and custom greeting
greet("Alex", "Good morning")

#greeting passed as keyword
greet("Alex", "Hi!")
