from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "nowayyoucanguessthiskey"

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/guess", methods=["GET"])
def checkguess():
    session['compguess'] = random.randint(1, 10)
    session['myguess'] = request.form["myguess"]
    print session["compguess"]
    print session["myguess"]
    if session['compguess'] == session["myguess"]:
        return redirect("/", result="your right!")
    elif session['compguess'] > session["myguess"]:
        return redirect("/", result="too low!")
    elif session['compguess'] < session["myguess"]:
        return redirect("/", result="too high!")

app.run(debug=True)