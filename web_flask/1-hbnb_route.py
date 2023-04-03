#!/usr/bin/python3
"""This module contain a Flask instance"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function that starts a Flask web application"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello_2():
    """Function that starts a Flask web application"""
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

