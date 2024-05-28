#!/usr/bin/python3

''' Contains th function rotate_2d_matrix()'''


def rotate_2d_matrix(matrix):
    ''' Rotates a 2D n x n matrix(list of lists) 90 degrees clockwise '''
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        temp = row[0]
        row[0] = row[n - 1]
        row[n - 1] = temp
