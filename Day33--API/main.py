import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code) #<Response [200]>

# if response.status_code == 404:
#     raise Exception("that resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")

response.raise_for_status()

longitude= response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
