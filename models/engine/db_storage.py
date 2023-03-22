#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import os

class DBStorage():
    """DOCUMENT"""
    __engine = None
    __session = None

    def __init__(self):
        """DOCUMENTATION"""
        db_api = 'mysql+mysqldb://{}:{}@{}/{}'
        usr = os.environ.get('HBNB_MYSQL_USER')
        pswd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(db_api.format(usr, pswd, host, db), pool_pre_ping=True)
        
    
    def all(self, cls=None):
        """Documentation"""
        all_list = {}
        classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        cls_lst = [BaseModel, User, Place, State, City, Amenity, Review]
        if cls != None:
            query = self.__session.query(classes[cls]).all()
            for obj in query:
                obj_id = obj.id
                obj_key = '{}.{}'.format(cls, obj_id)
                all_list.update({obj_key: obj})
        else:
            query = self.__session.query(City, State).filter(City.state_id == State.id).all()
            for objs in query:
                for obj in objs:
                    obj_id = obj.id
                    obj_key = '{}.{}'.format(cls, obj_id)
                    all_list.update({obj_key: obj})
        return all_list
    
    def new(self, obj):
        """DOCUMENTATION"""
        if obj != None:
            self.__session.add(obj)

    def save(self):
        """DOCUMENTATION"""
        self.__session.commit()

    def delete(self, obj=None):
        """DOCUMENTATION"""
        if obj != None:
            results = self.__session.query(State, City).all()
            for row in results:
                if obj == row:
                    self.__session.delete(row)
                    break
            self.save()

    def reload(self):
        """DOCUMENTATION"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()