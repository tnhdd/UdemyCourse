import requests
from datetime import datetime
app_id = "2adf1bc7"
api_key = "000562ca56b093f7fb0a56ab7c679dac"

gender = "male"
weight_kg = 71
height_cm = 171
age = 25

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/22a45d09cfe92d4cf5e5aab5c5dc3342/workoutTracking/workouts"
exercise = input("What did you do today? ")

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

nutrition_param = {
    "query": exercise,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

response = requests.post(url=nutrition_endpoint, json=nutrition_param, headers=headers)
data = response.json()
# print(data)]

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_input = {
        "workout":{
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint,json=sheet_input)
    print(sheet_response.text)
