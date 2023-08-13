#!/usr/bin/python3

"""
This module defines the BaseModel class, which serves
as the base class for all models in the application.
"""

import uuid

from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class that defines common attributes and methods for
    other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Tuple of arguments
            **kwargs: Dictionary of key-value arguments.
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Retrieves an informal string representation of the BaseModel object.

        Return:
        A string in the format: "[class name] (id) {attribute dictionary}"
        """
        class_name = self.__class__.__name__
        attributes = self.__dict__.copy()
        attributes.pop('_sa_instance_state', None)
        return "[{}] ({}) {}".format(class_name, self.id, attributes)

    def save(self):
        """
        Update the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the instance attribute to a dictionary.

        Returns:
            A dictionary that  contains all instance attributes, including
            the class name, creation datetime, and update datetime.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
