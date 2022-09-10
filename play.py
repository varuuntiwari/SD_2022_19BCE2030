import inquirer
from boardFunc import *

chessBoard = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-']
    ]

Characters = {
    "P": "Pawn, capable of moving L, R, F, B"
}

def Welcome():
    print("+-------------------------------+")
    print("| Welcome to Minimalistic Chess |")
    print("+-------------------------------+\n")
    print("Characters available are:")
    print("-------------------------")
    for name, info in Characters.items():
        print(name, " | ", info)
    print()
    
    print("\nEnter the character positions in the format {(character_name)(character_number)}, for example {P2}\n")

def initBoard(board):
    print("1st player\nEnter 5 characters' positions in a line(left to right):")
    checkInput = [x for x in input().split()]
    if len(checkInput) == 5:
        board[0] = checkInput
    
    print("2nd player\nEnter 5 characters' positions in a line(left to right):")
    checkInput = [x for x in input().split()]
    if len(checkInput) == 5:
        board[4] = checkInput

if __name__ == "__main__":
    Welcome()
    initBoard(chessBoard)
    showBoard(chessBoard)