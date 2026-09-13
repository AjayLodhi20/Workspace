from flask import Flask, flash, redirect, render_template, request, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY", "dev-key-change-in-production")


@app.route("/")
def home():
    return render_template(
        "base.html",
        content="Welcome to the portal. Select Login or Register above to continue.",
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        flash(f"Logged in successfully as {email}!")
        return redirect(url_for("home"))

    return render_template("auth/login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        flash(f"Account created for {username}! Please log in.")
        return redirect(url_for("login"))

    return render_template("auth/register.html")