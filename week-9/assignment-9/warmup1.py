import requests

#url given in instructions
url = "https://api.agify.io/?name=michael"

#makes the request to the REST countries
response = requests.get(url)

#prints status code and the response
print(f"Status code: {response.status_code}") 
print(f"Response: {response.json()}")
