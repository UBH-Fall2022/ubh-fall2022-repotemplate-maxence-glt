import datetime as dt
import requests
import ssl
import certifi
import geopy.geocoders
import sys
import json

from geopy.geocoders import Nominatim

from urllib.parse import quote as urlencode

# Helper functions
def degToCompass(num) -> str:
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return arr[(val % 16)]
def time_format(time: str) -> str:
    hour = int(time[:2])
    if hour < 10:
        return time[1:] + " AM"
    if hour <= 12:
        return time + " AM"
    else:
        hour = hour - 12
        return str(hour) + time[2:] + " PM"



# ssl certification for geopy
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx




def weather_specs(location: str) -> dict:
    """Function that takes in any location on earth and (address, city, state)
    and returns a tuple with the attributes, in order, of the precipitation 
    probability, the cloud cover and the visibility of the input location at the
    current time, even optimizing for timezones"""
    geolocator = Nominatim(user_agent="my_request")
    getLoc = geolocator.geocode(location)
    if getLoc is None: return False

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={getLoc.latitude}&longitude={getLoc.longitude}&hourly=temperature_2m,relativehumidity_2m,precipitation_probability,evapotranspiration,soil_temperature_6cm,soil_moisture_3_to_9cm&forecast_days=14")
    print(f"https://api.open-meteo.com/v1/forecast?latitude={getLoc.latitude}&longitude={getLoc.longitude}&hourly=temperature_2m,relativehumidity_2m,precipitation_probability,evapotranspiration,soil_temperature_6cm,soil_moisture_3_to_9cm&forecast_days=14")
    # making sure the API key was input correctly
    if response.status_code != 200:
        print("API Key Invalid")
        return None
    
    # API CALL REFS!!
    # To get weather var: ["hourly"]["YOUR_WEATHER_VAR"][dt.datetime.now().hour + YOUR_TIME_VAR]
    # YOUR_WEATHER_VARs: string value - "temperature_2m", "relativehumidity_2m", "precipitation_probability", 
    #                    "evapotranspiration", "soil_temperature_6cm", "soil_moisture_3_to_9cm",
    
    # YOUR_TIME_VAR: integer value - add 0 for current, add 24 for next day same time, -x for x hours before, etc

    # EX: Getting humidity of next day (done on HTML file) ["hourly"]["relativehumidity_2m"][dt.datetime.now().hour + 24]


    return response.json()

