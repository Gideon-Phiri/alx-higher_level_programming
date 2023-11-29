import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_invalid_number_and_exit():
    print("N must be an integer")
    sys.exit(1)

def print_minimum_value_and_exit():
    print("N must be at least 4")
    sys.exit(1)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in board]

def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    if 'Q' in board[row]:
        return False

    # Check if there is a queen in the same column
    if any(board[i][col] == 'Q' for i in range(n)):
        return False

    # Check if there is a queen in the diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_queens(board, row, n, solutions):
    if row == n:
        # If all queens are placed, add the solution to the list
        solutions.append(board_deepcopy(board))
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_queens(board, row + 1, n, solutions)
            board[row][col] = ' '  # backtrack

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    n = sys.argv[1]

    if not is_integer(n):
        print_invalid_number_and_exit()

    n = int(n)

    if n < 4:
        print_minimum_value_and_exit()

    board = init_board(n)
    solutions = []

    solve_queens(board, 0, n, solutions)

    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()