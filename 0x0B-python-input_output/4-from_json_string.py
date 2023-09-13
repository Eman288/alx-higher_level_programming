#!/usr/bin/python3
"""a definition for the module"""


import json
"""a module to use json"""


def from_json_string(my_str):
    """a function that returns
    an object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
