from flask import Flask, request, Response
import json
import random

app = Flask('name')

@app.route("/")
def index():
    print(request.json)
    return  jsonify(serverplay(request.json))

# dale pues maldita puta codea
def produceBoard():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    return board

def jsonify(input):
    return Response(
        json.dumps(input),
        mimetype="application/json"
    )
def serverplay(board):
    line = random.randint(0,2)
    column = random.randint(0,2)
    
    board[line][column] = 0 
    return board