import requests
import os


api_key = "f86bb25f3c238f05f3545a7b11476ca7"

parameters = {
    "lat" : 20.593683,
    "lon" : 78.962883,
    "appid" : api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella..")