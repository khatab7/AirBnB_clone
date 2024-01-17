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

    def update(self, obj_id, attr_key, attr_value):
        try:
            attr_value = self.__clean_quotes(attr_value)
            if attr_key not in ["id", "created_at", "updated_at"]:
                self.__objects[f'{obj_id}'].__dict__[
                    f'{attr_key}'] = attr_value
                self.save()
                return True
            else:
                return False
        except KeyError:
            return False

    def __clean_quotes(self, to_clean):
        clean_attr_value = to_clean.split("\"")
        if len(clean_attr_value) > 1:
            return clean_attr_value[1]
        else:
            return clean_attr_value[0]

    def remove(self, obj_id):
        '''Public instance method to delete a
         certain element from the dictionary'''
        try:
            del self.__objects[f'{obj_id}']
            self.save()
            return True
        except KeyError:
            return False

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
