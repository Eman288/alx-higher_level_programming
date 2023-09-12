#!/usr/bin/python3
"""defintion of the module"""


def append_write(filename="", text=""):
    """a function that append a string to a file"""
    with open(filename, 'a', encoding='utf-8') as file1:
        return file1.write(text)
