from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://localhost/fruits-db-brand-new"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

modus = Modus(app)
db = SQLAlchemy(app)

class Fruit(db.Model):

    __tablename__ = "fruits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    image = db.Column(db.Text)
    sweetness = db.Column(db.Integer)
    sourness = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __init__(self, name, sweetness, sourness, image, price):
        self.name = name
        self.sweetness = sweetness
        self.sourness = sourness
        self.image = image
        self.price = price

    def __repr__(self):
        return f"Fruit #{self.id}; Name: {self.name}; Sweetness: {self.sweetness}; Sourness: {self.sourness}"

@app.route("/fruits", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_fruit = Fruit(
            request.form.get("name"),
            int(request.form.get("sweetness"))
        )
        db.session.add(new_fruit)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("index.html", fruits=Fruit.query.all())

@app.route("/fruits/new")
def new():
    return render_template("new.html")

@app.route("/fruits/<int:id>", methods=["GET", "DELETE", "PATCH"])
def show(id):
    found_fruit = Fruit.query.get_or_404(id)
    if request.method == b"DELETE":
        db.session.delete(found_fruit)
        db.session.commit()
    if request.method == b"PATCH":
        found_fruit.name = request.form['name']
        found_fruit.sweetness = int(request.form['sweetness'])
        db.session.add(found_fruit)
        db.session.commit()
    if request.method == "GET":
        return render_template("show.html", fruit=found_fruit)
    return redirect(url_for("index"))

@app.route("/fruits/<int:id>/edit")
def edit(id):
    found_fruit = Fruit.query.get_or_404(id)
    return render_template("edit.html", fruit=found_fruit)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
