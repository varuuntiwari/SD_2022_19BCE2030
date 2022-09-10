from tabulate import tabulate

def showBoard(board):
    print(tabulate(board, tablefmt="grid"))

def sweepBoard(board, player):
    for r in board:
        for c in board:
            if board[r][c][0] == player:
                return False
    
    return True