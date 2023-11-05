from flask import Blueprint, render_template, request
from api import weather_specs
import datetime as dt

weather_specs_default = weather_specs("San Jose")

views = Blueprint(__name__, "views")

@views.route("/member")
def home():
    return {"members": ["Member1", "Member2", "Member3"]}
