#!/usr/bin/python3
"""This module contains the FileStorage class
which serializes/deserializes dictionaries/JSON files
"""

from models.base_model import BaseModel
import json

class FileStorage():
    """convert between dictionary string representations of
    objects and JSON files
    """
    __file_path = ""      # path to the JSON file
    __objects = {}        # stores objects by [class].[id]

    def all(self):
        return self.__class__.__objects

    def new(self, obj):
       self.__class__.objects[str(obj)] = '{}.{}'.format(type(obj), obj.id)

    def save(self):
        for obj in self.__class.__objects:
            filename = ""
            filename += self.__class__.__file_path
            filename += '/'
            filename += self.__class__.obj
            with open(filename, mode="w") as file:
                json.dump(filename, file)

    def reload(self):
        for obj in self.__class__.__objects:
            filename = ""
            filename += self.__class__.__file_path
            filename += '/'
            filename += self.__class__.obj
            with open(filename, mode="r") as file:
                return json.load(file) 
