from flask_app import app

from flask import redirect, render_template, request

from flask_app.models.user import User


@app.route("/")
def home():
    return redirect("/users")

@app.route("/users")
def users():
    return render_template("user.html", users = User.get_all())

@app.route("/user/new")
def new():
    return render_template("new.html")


@app.route("/user/add", methods = ["POST"])
def add():
    print(request.form)
    User.save(request.form)
    return redirect ("/users")
