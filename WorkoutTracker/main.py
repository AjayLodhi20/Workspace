import pandas as pd
import openpyxl
from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()
# create a dictionary of exercise data..
app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")


nutrition_url = "https://app.100daysofpython.dev"

headers = {
    'x-app-id': app_id,
    'x-app-key': api_key,
}

exercise_endpoint = f"{nutrition_url}/v1/nutrition/natural/exercise"

request_body = {
    "query": "ran 20m 1km",
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

exercise_dict = {}
for exercise in dict_from_exer["exercises"]:
    exercise_dict["Date"] = date_today
    exercise_dict["Time"] = time_today
    exercise_dict["Exercise"] = exercise["name"]
    exercise_dict["Duration"] = exercise["duration_min"]
    exercise_dict["Calories"] = exercise["nf_calories"]


print(exercise_dict)

# post the row into excel
df = pd.read_excel("workout.xlsx")
print(df)

