import requests
from pprint import pprint

API_Key = "aaf4d494099f29b67fdf51bd57d30134"
city = input("Enter a city name ")
base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key
weather_date = requests.get(base_url).json()
print(weather_date)