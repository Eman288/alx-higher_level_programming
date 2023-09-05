#!/usr/bin/python3
"""
a function for division for a matrix
"""
def matrix_divided(matrix, div):
    """
    a function that divide the elements by a value

    matrix => the matrix

    div => the value

    Return =>> a new matrix of divided elements
    """
    if isinstance(matrix, list) != True:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix) == 0 or isinstance(matrix[0], list) != True:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif isinstance(div, (int, float)) != True:
        raise TypeError("div must be a number")
    length = len(matrix[0])
    new_mat = list()
    k = list()
    for i in matrix:
        if isinstance(i, list) != True:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            try:
                k.append(round(j / div, 2))
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")
            except TypeError:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_mat.append(k)
        k = []
    return new_mat
