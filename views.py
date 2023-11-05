from flask import Blueprint, render_template, request
from api import weather_specs, fullLocation

views = Blueprint(__name__, "views")

defaultWeather = weather_specs("Buffalo")
locationIndex = "Buffalo"

views = Blueprint(__name__, "views")

@views.route("/ayush", methods = ["POST", "GET"])
def home():
    global defaultWeather, locationIndex
    if request.method == "GET":
        return render_template('index.html', loc=locationIndex, test=defaultWeather)
    
    if request.method == "POST":
        location = request.form.get("location")
        defaultWeather = weather_specs(location)

        if defaultWeather == False:
            return render_template("error.html", request=location)
            

        locationIndex=location        

        return render_template("index.html", loc=fullLocation(location), test=defaultWeather)

@views.route("/")
def ayush():
    return render_template('ayush.html')

@views.route("/about")
def about():
    return render_template('about.html')

@views.route("/help")
def help():
    return render_template('help.html')
