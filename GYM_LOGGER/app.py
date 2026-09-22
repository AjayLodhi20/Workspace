from flask import Flask, flash, redirect, render_template, request, url_for
from dotenv import load_dotenv
import os
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("APP_SECRET_KEY", "dev-key-change-in-production")
# add database

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str]
    password: Mapped[str] = mapped_column(String(255))

with app.app_context():
    db.create_all()

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("user/list.html", users = users)


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")


        hashed_pass = generate_password_hash(password=password)
        user = db.session.execute(
                    db.select(User).filter_by(email=email)
                ).scalar_one_or_none()

        if user and check_password_hash(user.password, password):
            flash(f"logged in successfully as {user.username}!")
            return redirect(url_for("home"))

        else:
            flash(f"invalid email or password. Please try again.")
            return redirect(url_for("login"))
    return render_template("auth/login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)

        new_user = User(username = username, email = email, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()


        flash(f"Account created for {username}! Please log in.")
        return redirect(url_for("login"))

    return render_template("auth/register.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        return "post"
    return "hello world"




