#!/usr/bin/python3
"""a difintion of the module"""


import json
"""a module to use json"""


def to_json_string(my_obj):
    """a function
    that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
