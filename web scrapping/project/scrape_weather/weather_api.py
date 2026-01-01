import requests

API_KEY = "fb7261af1eb1a4bdd26e0751f1f38995"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city, units="metric"):
    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": units
    }

    response = requests.get(BASE_URL, params=parameters)

    if response.status_code == 200:
        return response.json()
    else:
        return None