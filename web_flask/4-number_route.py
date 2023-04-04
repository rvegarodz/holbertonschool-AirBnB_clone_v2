#!/usr/bin/python3
"""This module contain a Flask instance"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function that starts a Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_2():
    """Function that starts a Flask web application"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_3(text):
    """Function that starts a Flask web application"""
    return 'C ' + f'{escape(text)}'.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def hello_4(text):
    """Function that starts a Flask web application"""
    return 'Python ' + f'{escape(text)}'.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def hello_5(n):
    """Function that starts a Flask web application"""
    if type(n) == int:
        return f'{escape(n)}' + ' is a number'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
