import requests

# Weatherstack API endpoint and parameters
api_key = "a3e84715911580f0970d81391cc4c4f2"  # Replace with your Weatherstack API key
location = "Delhi"  # Replace with your desired location
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


url = BASE_URL + "appid=" + api_key + "&q=" + location

# Make the request to Weatherstack API
response = requests.get(url)


# Check if request was successful
if response.status_code == 200:

    data = response.json()
    print(data)
    Location = data['name']
    Temperature = data['main']['temp']
    print(Temperature, " at ", Location)

else:
    print("Failed to retrieve weather data.")
