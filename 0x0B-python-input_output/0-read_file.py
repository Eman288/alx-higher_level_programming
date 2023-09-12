#!/usr/bin/python3
"""a difinition for the function"""


def read_file(filename=""):
    """ a function that reads and print a text from a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
