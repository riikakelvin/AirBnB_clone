#!/usr/bin/python3

"""
File storage class for storing objects in JSON format.
"""

import datetime
import os
import json


class FileStorage:
    """
    A class that serializes instances to a JSON file and deserializes JSON
    file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the obj in __objects with key <obj class name>.id

        Args:
            obj (BaseModel): The object to set in __objects.
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        file_path = FileStorage.__file_path
        obj = {key: value.to_dict()
               for key, value in FileStorage.__objects.items()}
        with open(file_path, "w", encoding="utf-8") as obj_file:
            json.dump(obj, obj_file)

    def classes(self):
        """
        Retrieve a dictionary mapping valid class names
        to their corresponding class references.

        Returns:
            dict: A dictionary containing the valid classes
            and their references
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """
        Deserializes the JSON file into __objects.

        This method reads the JSON file, deserializes its contents, and
        assigns the loaded objects to the __objects dictionary.

        If the JSON file does not exist, is empty, or an error occurs during
        deserialization, this method does nothing.

        Returns:
            None
        """
        if not os.path.isfile(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {
                    k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_dict.items()
                }
                FileStorage.__objects = obj_dict
        except json.JSONDecodeError:
            # Handles when the JSON file is empty or contains invalid data
            print("Error: Invalid JSON data. File will be recreated.")
            FileStorage.__objects = {}

    def to_dict(self):
        """
        Serializes the objects(JSON data in this case) in storage
        to a dictionary.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def from_dict(self, obj_dict):
        """
        Deserializes the dictionary into objects in storage.
        """
        class_dict = self.classes()
        for key, value in obj_dict.items():
            class_name = value['__class__']
            if class_name in class_dict:
                cls = cls_dict[class_name]
                obj = cls(**value)
                FileStorage.__objects[key] = obj

    def attributes(self):
        """
        Returns the valid attributes and their types for classname.
        """
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes
