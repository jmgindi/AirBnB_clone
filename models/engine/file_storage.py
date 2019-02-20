#!/usr/bin/python3
"""This module contains the FileStorage class
which serializes/deserializes dictionaries/JSON files
"""

from models.base_model import BaseModel
# import models
import json
import os


class FileStorage():
    """convert between dictionary string representations of
    objects and JSON files
    Attributes
        file_path: json file to store json formatted objs in
        objects: Dict of objs by [class].[id]
    """
    __file_path = str(os.getcwd()) + "/file.json"      # path to the JSON file
    __objects = {}        # stores objects by [class].[id]
    __allowed = {"BaseModel" : BaseModel}

    def __init__(self):
        """Initializes file storage class"""
        self.__class__.__objects = {}

    def all(self):
        """Returns list of all objects in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets a new object's key and value in __objects"""
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Saves objects to file"""
        with open(FileStorage.__file_path, mode="w") as fp:
            json.dump({k:v.to_dict() for k, v in FileStorage.__objects.items()}, fp)

    def reload(self):
        """Reloads file from disk"""
        try:
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
        except FileNotFoundError:
            return
        for k, v in data.items():
            tmp = k.split(".")
            class_name = tmp[0]
            FileStorage.__objects[k] = FileStorage.__allowed[class_name](v)

    @property
    def objects(self):
        """objects getter"""
        return self.__class__.__objects

    @objects.setter
    def objects(self):
        """objects getter"""
        tmp = {}
        self.__class__.__objects = tmp
