import requests
from datetime import datetime
from email.message import EmailMessage
import smtplib


MY_LAT = 20.593683
MY_LONG = 78.962883
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response.status_code) #200
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

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False



def is_night():
    parameters= {
        "lat": MY_LAT,
        "lng": MY_LONG,
    }
    response = requests.get(url=" https://api.sunrise-sunset.org/v2", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True
    return False

if is_iss_overhead() and is_night():

    msg = EmailMessage()

    msg["subject"] = "ISS watch"
    msg["from"] = "satyamlodhi123@gmail.com"
    msg["to"] = "satyamlodhi735562@gmail.com"
    msg.set_content("ISS is above your head...")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("satyamlodhi123@gmail.com", 'uire emja eexd sgwg')
