from flask import Flask

app = Flask('name')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def goodbye_world():
    return "<p>Goodbye, World!</p>"