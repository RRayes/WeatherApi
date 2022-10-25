import json
import requests
from geopy.geocoders import Nominatim


def weather(lat, lon):
    url = f"{base_url}lat={lat}&lon={lon}&appid={api}&units=imperial"
    response = requests.get(url).json()
    # print(json.dumps(response, indent=4)) #shows entire json data retrieved from api call
    humidity = []
    feels_temp = []
    weather = []
    weather_description = []
    wind = []
    for count in range(0, 7, 3):
        humidity.append(response["list"][count]["main"]["humidity"])
        feels_temp.append(response["list"][count]["main"]["feels_like"])
        weather.append(response["list"][count]["weather"][0]["main"])
        weather_description.append(response["list"][count]["weather"][0]["description"])
        wind.append(response["list"][count]["wind"]["speed"])

    for count in range(0, 3):
        print(f"Day {count+1} forcast")
        print(f"humidity: {humidity[count]}%")
        print(f"temp: {feels_temp[count]}\u00b0F")
        print(f"Sky: {weather[count]}")
        print(f"Details: {weather_description[count]}")
        print(f"wind: {wind[count]}Mph")
        print("-----------")


def lat_long(city):
    geolocator = Nominatim(user_agent="User")
    location = geolocator.geocode(city)
    lat = location.latitude
    lon = location.longitude
    weather(lat, lon)


def get_input():
    city = input("What Cities wheather would you like to check?: ")
    lat_long(city)


if __name__ == "__main__":
    base_url = 'http://api.openweathermap.org/data/2.5/forecast?'
    api = 'c35e59f4bca2558a6c41e35aa1cfd1f0'
    get_input()

# uses openweathersapi's built in lat,lon finder. !deprecated!
# other_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api}&units=imperial"
# print(other_url)
# response = requests.get(other_url).json()
# print(json.dumps(response, indent=4))
