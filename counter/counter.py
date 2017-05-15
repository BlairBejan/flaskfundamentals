from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route("/")
def start():
    if session["count"] == False:
        session["count"] = 0 
    return render_template("counter.html")

@app.route("/plustwo", methods=["get"])
def increment():
    session["count"] += 2
    print "added two"
    return redirect("/")
app.run(debug=True)