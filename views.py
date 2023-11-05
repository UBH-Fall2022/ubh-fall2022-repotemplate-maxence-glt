from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template('index.html')

@views.route("/ayush")
def ayush():
    return render_template('ayush.html')

@views.route("/about")
def about():
    return render_template('about.html')

@views.route("/help")
def help():
    return render_template('help.html')