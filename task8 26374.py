# Python3 program to solve N Queen Problem using backtracking
N = 4  # You can change this value to explore other board sizes

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()  # Newline between solutions

def isSafe(board, row, col):
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, solutions):
    # Base case: All queens are placed
    if col >= N:
        solutions.append([row[:] for row in board])  # Deep copy
        return

    # Try placing a queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place queen
            solveNQUtil(board, col + 1, solutions)
            board[i][col] = 0  # BACKTRACK

def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solveNQUtil(board, 0, solutions)

    if not solutions:
        print("No solutions exist.")
    else:
        print(f"Total solutions for N = {N}: {len(solutions)}\n")
        for idx, sol in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            printSolution(sol)

# Driver Code
if __name__ == '__main__':
    solveNQ()
