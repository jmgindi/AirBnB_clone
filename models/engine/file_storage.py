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

    def __init__(self):
        self.__class__.__objects = {}

    def all(self):
        return self.__class__.__objects

    def new(self, obj):
        self.__class__.__objects['{}.{}'.format(str(obj), obj.id)] = obj.to_dict()

    def save(self):
        for obj in self.__class__.__objects:
            filename = ""
            filename += self.__class__.__file_path
            filename += '/'
            filename += obj
            try:
                with open(filename, mode="rb+") as file:
                    pass
            except FileNotFoundError:
                with open('{}.py'.format(filename), mode="w") as file:
                    pass


    def reload(self):
        if self.__class__.__objects is not None:
            for obj in self.__class__.__objects:
                filename = ""
                filename += self.__class__.__file_path
                filename += '/'
                filename += obj
                with open(filename, mode="r") as file:
                    return json.load(file)

    @property
    def objects(self):
        return self.__class__.__objects

    @objects.setter
    def objects(self):
        tmp = {}
        self.__class__.__objects = tmp
