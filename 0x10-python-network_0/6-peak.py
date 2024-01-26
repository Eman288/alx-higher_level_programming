#!/usr/bin/python3
"""a module"""


def find_peak(list_of_integers):
    """a function to find the peak"""
    if list_of_integers is None:
        return None
    else:
        p = 0
        n = 0
        j = 0
        for i in range(0, len(list_of_integers)):
            if i != 0:
                if list_of_integers[i] >= list_of_integers[i - 1]:
                    if list_of_integers[i] >= list_of_integers[i + 1]:
                        return list_of_integers[i]
            elif i != len(list_of_integers) - 1:
                if list_of_integers[i] >= list_of_integers[i + 1]:
                    return list_of_integers[i]
            else:
                return list_of_integers[i]
