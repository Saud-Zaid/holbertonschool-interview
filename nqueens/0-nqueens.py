#!/usr/bin/python3
"""
0-nqueens module
Solves the N queens puzzle using backtracking.
"""
import sys


def solve_nqueens(n):
    """
    Solves the N queens puzzle and prints every solution.

    Args:
        n (int): The size of the chessboard and number of queens.
    """
    queens = []
    cols = set()
    pos_diag = set()
    neg_diag = set()

    def backtrack(row):
        """Backtracking helper function to place queens row by row."""
        if row == n:
            print(queens)
            return

        for col in range(n):
            if (col in cols or (row + col) in pos_diag or
                    (row - col) in neg_diag):
                continue
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            queens.append([row, col])

            backtrack(row + 1)

            queens.pop()
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    backtrack(0)


def main():
    """
    Validates command-line arguments and initiates N queens solver.
    """
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

    solve_nqueens(n)


if __name__ == "__main__":
    main()
