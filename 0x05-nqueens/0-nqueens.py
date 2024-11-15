#!/usr/bin/python3
"""N queens puzzle"""

import sys


def isSafe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[i] == row or \
           board[i] == row - col + i or \
           board[i] == row + col - i:
            return False
    return True


def solveNQUtil(board, col):
    """Use backtracking to solve the N queens puzzle"""
    n = len(board)
    if col == n:
        print(str([[i, board[i]] for i in range(n)]))
        return
    for i in range(n):
        if isSafe(board, i, col):
            board[col] = i
            solveNQUtil(board, col + 1)


def nqueens(n):
    """Initialize the board and call solveNQUtil()"""
    board = [-1 for _ in range(n)]
    solveNQUtil(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n)
