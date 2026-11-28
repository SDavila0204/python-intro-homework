import requests

url = "https://api.agify.io/?name=michael"

#making request and parsing data
response = requests.get(url)
data = response.json()

name = data.get("name")
age = data.get("age")
#adding fallback message
birthday = data.get("birthday", "Data not available")

#PRINTING MESSAGE
print(f"Name: {name}") 
print(f"Age: {age}") 
print(f"Birthday: {birthday}")

