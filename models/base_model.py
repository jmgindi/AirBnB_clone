#!/usr/bin/python3
"""This module contains the Base class for 
all classes in the Holberton BnB Project
"""

import datetime
import uuid

class BaseModel():
    """Base class for Holberton BnB project
    """
    nb_objects = 0

    def __init__(self):
        if id is not None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            self.__class__.nb_objects += 1

    def __del__(self):
        self.__class__.nb_objects -= 1
        del(self)

    def __str__(self):
        obj_str = ''
        obj_str += '[<{}>] '.format(self.__class__.__name__)
        obj_str += '(<{}>) '.format(self.id)
        obj_str += '<{}>'.format(self.__dict__)
        return obj_str

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.__dict__['created_at'] = datetime.date.isoformat(self.created_at)
        self.__dict__['updated_at'] = datetime.date.isoformat(self.updated_at)
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
        

