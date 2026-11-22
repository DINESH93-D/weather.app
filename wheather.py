import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def getweather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    return requests.get(BASE_URL, params=params, timeout=10)


def parseweather(response):
    data = response.json()

    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }


def displayweather(weather):
    print("\nWeather Information:")
    print("City:", weather["city"])
    print("Temperature:", weather["temp"], "°C")
    print("Feels Like:", weather["feels_like"], "°C")
    print("Humidity:", weather["humidity"], "%")
    print("Condition:", weather["condition"])
    print("Wind Speed:", weather["wind_speed"], "m/s")


def main():
    city = input("Enter the city name: ")

    try:
        response = getweather(city)

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            weather = parseweather(response)
            displayweather(weather)

        elif response.status_code == 404:
            print("City not found. Please check the city name.")

        else:
            print("Error occurred while fetching weather data.")
            print("Status Code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", str(e))

    except Exception as e:
        print("An unexpected error occurred:", str(e))


if __name__ == "__main__":
    main()