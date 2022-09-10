# Minimalistic Chess
## Completed till level 1
This command line game is made using Python. A 5x5 board is used which has two sides. The players A and B initialize their characters' positions on their respective sides, following which the game starts unless a winner is found.
```python
while(winner == ""):
    chessBoard, winner = makeMove(chessBoard, currentTurn)
    currentTurn = "A" if currentTurn == "B" else "B"
```
# Working
Every move is followed by checking the format of the input, which returns to the user in case of fault.
```python
while(True):
    move = input(f"Player {player}'s turn: ")
    if not re.match(moveMatch, move):
        print("Correct format is (character:move), try again")
    elif move[-1] not in ["F", "B", "L", "R"]:
        print("Not a valid move, try again")
    else:
        break
```

After that, the corresponding piece is searched on the board and if not found, the function `makeMove` is called recursively.
```python
for r in range(5):
    for c in range(5):
        if board[r][c] == move:
            currPos.append(r)
            currPos.append(c)
            break

if currPos == []:
    print("character not found, try again")
    board, res = makeMove(board, player)
```

For level 1, only the Pawn character is used, so the step given by the user is matched using else-if statements.
```python
if step == "L":
    newPos[0] -= 1
elif step == "R":
    newPos[0] += 1
elif step == "B":
    newPos[1] += 1
elif step == "F":
    newPos[1] -= 1
```

The `newPos` is updated accordingly and checked for bounds. If it passes, the position of the character is updated along with checking if any existing character is on the same square. It is then replaced by the new character.
```python
if newPos[0] not in range(0, 5) or newPos[1] not in range(0, 5):
    print("move out of bounds, try again")
    board, res = makeMove(board, player)
else:
    board[currPos[0]][currPos[1]] = "-"
    if board[newPos[0]][newPos[1]] != "-":
        print(board[newPos[0]][newPos[1]], " eliminated")
    board[newPos[0]][newPos[1]] = move
```