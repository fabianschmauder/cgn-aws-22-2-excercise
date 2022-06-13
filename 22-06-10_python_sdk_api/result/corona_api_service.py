import requests

def fetch_corona_data():
    response = requests.get(
        "https://api.covid19api.com/country/germany/status/confirmed/live")
    return response.json()
