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


@app.route('/c/<text>', strict_slashes=False, defaults = ['is cool'])
def hello_3(text):
    """Function that starts a Flask web application"""
    if '_' in text:
        text.replace('_', ' ')
    return f'C {escape(text)}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
