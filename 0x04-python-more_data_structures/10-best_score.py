#!/usr/bin/python3
def best_score(a_dictionary):
    best = ""
    j = -1
    if a_dictionary is None:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > j:
            j = a_dictionary[i]
            best = i
    return best
