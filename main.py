import requests

ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
params = {

    "lat":42.417381,
    "lon":12.104850,
    "units":"metric",
    "appid":"c31f508cc53cdedf42d0280b0d2a2b2b"
}
response = requests.get(ENDPOINT, params=params)
jdata = response.json()
print(jdata)