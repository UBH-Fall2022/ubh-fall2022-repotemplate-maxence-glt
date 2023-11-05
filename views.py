from flask import Blueprint, render_template, request
from api import weather_specs

defaultWeather = weather_specs("Buffalo")
locationIndex = "Buffalo"

views = Blueprint(__name__, "views")

@views.route("/", methods = ["POST", "GET"])
def home():
    global defaultWeather, locationIndex
    if request.method == "GET":
        return render_template('index.html', loc=locationIndex, test=defaultWeather)
    
    if request.method == "POST":
        location = request.form.get("location")
        defaultWeather = weather_specs(location)

        print(defaultWeather, "THIS IS THE LOCATION")

        if defaultWeather == False:
            return render_template("error.html", request=location)

        locationIndex=location

        

        return render_template("index.html", loc=locationIndex, test=defaultWeather)
