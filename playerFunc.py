from boardFunc import sweepBoard, showBoard
import re

# Regular expression for move format
moveMatch = re.compile("^[A-Za-z]{1}[1-5]{1}:(F, B, L, R)$")

def makeMove(board, player):
    # Assign opposition
    opposition = "A" if player == "B" else "B"
    res = ""

    # Get move in correct format
    while(True):
        move = input(f"Player {player}'s turn: ")
        if not re.match(moveMatch, move):
            print("Correct format is (character:move), try again")
        elif move[-1] not in ["F", "B", "L", "R"]:
            print("Not a valid move, try again")
        else:
            break
    
    character, step = re.split(":", move)
    currPos = []
    move = player + "-" + character
    for r in range(5):
        for c in range(5):
            if board[r][c] == move:
                currPos.append(r)
                currPos.append(c)
                break
    
    
    newPos = currPos
    if currPos == []:
        print("character not found, try again")
        board, res = makeMove(board, player)
    else:
        if step == "L":
            newPos[0] -= 1
        elif step == "R":
            newPos[0] += 1
        elif step == "B":
            newPos[1] += 1
        elif step == "F":
            newPos[1] -= 1
        else:
            print("step not found, try again")
            board, res = makeMove(board, player)

    if newPos[0] not in range(0, 5) or newPos[1] not in range(0, 5):
        print("move out of bounds, try again")
        board, res = makeMove(board, player)
    else:
        board[currPos[0]][currPos[1]] = "-"
        if board[newPos[0]][newPos[1]] != "-":
            print(board[newPos[0]][newPos[1]], " eliminated")
        board[newPos[0]][newPos[1]] = move
    
    showBoard(board)

    if sweepBoard(board, opposition):
        res = player

    return board, res