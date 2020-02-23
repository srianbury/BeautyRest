import os
from flask import Flask

message = "Hello from Heroku"

app = Flask(__name__)

if 'MESSAGE' in os.environ:
    message = os.environ['MESSAGE']
    print("message: %s" % message)

@app.route('/')
def hello_world():
    return '<b>' + message + '</b>'