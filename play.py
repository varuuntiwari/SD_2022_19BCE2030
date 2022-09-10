import re
from boardFunc import showBoard
from playerFunc import makeMove

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

def initBoard():
    global chessBoard
    # Taking input of Player A
    print("Player A, enter 5 characters' positions in a line(left to right):")
    checkInput = [x for x in input().split()]
    if len(checkInput) == 5:
        chessBoard[0] = ["A-"+s for s in checkInput]
    
    # Taking input of Player B
    print("Player B, enter 5 characters' positions in a line(left to right):")
    checkInput = [x for x in input().split()]
    if len(checkInput) == 5:
        chessBoard[4] = ["B-"+s for s in checkInput]


if __name__ == "__main__":
    Welcome()
    initBoard()
    showBoard(chessBoard)
    winner = ""
    currentTurn = "A"
    while(winner == ""):
        # Prompt the user for a move
        chessBoard, winner = makeMove(chessBoard, currentTurn)
        # Pass the move to other player
        currentTurn = "A" if currentTurn == "B" else "B"
    
    print(f"The winner is {winner}") 