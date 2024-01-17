#!/usr/bin/python3
"""This module defines a class FileStorage"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ """
        with open(FileStorage.__file_path, 'w') as file:
            data = {}
            data.update(FileStorage.__objects)
            for key, value in data.items():
                data[key] = value.to_dict()
            json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.state import State

        
        cls_name = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'Amenity': Amenity,
            'City': City,
            'Review': Review,
            'State': State
            }
        try:
            data = {}
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    self.all()[key] = cls_name[value['__class__']](**value)
        except FileNotFoundError:
            pass
