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
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        from models.base_model import BaseModel
        """deserializes the JSON file to __objects"""
        cls_name = {'BaseModel': BaseModel}
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    self.__objects[key] = cls_name[value['__class__']](**value)
        except FileNotFoundError:
            pass
