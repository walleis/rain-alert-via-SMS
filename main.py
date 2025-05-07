import requests
from twilio.rest import Client

# API keys and auth tokens.
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast" # OpenWeather API endpoint
API_KEY = "724c91df695389ce582e9a11db8ecd09" # OpenWeather API Key

ACCOUNT_SID = "AC133a9dd29e7fc6b519813fdabf5e3860" # Twilio account ID
AUTH_TOKEN = "e1181139ff3cde52921e25f61b8a7633" # Twilio auth token


# Params for the OpenWeather.
weather_params = {
    "lat": -22.908333,
    "lon": -43.196388,
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
        from_="+12317511937", # Number from Twilio
        to="+5521970135600", # Your phone number
    )
    print(message.status)