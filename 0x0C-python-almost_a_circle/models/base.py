#!/usr/bin/python3
"""the module for the base class"""


import json
"""the json module"""


class Base:
    """the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """a function to set the id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a function writes the JSON strin
        representation of list_objs to a file"""
        name = cls.__name__ + ".json"
        li = list()
        with open(name, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for i in list_objs:
                    li.append(i.to_dictionary())
                f.write(Base.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            ins = cls(1, 1)
        else:
            ins = cls(1)
        ins.update(**dictionary)
        return ins
