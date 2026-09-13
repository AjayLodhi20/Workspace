import requests
import datetime

APP_ID = 'app_9d03ba6dab184177aff4c178'
API_KEY = 'nix_live_B6TtzNVscYm6RY2rC0J4PkHjOOwT1xDh'


nutrition_url = "https://app.100daysofpython.dev"

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

exercise_endpoint = f"{nutrition_url}/v1/nutrition/natural/exercise"

request_body = {
    "query": "ran 20m 1km",
    "height_cm": 175,
    "age": 26,
    "gender": "male"
}

today = datetime.datetime.now()
print(today)

date_today = today.strftime("%d/%m/%Y")

time_today = today.strftime("%H:%M:%S")

response = requests.post(url=exercise_endpoint, json=request_body, headers=headers)
dict_from_exer = response.json()
# dict_from_api["date"] = date_today
# dict_from_api["time"] = time_today
print(dict_from_exer)

sheety_endpoint = 'https://api.sheety.co/1106d12202afae3360168efe512c73af/myWorkouts/workouts'


for exercise in dict_from_exer["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date_today,
            "time": time_today,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    header = {
        "Content-Type": "application/json",
        'Authorization': 'Basic c2F0eWFtbG9kaGkxMjM6UmFtc3VuZGVyMTIzQEBA'
    }
    sheetyAddARow= requests.post(url=sheety_endpoint, json=sheet_inputs, headers=header)
    print(sheetyAddARow.text)
    print(sheetyAddARow.status_code)