#!/usr/bin/python3
"""Script that starts a Flask Web app for my HBNB clone project"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Method that route to /hbnb_filters"""
    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()
    return (render_template('10-hbnb_filters.html',
                            all_states=all_states,
                            all_amenities=all_amenities))


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Method that remove current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
