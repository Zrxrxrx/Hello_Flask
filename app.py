from flask import Flask
from flask import url_for, escape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello flask!'
