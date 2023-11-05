from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

# @app.route("/member")
# def home():
#     return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == '__main__':
   app.run(debug=True)
