# Weather SMS Notifier - Umbrella Reminder

## Overview

This Python script checks the weather forecast for a specific location using the OpenWeatherMap API. If the forecast indicates rain within the next few hours, the script sends an SMS notification to a specified phone number via the Twilio API, reminding the user to bring an umbrella.

## Features

* **Weather Forecast Check:** Retrieves weather forecast data for a defined latitude and longitude from OpenWeatherMap.
* **Rain Detection:** Analyzes the weather conditions in the forecast to determine if it will rain.
* **SMS Notification:** Sends an SMS message via Twilio if rain is detected in the forecast.
* **Umbrella Reminder:** The SMS message reminds the user to take an umbrella.
* **Configurable Location:** The latitude and longitude in the script can be easily modified to check the weather for a different location.

## How to Use

1.  **Prerequisites:**
    * **Python 3:** Ensure you have Python 3 installed on your system.
    * **`requests` Library:** Install the `requests` library for making HTTP requests:
      ```bash
      pip install requests
      ```
    * **`twilio` Library:** Install the `twilio` library for sending SMS messages:
      ```bash
      pip install twilio
      ```
    * **OpenWeatherMap API Key:** Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
    * **Twilio Account:** Sign up for a Twilio account at [Twilio](https://www.twilio.com/). You will receive an Account SID and an Auth Token. You will also need a Twilio phone number.

2.  **Configuration:**
    * **Open `main.py` (or the name you saved the script as) and modify the following variables:**
        * `API_KEY`: Replace `"OPENWEATHER API"` with your actual OpenWeatherMap API key.
        * `weather_params["lat"]`: Update `CITY LATITUDE` to the latitude of your desired location.
        * `weather_params["lon"]`: Update `CITY LONGITUDE` to the longitude of your desired location.
        * `ACCOUNT_SID`: Replace `"TWILIO ACCOUNT SID"` with your Twilio Account SID.
        * `AUTH_TOKEN`: Replace `"TWILIO AUTH TOKEN"` with your Twilio Auth Token.
        * `from_`: Replace `"TWILIO PHONE NUMBER"` with your Twilio phone number.
        * `to`: Replace `"YOUR PHONE NUMBER"` with the recipient's phone number (including the country code).

3.  **Run the script:** Execute the Python script:
    ```bash
    python main.py
    ```

    The script will fetch the weather forecast, check for rain, and send an SMS notification if rain is predicted within the next few hours. You will see the status of the SMS message printed in the console.

## Project Structure

The project consists of a single Python file (e.g., `main.py`) which contains all the logic for fetching weather data and sending SMS notifications.

## Code Overview

* **Import Libraries:** Imports the `requests` library for making HTTP requests to the OpenWeatherMap API and the `twilio.rest.Client` for interacting with the Twilio API.
* **API Keys and Auth Tokens:** Defines variables to store the OpenWeatherMap API key, Twilio Account SID, and Twilio Auth Token. **Remember to replace the placeholder values with your actual credentials.**
* **OpenWeatherMap Parameters:** Creates a dictionary `weather_params` to hold the latitude, longitude (default set to Rio de Janeiro), API key, and the number of forecast hours to check (`cnt=4` means checking the forecast for the next 4 intervals).
* **Fetch Weather Data:** Uses `requests.get()` to retrieve weather forecast data from the OpenWeatherMap API using the specified endpoint and parameters. `response.raise_for_status()` checks for any errors in the API request. The JSON response is stored in `weather_data`.
* **Rain Detection Logic:**
    * Initializes a boolean variable `will_rain` to `False`.
    * Iterates through the list of hourly forecast data in `weather_data["list"]`.
    * For each hour, it extracts the weather condition code (`id`).
    * It checks if the condition code is less than 700, which generally indicates various forms of rain, snow, or other precipitation according to OpenWeatherMap's weather condition codes.
    * If a condition code indicating rain is found, `will_rain` is set to `True`, and the loop continues checking the remaining forecast hours.
* **Send SMS Notification:**
    * An `if will_rain:` block checks if the `will_rain` flag is `True`.
    * If it is raining (or predicted to rain), it initializes a Twilio `Client` with the provided Account SID and Auth Token.
    * It then uses `client.messages.create()` to send an SMS message with the body "It is going to rain today! 🌧️\nBring an umbrella!☔" to the specified `to` phone number from the specified `from_` Twilio number.
    * The `message.status` is printed to the console, indicating the delivery status of the SMS.
