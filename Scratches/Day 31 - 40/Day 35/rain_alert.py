import requests

api_key = "aaf4d494099f29b67fdf51bd57d30134"
endpoint = f"https://api.openweathermap.org/data/2.5/onecall"

weather_parameters = {
    "lat": 52.6638,
    "lon": 8.6267,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(endpoint, params=weather_parameters)
response.raise_for_status()

weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")

# print(weather_data["hourly"][0]["weather"][0]["id"])
