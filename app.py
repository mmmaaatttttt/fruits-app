from flask import Flask, render_template, request, redirect, url_for, abort
from fruits import Fruit
from flask_modus import Modus

fruits = [
    Fruit("apple", 6),
    Fruit("banana", 9),
    Fruit("cherry", 6)
]

app = Flask(__name__)
modus = Modus(app)

from functools import wraps

def ensure_valid_id(fn):
    @wraps(fn)
    # these are args and kwargs from function
    # being decorated: show, edit, etc
    def wrapper(*args, **kwargs):
        found_fruit = [
            fruit
            for fruit in fruits
            if fruit.id == kwargs.get('id')
        ]
        if len(found_fruit) == 1:
            return fn(*args, **kwargs)
        return abort(404)
    return wrapper

@app.route("/fruits", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_fruit = Fruit(
            request.form.get("name"),
            int(request.form.get("sweetness"))
        )
        fruits.append(new_fruit)
        return redirect(url_for("index"))
    return render_template("index.html", fruits=fruits)

@app.route("/fruits/new")
def new():
    return render_template("new.html")

@app.route("/fruits/<int:id>", methods=["GET", "DELETE", "PATCH"])
@ensure_valid_id
def show(id):
    found_fruit = [
        fruit
        for fruit in fruits 
        if fruit.id == id
    ][0]
    if request.method == b"DELETE":
        fruits.remove(found_fruit)
    if request.method == b"PATCH":
        found_fruit.name = request.form['name']
        found_fruit.sweetness = int(request.form['sweetness'])
    if request.method == "GET":
        return render_template("show.html", fruit=found_fruit)
    return redirect(url_for("index"))

@app.route("/fruits/<int:id>/edit")
@ensure_valid_id
def edit(id):
    found_fruit = [
        fruit
        for fruit in fruits 
        if fruit.id == id
    ][0]
    return render_template("edit.html", fruit=found_fruit)

if __name__ == "__main__":
    app.run(debug=True)










