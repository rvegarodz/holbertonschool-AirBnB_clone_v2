#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=False)
    last_name = Column('last_name', String(128), nullable=False)

    places = relationship("Place", cascade="delete", backref="cities")
