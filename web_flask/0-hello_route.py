 #!/usr/bin/python3
"""This module contain a Flask instance"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Function that starts a Flask web application"""
    return 'Hello HBNB!'
