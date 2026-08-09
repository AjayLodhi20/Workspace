from http.client import responses

import requests
from datetime import datetime
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response.status_code) #<Response [200]>
#
# # if response.status_code == 404:
# #     raise Exception("that resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access this data.")
#
# response.raise_for_status()
#
# longitude= response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])



parameters= {
    "lat": 20.593683,
    "lng": 78.962883,
}
response = requests.get(url=" https://api.sunrise-sunset.org/v2", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
