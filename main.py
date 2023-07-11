import requests
from datetime import datetime

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercises you did: ")

nutri_params = {
    "query": query,
    "gender": "male",
    "weight_kg":60.5,
    "height_cm":190.64,
    "age": 25
}

headers = {
    "x-app-id": "6b3574a8",
    "x-app-key": "10b7a2290a7be30c3e7dc88f95b4af8b",
    "Content-Type": "application/json"
}

url = requests.post(nutritionix_endpoint, json=nutri_params, headers=headers)
response = url.json()

sheety_endpoint = "https://api.sheety.co/e52686a4332e4a1ce599bade3e1ea441/myWorkouts/workouts"

sheety_params = {
    "workout":
        {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": response['exercises'][0]['name'].title(),
            "duration": round(response['exercises'][0]['duration_min'],0),
            "calories": round(response['exercises'][0]['nf_calories'],0)
        }
}
sheety_header = {
    "Content-Type": "application/json",
    "Authorization": "ENTER TOKEN HERE"
}

url_sheety = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_header)
print(url_sheety.status_code)