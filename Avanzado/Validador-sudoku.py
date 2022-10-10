from collections import Counter
import numpy as np

def valid_solution(board):
    print(board)
    board = np.asarray(board)
    if board.min() <= 0:
        return False
    for i in board:
        fila = Counter(i)
        if max(fila.values()) > 1:
            return False
    board = np.transpose(board)
    for i in board:
        col = Counter(i)
        if max(col.values()) > 1:
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            sub = board[i:i+3,j:j+3].flatten()
            cuad = Counter(sub)
            if max(cuad.values()) > 1:
                return False
    return True