import requests
from twilio.rest import Client

# API keys and auth tokens.
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast" # OpenWeather API endpoint
API_KEY = "OPENWEATHER API KEY" # OpenWeather API Key

ACCOUNT_SID = "TWILIO ACCOUNT SID" # Twilio account ID
AUTH_TOKEN = "TWILIO AUTH TOKEN" # Twilio auth token


# Params for the OpenWeather.
weather_params = {
    "lat": YOUR CITY LATITUDE,
    "lon": YOUR CITY LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}


# Get the OpenWeather data.
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


# If it rains an SMS will be sent to reminder to bring an umbrella.
will_rain = False
for hour_data in weather_data["list"]: # Loop through the weather conditions list
    condition_code = hour_data["weather"][0]["id"] # Get the weather ID corresponding to rain
    if int(condition_code) < 700: # Check if it is raining
        will_rain = True # If true, it is raining

# If it's raining an SMS will be sent
if will_rain:
    client = Client(account_sid, auth_token) # Logging in Twilio
    message = client.messages.create(
        body="It is going to rain today! 🌧️\nBring an umbrella!☔", # SMS Message
        from_="TWILIO PHONE NUMBER", # Number from Twilio
        to="YOUR PHONE NUMBER", # Your phone number
    )
    print(message.status)
