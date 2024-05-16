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


def queens_attack(board, pos_x, pos_y):
    """ Checks if a queen is placed in the crossfire of another queen's attack
        path """
    
    # Vertical check
    sum_of_queens = 0
    for i in range(N):
        sum_of_queens += board[i][pos_y]
        if sum_of_queens > 1:
            return True
    print("Vertically okay")

     # Horizontal check
    sum_of_queens = 0
    for j in range(N):
        sum_of_queens += board[pos_x][j]
        if sum_of_queens >= 1:
            return True
    print("Horizontally okay")

    # LTR Diagonal check
    sum_of_queens = 0
    if pos_x >= pos_y:
        diagonal_start = pos_x - pos_y
        upper_bound = N - diagonal_start
        lower_bound = 0
    else:
        diagonal_start = 0
        upper_bound = N - (pos_y - pos_x) + 1
        lower_bound = pos_y - pos_x

    i = diagonal_start
    for j in range(lower_bound, upper_bound):
        sum_of_queens += board[i][j]
        if sum_of_queens > 1:
            return True
        i += 1
    print("LTR okay")

    # RTL Diagonal check
    sum_of_queens = 0
    if pos_x + pos_y > 3:
        diagonal_start = pos_x + pos_y - 3
        upper_bound = N - diagonal_start
        lower_bound = 0
    else:
        diagonal_start = 0
        upper_bound = N - (N - (pos_x + pos_y))
        lower_bound = -1

    i = diagonal_start
    for j in range(upper_bound, lower_bound, -1):
        sum_of_queens += board[i][j]
        if sum_of_queens > 1:
            return True
        i += 1
    print("No attacking queens")
    return False


board = []
for r in range(N):
    row = []
    for col in range(N):
        row.append(0)
    board.append(row)

solutions = []
safe = []

def backtrack(board, x):
    ''' Goes back to the previous one on board and moves it to the left '''
    for pos_y in range(N):
        if board[x][pos_y] == 1:
            board[x][pos_y] = 0
            if pos_y < N - 1:
                board[x][pos_y + 1] = 1
                return
            else:
                backtrack(board, x - 1)


def no_queens_attack(board, pos_x, pos_y):
    '''  Solves the NQueens problem with Recursion and backtracking '''
    if pos_x == N:
        solutions.append(safe)
        return

    for y in range(pos_y, len(board[pos_x])):
        board[pos_x][y] = 1
        for row in board:
            print(row)
        print()
        if queens_attack(board, pos_x, y) == True:
            board[pos_x][y] = 0
            if [pos_x, y] in safe:
                safe.remove([pos_x, y])
            if (y == N - 1):
                backtrack(board, pos_x - 1)
        else:
            safe.append([pos_x, y])
            no_queens_attack(board, pos_x + 1, 0)

    return

no_queens_attack(board, 0, 0)
for row in solutions:
    print(row)
