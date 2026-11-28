import os
import requests

API_KEY = os.environ.get("RESTCOUNTRIES_API_KEY")

if not API_KEY:
	print("API key not found. Please try again")
	exit()

url = "https://api.restcountries.com/countries/v5/region/Europe?response_fields=names.common,population"

header = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(url, header=header)

if response.status_code == 200:
	data = response.json()

	countries_list = data.get("data", {}).get("objects", [])

	for item in countries_list[:10]:
		country_name = item.get("names", {}).get("common")
		if country_name:
			print(country_name)
else:
	print(f"request failed. Status code {response.status_code}")
