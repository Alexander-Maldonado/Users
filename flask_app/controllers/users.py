from dataclasses import dataclass
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

@app.route("/user/edit/<int:id>")
def edit(id):
    data={
        "id":id
    }
    return render_template("edit.html", user=User.get_one(data))

@app.route("/user/update", methods = ["POST"])
def update():
    User.update(request.form)
    return redirect("/users")

@app.route("/user/deleteconfirm/<int:id>")
def confirm(id):
    data={
        "id":id
    }
    return render_template("delete.html", user=User.get_one(data))

@app.route("/user/delete/<int:id>")
def delete(id):
    data ={
        "id":id
    }
    User.delete(data)
    return redirect("/users")

@app.route("/user/view/<int:id>")
def View(id):
    data={
        "id":id
    }
    return render_template("view.html", user=User.get_one(data))