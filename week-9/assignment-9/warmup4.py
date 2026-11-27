import requests

#URL that WILL fail
url = "https://thisurldoesnotexist.example.com"

try:
    #GET request attempt
    response = requests.get(url)
    
    #checks whether status is anything other than 200
    if response.status_code != 200:
        print(f"Error: Server responded with status code {response.status_code}.")
    else:
        print("Success:", response.json())

except requests.exceptions.RequestException:
    #prints message if error occurs
    print("Error: Could not reach the server. Please try again later.")
