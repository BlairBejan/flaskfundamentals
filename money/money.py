from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

gold = 0 
activities = []

@app.route("/")
def index():
    return render_template("index.html", gold=gold, activities=activities)

@app.route("/process_money", methods=["POST"])
def money():
    global gold
    if request.form["building"] == "farm":
        gold += random.randint(10, 20)
        # activities.append("earned {} gold from the farm".format())
    if request.form["building"] == "cave":
        gold += random.randint(5, 10)
    if request.form["building"] == "house":
        gold += random.randint(2, 5)
    if request.form["building"] == "casino":
        gold += random.randint(-50, 50)
    return redirect("/")

app.run(debug=True)