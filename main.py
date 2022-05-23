import requests
import os
from dotenv import load_dotenv # this package use for take env
import datetime as datetime
load_dotenv()

#-------------API and KEY----------
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
NUTRITIONNIX_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API = "https://api.sheety.co/9fe831d2374894c4af50391028cb84f7/workoutTracker/workouts"

#---------GLOBAL VARIABLE----------
gender = os.getenv('GENDER')
weight = os.getenv('weight')
height = os.getenv('height')
age = os.getenv('age')

get_string = input("Tell me what you do: ")
today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

#--------Parameters and headers--------
parameter = {
    "query": get_string,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
sheety_header = {
    "Authorization": os.getenv('AUTHORIZATION_HEADER')
}
exercise_status = requests.post(NUTRITIONNIX_API, json=parameter, headers = headers)
exercise_status = exercise_status.json()
print(exercise_status)
for exercise in exercise_status["exercises"]:

    workouts ={
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": str(exercise["name"]),
            "duration": str(exercise["duration_min"]),
            "calories": str(exercise["nf_calories"])
        }
    }

    post_to_sheet = requests.post(url=SHEETY_API, json=workouts, headers = sheety_header)
    print(post_to_sheet.text)


