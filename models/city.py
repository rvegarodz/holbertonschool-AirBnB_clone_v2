#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
>>>>>>> e323df1bb25f5b63fff9976b6c4cd228ac430f1f

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
<<<<<<< HEAD
    state_id = Column(String(60), ForeignKey(State.id))
    name = Column(String(128))

places = relationship("Place", cascade="delete", backref="cities")
=======
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
>>>>>>> e323df1bb25f5b63fff9976b6c4cd228ac430f1f
