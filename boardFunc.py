from tabulate import tabulate

def showBoard(board):
    print(tabulate(board, tablefmt="grid"))