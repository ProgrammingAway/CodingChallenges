# Tic Tac Toe Programming Challenge Updated

Shortly after writing a [Tic Tac Toe program](https://programmingaway.com/tic-tac-toe-challenge) in python for one of my programming challenges, I ran across a new Tic Tac Toe programming challenge from [Robert Heaton](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/).  While looking through his challenge, I decided my program was too simple and needed to be updated with better written functions.  The functions in my original Tic Tac Toe program were hardcoded in some ways and needed to be more abstracted.  Functions need to do just one thing and need to be able to accomodate potential changes in the future without re-writing the function.

So the first thing I did was make the game board size a variable that can be controlled by the user.  Now we aren't stuck with a 3x3 board, however, this would require us to re-write most of the functions since they were hardcoded to use a 3x3 board.  The first thing I needed to do is to create a initializeBoard function that created a 2 dimensional array based off the boardSize variable.

<code>
def initializeBoard(boardSize):
    # Creates a 2 dimentional martix of boardSize
    board = []
    for x in range(boardSize):
        column = []
        for y in range(boardSize):
            column.append(None)
        board.append(column)
    return board
</code>

The next thing I did was update the printBoard function to use this new board.  

<code>
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
</code>

I will have to put some practical limit on the board size to keep the game managable, but I wanted the printBoard function to be able to hangle a large size board.  I added conditionals that tested if there are more than 10 or 100 positions on the board so I can add proper spacing and everything would line up.  But I did think testing anything bigger than that would make the board too big and make the game too hard to play.  However, I may be able to accomplish this by using some print formatting.  I will look into that.

I could have used the same method of checking for a draw as my old program, but I decided to give it it's dedicated function and actually test for any empty spaces on the board.  Hopefully this is more robust.

<code>
def checkForDraw(board):
    # Checks to see if there are any empty spaces on the board
    # If not, it is a draw
    for row in board:
        for col in row:
            if col is None:
                return False
    return True
</code>




