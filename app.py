from flask import Flask, render_template, request, redirect, url_for
from fruits import Fruit
from flask_modus import Modus

fruits = [
    Fruit("apple", 6),
    Fruit("banana", 9),
    Fruit("cherry", 6)
]

app = Flask(__name__)
modus = Modus(app)

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
def show(id):
    try:
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
    except IndexError:
        return render_template("404.html"), 404

@app.route("/fruits/<int:id>/edit")
def edit(id):
    try:
        found_fruit = [
            fruit
            for fruit in fruits 
            if fruit.id == id
        ][0]
        return render_template("edit.html", fruit=found_fruit)
    except IndexError:
        return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)










