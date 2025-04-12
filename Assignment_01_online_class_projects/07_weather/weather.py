import requests
from pprint import pprint

API_KEY='cb771e45ac79a4e8e2205c0ce66ff633'


city=input("Enter a city : ")


# Include the city in the URL query
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(base_url)
weather_data = response.json()
pprint(weather_data)