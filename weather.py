from dotenv import load_dotenv
from pprint import pprint
import requests 
import os

load_dotenv()
API_key = os.getenv('OPENWEATHER_API_KEY')

# get weather for any city
def get_current_weather(city):
    # request_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}'
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'

    weather_data = requests.get(request_url).json()
    print("this is running\n")
    return weather_data
    
if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input('\nPlease enter a city')

    #Sanitize
    if not bool(city.strip()):
        city = "London"

    # city = city.strip()
    weather_data = get_current_weather(city)

    print('\n')
    # print(weather_data, "this is weather data\n")