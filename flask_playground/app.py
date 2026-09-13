from flask import Flask, request, url_for, redirect, render_template
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.integer, primary_key = True)
#     name = db.Column(db.string(100))
#     date_joined = db.Column(db.DateTime)

# you name the function what you have in the brackets
@app.route("/")
def index():
    return render_template("index.html", page_name = "index")

@app.route("/home")
def home():
    return render_template("home.html", number = 2, dictionary = [{"key" : "value1"}, {"key" : "value2"}, {"key" : "value3"}])

@app.route("/json")
def json():
    return {"my_name": "ajay"}


@app.route('/help')
def projects():
    return "The project page"


@app.route("/dynamic", defaults={"user_input": "AJAY"})
@app.route("/dynamic/<user_input>")
def dynamic(user_input):
    return f"<h1>hello {user_input}</h1>"


@app.route("/query")
def query():
    hello = request.args.get("hello")
    world = request.args.get("world")
    return f"<h1>the query string contains {hello} and {world}</h1>"


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        return redirect(url_for('query'))
    return "<form method = POST><input type = 'text' name = 'user_input' /><input type = 'submit' /> </form>"


@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"HELLO, {escape(name)}"

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {escape(username)}"


@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f"{username}\'s profile"


@app.route("/error")
def error():
    a = 1/0
    return "Error"


@app.route("/profile", endpoint = "profile_page")
def user_profile():
    return f"<h1> hello </h1>"


