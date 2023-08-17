#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda a: a * a, x)) for x in matrix]
