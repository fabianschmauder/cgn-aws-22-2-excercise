import requests


response = requests.get("https://api.covid19api.com/country/germany/status/confirmed/live?from=2022-03-01T00:00:00Z&to=2022-06-01T00:00:00Z")

data = response.json()

for item in data:
    print(item["Date"] +": "+ str(item["Cases"]))