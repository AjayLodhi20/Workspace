import requests
from datetime import datetime

USERNAME = "satyamlodhi123"
TOKEN = "oshdgjogaslkjghl"
GRAPH = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
## creates account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)



# create a new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH,
    "name" : "Walking Graph",
    "unit": "Km",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# add a pixel to the graph

create_a_pixel = f"{graph_endpoint}/{graph_config["id"]}"


today = datetime(year=2026,month=8,day=23)
print(today.strftime("%Y%m%d"))

create_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8",
}



# pixel = requests.post(url=create_a_pixel, json=create_pixel, headers=headers)
# print(pixel.text)

# update a pixel
update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/20260823"

updating = requests.put(url=update, json=create_pixel, headers=headers)

print(updating.text)
