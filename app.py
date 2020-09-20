import json
import requests
from game import mainGameMannager
from flask import *

# import pyrebase

mainGame =  mainGameMannager()

app = Flask(__name__)


toreturn = []

@app.route("/")
def aprubas():
    global options
    title, x, options = mainGame.startGame(5)
    opt = ['','','','']
    for i in range(len(options)):
        opt[i] = options[i][1]
    return render_template("prubas.html", titulo = title, body1 = opt[0], body2 = opt[1], body3 = opt[2], body4 = opt[3])

@app.route("/game")
def test():
    global options
    global toreturn
    title, x, options = mainGame.updateMetricsAndReturnNext(toreturn)
    if not x:
        mainGame.calculateVotes()
        if mainGame.gimmeWinner():
            a = 'you won boiiiiii'
        else:
            a = 'f in the chat, AI got more votes than you'
        return render_template("prubas.html", titulo = 'congrats boi', body1 = a, body2 = '', body3 = '', body4 = '')
    opt = ['','','','']
    for i in range(len(options)):
        opt[i] = options[i][1]
    return render_template("prubas.html", titulo = title, body1 = opt[0], body2 = opt[1], body3 = opt[2], body4 = opt[3])

@app.route("/run1")
def run1():
    global options
    global toreturn
    toreturn = options[0][3]

    return render_template("test.html")

@app.route("/run2")
def run2():
    global options
    global toreturn
    toreturn = options[1][3]
    return render_template("test.html")

@app.route("/run3")
def run3():
    global options
    global toreturn
    toreturn = options[2][3]
    return render_template("test.html")

@app.route("/run4")
def run4():
    global options
    global toreturn
    toreturn = options[3][3]
    return render_template("test.html")

if __name__ == "__main__":    
    app.run(debug = True)

