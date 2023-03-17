#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """ Rotates a n x n matrix by 90 degrees """
    import copy
    matcopy = copy.deepcopy(matrix)
    fwd = 0
    current = 0
    revrs = len(matrix) - 1
    for start in range(len(matrix)):
        while fwd < len(matrix):
            matrix[start][fwd] = matcopy[revrs][current]
            revrs -= 1
            fwd += 1
        current += 1
        fwd = 0
        revrs = len(matrix) - 1
