from flask import Flask, render_template, request, redirect, url_for
from fruits import Fruit

fruits = [
    Fruit("apple", 6),
    Fruit("banana", 9),
    Fruit("cherry", 6)
]

app = Flask(__name__)

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

@app.route("/fruits/<int:id>")
def show(id):
    found_fruit = [
        fruit
        for fruit in fruits 
        if fruit.id == id
    ]
    if found_fruit:
        return render_template("show.html", fruit=found_fruit[0])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)










