# Tic Tac Toe
# Build a game of Tic Tac Toe. I would suggest you start off building a two player version then if
# you want a little extra challenge see if you can build a version where you get to challenge the
# computer. (from https://ryanstutorials.net/programming-challenges/)

play = input("Would you like to play Tic Tac Toe? (Y/N) ")

if "y" not in play.lower():
    print("Ok, bye!")
    exit(1)

# Game Board:
#
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
winningSequences = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2],
                    [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])


def printBoard():
    # Prints the current state of the board
    print()
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("---------")
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("---------")
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))
    print()


def checkForWin(count):
    # Checks the board for a winning sequence
    # Also checks if there are no more moves and calls a draw
    if count == 8:
        printBoard()
        print("The game is a draw!")
        return 2
    for sequence in winningSequences:
        if board[sequence[0]] == board[sequence[1]] == board[sequence[2]]:
            printBoard()
            if board[sequence[0]] == "X":
                print("Player 'X' won!!")
            if board[sequence[0]] == "O":
                print("Player 'O' won!!")
            return 1
    return 0


def playGame():
    # while there is not a win or draw, then ask the player for the next move
    win = 0
    count = 0
    while win == 0:  # =1 for win, =2 for draw, =0 to continue play
        printBoard()
        if count % 2 == 0:  # Even count is player X
            player = "X"
        else:  # Odd count is player O
            player = "O"
        move = int(input("Player " + player +
                   ": Enter number of space you want to place your piece: "))
        while move not in range(9) or board[move] != move:
            move = int(input("Please pick an unused space between 0 and 8: "))
        board[move] = player
        win = checkForWin(count)
        count = count + 1


while "y" in play.lower():
    playGame()
    play = input("Would you like to play again? (Y/N) ")
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print("Thanks for playing")
