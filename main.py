import requests

ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
params = {

    "lat":42.417381,
    "lon":12.104850,
    "units":"metric",
    "appid":"c31f508cc53cdedf42d0280b0d2a2b2b"
}

#response = requests.get(ENDPOINT, params=params)
#jdata = response.json()
#print(jdata)

def get_weather_data():
    response = requests.get(ENDPOINT, params=params)
    return response


# Questo blocco esegue lo script solo se viene avviato direttamente (non durante i test)
if __name__ == "__main__":
    response = get_weather_data()
    print(response.json())