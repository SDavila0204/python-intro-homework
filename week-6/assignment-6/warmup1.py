def greeting(name, hello= "hello"):
    print(f"{hello} {name}!!")

#only the name
greeting("Alex")

#name and custom greeting
greeting("Alex", "Good morning")

#greeting passed as keyword
greeting("Alex", "Hi!")
