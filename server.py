from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

#app is defined
app = Flask(__name__)

#Routes
@app.route('/')
@app.route('/index')
def index():
    # return "Hello World!"
    return render_template("index.html", title="Home")

@app.route('/weather', methods=['GET', 'POST'])
# print(get_current_weather("London"))

#Sample
# {'coord': {'lon': -98.5006, 'lat': 38.5003}, 
# 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 
# 'main': {'temp': 2.36, 'feels_like': -1.33, 'temp_min': 2.36, 'temp_max': 2.36, 'pressure': 1031, 'humidity': 56, 'sea_level': 1031, 'grnd_level': 964}, 'visibility': 10000, 'wind': {'speed': 3.92, 'deg': 332, 'gust': 5.94}, 'clouds': {'all': 69}, 'dt': 1764172770, 'sys': {'type': 2, 'id': 2008008, 'country': 'US', 'sunrise': 1764163683, 'sunset': 1764198910}, 'timezone': -21600, 'id': 4273857, 'name': 'Kansas', 'cod': 200}
def weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city)
    if weather_data.get('cod') != 200:
        error_message = weather_data.get('message', 'An error occurred while fetching the weather data.')
        return render_template("weather.html", title="Error", error=error_message)
    # log to console
    print(weather_data)
    return render_template(
        "weather.html",
        title=weather_data['name'],
        city=weather_data['name'],
        status=weather_data['weather'][0]['description'],
        temp=f'{weather_data["main"]["temp"]:.1f}',
        feels_like=f'{weather_data["main"]["feels_like"]:.1f}',
        # title=weather_data['title'],
        # status=weather_data['weather'][0]['description'],
        # temp=f'{weather_data["main"]["temp"]}:.1f',
        # feels_like=f'{weather_data["main"]["feels_like"]}:.1f',
    )

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5500)
    serve(app, host="0.0.0.0", port=5500)