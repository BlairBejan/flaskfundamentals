from flask import Flask, render_template, request, redirect

myninja = ""

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html")

@app.route("/ninjas/<color>", methods=["GET"])
def oneninja(color):
    global myninja
    if color != "blue" or "orange" or "red" or "purple":
        return render_template("not.html")
    if color == "blue":
        myninja = "leonardo.jpg"
    if color == "orange":
        myninja = "Michelangelo.jpg"
    if color == "red":
        myninja = "rafael.jpg"
    if color == "purple":
        myninja = "donatello.jpg"
    return render_template("oneninja.html")

app.run(debug=True)
