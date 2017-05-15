from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
  return render_template("dojosurvey.html")
@app.route('/dojoinfo', methods=['POST'])
def create_user():
   print "Got Post Info"
   # notice how the key we are using to access the info corresponds with the names
   # of the inputs from our html form
   session["firstname"] = request.form['firstname']
   session["lastname"] = request.form['lastname']
   session["gender"] = request.form['gender']
   return redirect('/') # redirects back to the '/' route
@app.route('/show')
def show_user():
  return render_template('user.html', firstname=session['firstname'], lastname=session['lastname'], gender=session["gender"])
app.run(debug=True)