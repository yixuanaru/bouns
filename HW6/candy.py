import numpy as np

def read_board(filename):
    with open(filename, 'r') as file:
        board = eval(file.read())
    return board

def write_board(filename, board):
    with open(filename, 'w') as file:
        file.write(str(board))

def crush_candies(board):
    rows, cols = len(board), len(board[0])
    stable = False
    while not stable:
        stable = True
        crush = set()
        
        # Mark candies to crush horizontally
        for r in range(rows):
            for c in range(cols - 2):
                if board[r][c] and board[r][c] == board[r][c+1] == board[r][c+2]:
                    stable = False
                    crush.update({(r, c), (r, c+1), (r, c+2)})
                    
        # Mark candies to crush vertically
        for r in range(rows - 2):
            for c in range(cols):
                if board[r][c] and board[r][c] == board[r+1][c] == board[r+2][c]:
                    stable = False
                    crush.update({(r, c), (r+1, c), (r+2, c)})
                    
        # Crush marked candies
        for r, c in crush:
            board[r][c] = 0
            
        # Drop candies
        for c in range(cols):
            write_idx = rows - 1
            for r in range(rows - 1, -
