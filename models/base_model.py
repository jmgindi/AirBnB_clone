#!/usr/bin/python3
"""This module contains the Base class for 
all classes in the Holberton BnB Project
"""

import datetime
import models
import uuid

class BaseModel():
    """Base class for Holberton BnB project
    """
    nb_objects = 0
    y = []

    def __init__(self, *args, **kwargs):
        storage.new(self)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.__class__.nb_objects += 1
        if kwargs is not None:
            for key, dt_str in kwargs.items():
                if key == "id":
                    self.id = dt_str
                if key == "created_at":
                    dt, _, us= dt_str.partition(".")
                    dt= datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
                    us= int(us.rstrip("Z"), 10)
                    self.created_at = dt + datetime.timedelta(microseconds=us)
                if key == "updated_at":
                    dt, _, us= dt_str.partition(".")
                    dt= datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
                    us= int(us.rstrip("Z"), 10)
                    self.updated_at = dt + datetime.timedelta(microseconds=us)
                self.y.append(key)
                self.y.append(dt_str)

    def __del__(self):
        self.__class__.nb_objects -= 1
        del(self)

    def __str__(self):
        obj_str = ''
        obj_str += '[{}] '.format(self.__class__.__name__)
        obj_str += '({}) '.format(self.id)
        obj_str += '{}'.format(self.__dict__)
        return obj_str

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save(self)

    def to_dict(self):
        if type(self.created_at) is not str:
            self.__dict__['created_at'] = self.created_at.isoformat()
        if type(self.updated_at) is not str:
            self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
        

