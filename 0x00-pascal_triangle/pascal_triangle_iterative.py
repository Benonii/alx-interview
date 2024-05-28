#!/usr/bin/python3

""" Itreative solution to creating pascal's triangele """


def pascal_triangle(n):
    """ Creates a list of lists representing pascal's triangle """
    pt_triangle = []
    row_idx = 0

    while (row_idx < n):
        pt_row = []
        if (row_idx == 0):
            row_idx += 1
            pt_triangle.append([1])
            continue
        prev_row = pt_triangle[len(pt_triangle) - 1]
        col_idx = 0
        while (col_idx <= row_idx):
            # print(col_idx, row_idx)
            if col_idx == 0:
                pt_row.append(1)
                col_idx+= 1
                continue
            elif col_idx == row_idx:
                pt_row.append(1)
                break
            col_value = prev_row[col_idx - 1] + prev_row[col_idx]
            pt_row.append(col_value)
            col_idx += 1

        pt_triangle.append(pt_row)
        row_idx += 1

    return pt_triangle
