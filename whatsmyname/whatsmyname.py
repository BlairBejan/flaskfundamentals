from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def landingpage():
    return render_template("whatsmyname.html")

@app.route("/process", methods=["POST"])
def formdata():
    name = request.form["firstname"]
    print name
    return redirect("/")

app.run(debug=True)