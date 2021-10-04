# Tic Tac Toe V2
# Another attempt at a Tic Tac Toe program challenge
# (from https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/)


def initializeBoard(boardSize):
    # Creates a 2 dimentional martix of boardSize
    board = []
    for x in range(boardSize):
        column = []
        for y in range(boardSize):
            column.append(None)
        board.append(column)
    return board


def printBoard(board):
    # Prints the current state of the board
    rowIndex = 0
    positionIndex = 0
    print()
    for row in board:
        boardRow1 = " | "
        boardRow2 = "---"
        for col in row:
            if col is None:
                if positionIndex < 10:
                    boardRow1 += " "
                if positionIndex < 100:
                    boardRow1 += " "
                boardRow1 += str(positionIndex)
                boardRow2 += "---"
            else:
                boardRow1 = boardRow1 + " " + col + " "
                boardRow2 += "---"
            boardRow1 += " | "
            boardRow2 += "---"
            positionIndex += 1
        if rowIndex == 0:
            print(boardRow2)
        print(boardRow1)
        print(boardRow2)
        rowIndex += 1
    print()


def checkForWin(board, winningSequencesList):
    # Check if either player has won the game
    for seq in winningSequencesList:
        boardValues = []
        for (x, y) in seq:
            boardValues.append(board[x][y])
        if len(set(boardValues)) == 1 and boardValues[0] is not None:
            return True
    return False


def winningSequences(boardSize):
    # Return all the sequences that can win the game
    colSequences = []
    rowSequences = []
    for a in range(boardSize):
        col = []
        row = []
        for b in range(boardSize):
            col.append((a, b))
            row.append((b, a))
        colSequences.append(col)
        rowSequences.append(row)

    diagSequences = []
    diag1 = []
    diag2 = []
    for x in range(boardSize):
        diag1.append((x, x))
        diag2.append((x, boardSize-1-x))
    diagSequences.append(diag1)
    diagSequences.append(diag2)

    return colSequences + rowSequences + diagSequences


def checkForDraw(board):
    # Checks to see if there are any empty spaces on the board
    # If not, it is a draw
    for row in board:
        for col in row:
            if col is None:
                return False
    return True


def get_move(board, player):
    boardSize = len(board)
    boardRange = boardSize * boardSize
    while True:
        answer = input(
            "Please pick an unused space between 0 and " + str(boardRange-1) + ": ")
        if answer.isdigit():
            move = int(answer)
            row = int(move / boardSize)
            col = int(move % boardSize)
            if move in range(boardRange) and board[row][col] == None:
                break
            elif move not in range(boardRange):
                print("Choose a valid space.")
            else:
                print("Choose an unused space.")
        else:
            print("Please enter a valid number.")
    return (row, col)


def playGame(board, winningSequencesList):
    # while there is not a win or draw, then ask the player for the next move
    win = 0
    draw = 0
    count = 0
    while win == 0 and draw == 0:  # =1 for win, =2 for draw, =0 to continue play
        printBoard(board)
        if count % 2 == 0:  # Even count is player X
            player = "X"
        else:  # Odd count is player O
            player = "O"
        move = get_move(board, player)
        board[move[0]][move[1]] = player
        draw = checkForDraw(board)
        win = checkForWin(board, winningSequencesList)
        count = count + 1
    printBoard(board)
    if draw:
        print("The game is a draw!")
    if win:
        print("Player " + player + " won!")


play = input("Would you like to play Tic Tac Toe? (Y/N) ")

if "y" not in play.lower():
    print("Ok, bye!")
    exit(1)

while "y" in play.lower():
    boardSize = int(input("What size board do you want to play with? "))
    board = initializeBoard(boardSize)
    winningSequencesList = winningSequences(boardSize)
    playGame(board, winningSequencesList)
    play = input("Would you like to play again? (Y/N) ")

print("Thanks for playing")
