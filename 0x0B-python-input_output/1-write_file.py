#!/usr/bin/python3
"""difintion of the module"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file1:
        return file1.write(text)
