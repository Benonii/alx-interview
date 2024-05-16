#!/usr/bin/python3

''' The Nqueens problem '''

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def solve_n_queens(n):
    ''' Solves the nqueens problem '''
    col = set()
    ltr_diagonal = set()
    rtl_diagonal = set()

    result = []
    sol_set = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        '''Recursively apply backtracking to solve the problem'''
        if r == n:
            solution = ["".join(row) for row in board]
            result.append(solution)
            return

        for c in range(n):
            if c in col or (r + c) in rtl_diagonal or (r - c) in ltr_diagonal:
                continue

            col.add(c)
            rtl_diagonal.add(r + c)
            ltr_diagonal.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)

            col.remove(c)
            rtl_diagonal.remove(r + c)
            ltr_diagonal.remove(r - c)
            board[r][c] = "."

        # print(board)
    backtrack(0)
    for i in range(len(result)):
        solution = result[i]
        sol_arr = []
        for j in range(len(solution)):
            row = solution[j]
            for k in range(len(row)):
                if solution[j][k] == "Q":
                    sol_arr.append([j, k])
        sol_set.append(sol_arr)
    for solution in sol_set:
        print(solution)


solve_n_queens(N)
