# Weather App API

import requests 
from pprint import pprint

API_key = 'a48b5a89c65391e0c4772ddbe0bf8580'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_key+ "&q="+ city

weather_data = requests.get(base_url).json()

pprint(weather_data)



