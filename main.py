import requests
from twilio.rest import Client

# This code retrieves weather information from the OpenWeatherMap API for a specific location, formats the data,
# and sends it as an SMS message using the Twilio API. It starts by importing the required modules, requests and
# twilio, and initializes the authentication tokens for the Twilio account.

# The code then specifies the latitude, longitude, and units for the weather data request, and sends a GET request to
# the OpenWeatherMap API. The response is stored in JSON format and processed to retrieve the weather information for
# the next 12 hours (4 time intervals with 3-hour increments).

# The retrieved weather information is then formatted into a string that includes the time, temperature, feels-like
# temperature, and weather condition for each of the 3-hour intervals. Finally, this formatted string is sent as an
# SMS message using the Twilio API, to the phone number specified in the 'to' field of the 'message' object.

# THIS CODE BY AZIZ SMAOUI https://github.com/loading04

# TODO change account_sid of twilio
# TODO change auth_token of twilio
# TODO change api_key of open weather api
# TODO change LATITUDE
# TODO change LONGITUDE
# TODO change number of sender
# TODO change number of reciver


account_sid = "YOUR ACCOUNT SID OF TWILIO API"
auth_token = "YOUR AUTH TOKEN OF TWILIO API"
client = Client(account_sid, auth_token)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOU API KEY OF OPEN WEATHER API"

weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": api_key,
    "units": "metric",
}
response = requests.get(OWM_Endpoint, params=weather_params)
data = response.json()
days = data["list"][:4]

list_of_hours = []

for i in range(0, 3):
    dicst = {
        "time": "",
        "weather": "",
        "temperature": 0,
        "feels": 0,
    }
    weather = days[i]["weather"][0]["main"]
    dicst["weather"] = weather
    time = days[i]["dt_txt"][11:16]
    dicst["time"] = time
    temperature = days[i]["main"]["temp"]
    dicst["temperature"] = temperature
    feels = days[i]["main"]["feels_like"]
    dicst["feels"] = feels
    list_of_hours.append(dicst)

weather_brief = f"so today at {list_of_hours[0]['time']} temperature is {list_of_hours[0]['temperature']}\n" \
                f" but if feels like {list_of_hours[0]['feels']} \n" \
                f" the weather is {list_of_hours[0]['weather']} \n " \
                f" after that at {list_of_hours[1]['time']} temperature is {list_of_hours[1]['temperature']}\n" \
                f" but if feels like {list_of_hours[1]['feels']} \n" \
                f" the weather is {list_of_hours[1]['weather']} \n " \
                f" after that at {list_of_hours[2]['time']} temperature is {list_of_hours[2]['temperature']}\n" \
                f" but if feels like {list_of_hours[2]['feels']} \n" \
                f" the weather is {list_of_hours[2]['weather']} \n "


message = client.messages.create(
    body=f"{weather_brief}",
    from_="PHONE NUMBER PROVIDED BY TWILIO",
    to="YOU PHONE NUMBER OR ANY NUMBER YOU WISH TO SEND"
)
