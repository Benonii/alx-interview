#!/usr/bin/python3

""" A recursive solution to pascal's triangle """


def pascal_triangle(n):
    """ Returns a list of lists of pascal's triangle upto n rows """

    if n <= 0:
        return []
    p_triangle = create_p_triangle_recursively([], n)

    return p_triangle


def create_p_triangle_recursively(p_triangle, n):
    """ Creates the rows recursively """

    if n == 1:
        return [[1]]
    p_triangle = create_p_triangle_recursively(p_triangle, n - 1)

    prev_row = p_triangle[len(p_triangle) - 1]
    row, col = [], 0

    while (col < n):
        if col == 0:
            row.append(1)
            col += 1
            continue
        elif col == n - 1:
            row.append(1)
            break
        # Calculate the value of the column and append it to row
        col_value = prev_row[col - 1] + prev_row[col]
        row.append(col_value)
        col += 1

    p_triangle.append(row)
    return p_triangle
