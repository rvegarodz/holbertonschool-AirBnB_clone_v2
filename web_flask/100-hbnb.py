#!/usr/bin/python3
"""Script that starts a Flask Web app for my HBNB clone project"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def places():
    """Method that route to /hbnb"""
    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()
    all_places = storage.all(Place).values()
    all_users = storage.all(User).values()
    return (render_template('100-hbnb.html',
                            all_states=all_states,
                            all_amenities=all_amenities,
                            all_places=all_places,
                            all_users=all_users))


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Method that remove current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
