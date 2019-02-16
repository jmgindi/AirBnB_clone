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

    def reload(self):

    @property
    def objects(self):
        return self.__class__.__objects

    @objects.setter
    def objects(self):
        tmp = {}
        self.__class__.__objects = tmp
