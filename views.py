from flask import Blueprint, render_template, request
from api import weather_specs
import datetime as dt

weather_specs_default = weather_specs("Salinas Valley")

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template('index.html', jsonFile=weather_specs_default)
