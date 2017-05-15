from flask import Flask, render_template, request, redirect
# from random

app = Flask(__name__)

@app.route("/")
def rockpaperscissors():
    return render_template("rockpaperscissors.html")

@app.route("/click", methods = ["GET"])
def play():
    value = 0 
    aivalue = 0
    # aivalue = random.randint(1,3)
    if form.validate_on_submit():
        if 
        print "rock"
    return redirect('/')


# wins = 0
# losses = 0
# ties = 0
app.run(debug=True)
