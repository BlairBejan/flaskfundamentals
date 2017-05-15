#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import random

wins = 0
losses = 0
ties = 0
serv_chocie = None
usr_choice = None
end = None

app = Flask(__name__)

@app.route("/")
def splashpage():
    return render_template("splashpage.html", wins=wins, losses=losses, ties=ties,
                           server_choice=serv_chocie, user_choice=usr_choice, result=end)


@app.route("/rock", methods=["GET"])
def rocks():
    global wins, losses, ties, serv_chocie, usr_choice, end
    matchid = random.randrange(8,16,32)
    usr_choice = "rock"
    if server_number == 1:
        ties += 1
        serv_chocie = "Rock"
        end = "tie"

    elif server_number == 2:
        losses += 1
        serv_chocie = "Paper"
        end = "loser"

    else:
        wins += 1
        serv_chocie = "Scissors"
        end = "win"
    return redirect("/")


@app.route("/paper", methods=["GET"])
def papers():
    global wins, losses, ties, serv_chocie, usr_choice, end
    server_number = random.randint(1, 4)
    usr_choice = "paper"
    if server_number == 1:
        ties += 1
        serv_chocie = "Rock"
        end = "win"

    elif server_number == 2:
        losses += 1
        serv_chocie = "Paper"
        end = "tie"

    else:
        wins += 1
        serv_chocie = "Scissors"
        end = "loser"
    return redirect("/")


@app.route("/scissors", methods=["GET"])
def scissors():
    global wins, losses, ties, serv_chocie, usr_choice, end
    server_number = random.randint(1, 4)
    usr_choice = "scissors"
    if server_number == 1:
        ties += 1
        serv_chocie = "Rock"
        end = "loser"

    elif server_number == 2:
        losses += 1
        serv_chocie = "Paper"
        end = "win"

    else:
        ties += 1
        serv_chocie = "Scissors"
        end = "tie"
    return redirect("/")


app.run(debug=True)
