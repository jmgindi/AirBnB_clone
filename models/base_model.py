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

    def __init__(self, *args, **kwargs):
        """Initializes the Base Model
        Args:
            args: args
            kwargs: Dictionary of object attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        if kwargs is not None:
            for key, dt_str in kwargs.items():
                if key == "id":
                    self.id = dt_str
                if key == "created_at":
                    dt, _, us = dt_str.partition(".")
                    dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
                    us = int(us.rstrip("Z"), 10)
                    self.created_at = dt + datetime.timedelta(microseconds=us)
                if key == "updated_at":
                    dt, _, us = dt_str.partition(".")
                    dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
                    us = int(us.rstrip("Z"), 10)
                    self.updated_at = dt + datetime.timedelta(microseconds=us)

    def __del__(self):
        """Deletes object"""
        del(self)

    def __str__(self):
        """Returns string repr of obj"""
        obj_str = ''
        obj_str += '[{}] '.format(self.__class__.__name__)
        obj_str += '({}) '.format(self.id)
        obj_str += '{}'.format(self.__dict__)
        return obj_str

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts obj to dict
        Return:
            Dict of all obj attributes
        """
        if type(self.created_at) is not str:
            self.__dict__['created_at'] = self.created_at.isoformat()
        if type(self.updated_at) is not str:
            self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
