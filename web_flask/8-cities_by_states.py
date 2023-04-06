#!/usr/bin/python3
"""This module contain a Flask instance"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City

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


@app.route('/number_template/<int:n>')
def hello_6(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def hello_7(n=None):
    result = ""
    if (n % 2) == 0:
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


@app.route('/states_list', strict_slashes=False)
def hello_8():
    states_dict = storage.all(State)
    return render_template('7-states_list.html', states=states_dict.values())


@app.route('/cities_by_states', strict_slashes=False)
def hello_9():
    states_dict = storage.all(State)
    return (render_template('8-cities_by_states.html',
                            states=states_dict.values()))


@app.teardown_appcontext
def close_sql(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
