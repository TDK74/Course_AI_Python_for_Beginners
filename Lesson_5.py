import os
import requests

from aisetup import print_llm_response
from dotenv import load_dotenv


## ------------------------------------------------------ ##
load_dotenv('.env', override=True)
api_key = os.getenv('WEATHER_API_KEY')

## ------------------------------------------------------ ##
lat = 42.6978
lon = 23.3217

## ------------------------------------------------------ ##
url = (f"https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=1"
        f"&lat={lat}&lon={lon}&appid={api_key}")

response = requests.get(url)

## ------------------------------------------------------ ##
data = response.json()

print(data)

## ------------------------------------------------------ ##
temperature = data['list'][0]['main']['temp']
description = data['list'][0]['weather'][0]['description']
wind_speed = data['list'][0]['wind']['speed']

## ------------------------------------------------------ ##
print(f"Temperature: {temperature}")
print(f"Weather Description: {description}")
print(f"Wind Speed: {wind_speed}")

## ------------------------------------------------------ ##
weather_string = f"""The temperature is {temperature}°C.
                It is currently {description},
                with a wind speed of {wind_speed}m/s.
                """

print(weather_string)

## ------------------------------------------------------ ##
prompt = f"""Based on the following weather,
        suggest an appropriate outdoor outfit.

        Forecast: {weather_string}
        """

print_llm_response(prompt)

## ------------------------------------------------------ ##
lat = 42.6978
lon = 23.3217
url = (f"https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=1"
        f"&lat={lat}&lon={lon}&appid={api_key}")
response = requests.get(url)

data = response.json()
feels_like = data['list'][0]['main']['feels_like']
city = data['city']['name']
print(f"The temperature currently feels like {feels_like}°C in {city}.")
