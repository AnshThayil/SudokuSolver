#Recursive program to solve the sudoku puzzle.
#Function to get the board from the .txt file.
def GetBoard(filename):
    file = open(filename,"r")
    text = file.read()
    board = [[0 for x in range(9)] for x in range(9)]
    x = 0
    y = 0
    for i in text:
        if i != " " and i != "*" and i != "\n":
            board[x][y] = int(i)
            y += 1
            if y > 8:
                x += 1
                y = 0
    return board

#Function to print board.
def printBoard(board):
    print("*********************")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("*********************")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("*", end=" ")
            print(board[x][y], end=" ")
        print()
    print("*********************")

#Function to check if the board is filled up.
def isFull(board):
    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == 0:
                return False
    return True

#Function to find possible entry values for every blank.
#It has to check horizontally, vertically and every 3x3 square.
def PossibleEntries(board,i,j):
    possibilityarray = {}
    for x in range(1,10):
        possibilityarray[x] = 0

    #Checks horizontally.
    for y in range(0,9):
        if not board[i][y] == 0:
            possibilityarray[board[i][y]] = 1

    #Checks vertically.
    for x in range(0,9):
        if not board[x][j] == 0:
            possibilityarray[board[x][j]] = 1

    #Checks 3x3 square.
    #If it's anywhere in a 3x3 square, it'll start from 0,0 for that square.
    k = 0
    l = 0
    if i >= 0 and i <= 2:
        k = 0
    elif i >= 3 and i <= 5:
        k = 3
    else:
        k = 6
    if j >= 0 and j <= 2:
        l = 0
    elif j >= 3 and j <= 5:
        l = 3
    else:
        l = 6

    for x in range (k, k + 3):
        for y in range (l, l + 3):
            if board[x][y] != 0:
                possibilityarray[board[x][y]] = 1

    #Return.
    for x in range(1,10):
        if possibilityarray[x] == 0:
            possibilityarray[x] = x
        else:
            possibilityarray[x] = 0
    return possibilityarray

#Function to solve the puzzle.
def SudokuSolver(board):
    i = 0
    j = 0
    possibilities = {}

    #Check if the board is full.
    if isFull(board):
        print ("Puzzle solved successfully.")
        printBoard(board)
        return
    else:
        #Finding the first vacant spot.
        for x in range(0,9):
            for y in range(0,9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break

        possibilities = PossibleEntries(board,i,j)

        #Recursive bit.
        for x in range(1,10):
            if not possibilities[x] == 0:
                board[i][j] = possibilities[x]
                SudokuSolver(board)
        #Backtrack.
        board[i][j] = 0

#Main.
SudokuBoard = GetBoard("board.txt")
printBoard(SudokuBoard)
print("Solving...")
SudokuSolver(SudokuBoard)
