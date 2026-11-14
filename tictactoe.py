import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):

    s = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                s.add((i, j))
    return s


def result(board, action):
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError("Move is out of bounds")
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Cell is already taken")
    
    new = copy.deepcopy(board)
    new[action[0]][action[1]] = player(board)
    return new


def winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):

    if winner(board):
        return True
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True


def utility(board):

    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    return 0


def minimax(board):

    if terminal(board):
        return None
    
    turn = player(board)
    
    if turn == "X":
        value = -float("inf")
        best_move = None

        for action in actions(board):
            score = min_value(result(board, action))
            if score > value:
                value = score
                best_move = action
        return best_move
    else:
        value = float("inf")
        best_move = None

        for action in actions(board):
            score = max_value(result(board, action))
            if score < value:
                value = score
                best_move = action
        return best_move


def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = -float("inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
