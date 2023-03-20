#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        all_fltr = {}
        classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
        if cls != None:
            for classs in classes:
                test = str(cls).rfind(classs)
                if test != -1:
                    cls_cln = str(cls)[test:-2]
            if cls_cln != None:
                for k_obj, v_obj in FileStorage.__objects.items():
                    if k_obj.rfind(cls_cln) != -1:
                        all_fltr.update({k_obj:v_obj})
                return all_fltr
        else:
            return FileStorage.__objects
    
    def delete(self, obj=None):
        """Delete obj from storage dictionary"""
        if obj != None:
            obj_key = obj.__class__.__name__ + "." + obj.id
            all_objs = self.all()
            del all_objs[obj_key]
            self.save()

    
    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
