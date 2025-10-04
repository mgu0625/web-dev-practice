# to generate random choice for CPU
import random

# for description at top
print("Welcome to Tic Tac Toe!")
print("DESCRIPTION: This is a small Python game I made bc coding is fun!")
print("(▽◕ ᴥ ◕▽)")
print("---------------------------------")

# Creating first variable
NumberChoices = [1,2,3,4,5,6,7,8,9] #creates array of 9 different spaces
## using 2D array
GameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

# Creating a funct that will print out gameboard on command
# Creating 2 for loops bc we have to loop through 2D of array
def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("",GameBoard[x][y], end=" |")
    print("\n+---+---+---+")

# for handing modification of gameboard
def modifyArray(num, turn):
    num -= 1
    if(num == 0):
        GameBoard[0][0] = turn
    elif(num == 1):
        GameBoard[0][1] = turn
    elif(num == 2):
        GameBoard[0][2] = turn
    elif(num == 3):
        GameBoard[1][0] = turn
    elif (num == 4):
        GameBoard[1][1] = turn
    elif (num == 5):
        GameBoard[1][2] = turn
    elif (num == 6):
        GameBoard[2][0] = turn
    elif (num == 7):
        GameBoard[2][1] = turn
    elif (num == 8):
        GameBoard[2][2] = turn

def checkForWinner(GameBoard):
    ## X axis
    if(GameBoard[0][0] == 'X' and GameBoard[1][0] == 'X' and GameBoard[2][0] == 'X'):
        print("X has Won the Game!!!")
        return "X"
    elif(GameBoard[0][0] == 'O' and GameBoard[1][0] == 'O' and GameBoard[2][0] == 'O'):
        print("O has Won the Game!!!")
        return "O"
    elif (GameBoard[0][1] == 'X' and GameBoard[1][1] == 'X' and GameBoard[2][1] == 'X'):
        print("X has Won the Game!!!")
        return "X"
    elif (GameBoard[0][1] == 'O' and GameBoard[1][1] == 'O' and GameBoard[2][1] == 'O'):
        print("O has Won the Game!!!")
        return "O"
    elif (GameBoard[0][2] == 'X' and GameBoard[1][2] == 'X' and GameBoard[2][2] == 'X'):
        print("X has Won the Game!!!")
        return "X"
    elif (GameBoard[0][2] == 'O' and GameBoard[1][2] == 'O' and GameBoard[2][2] == 'O'):
        print("O has Won the Game!!!")
        return "O"
    ## Y axis
    elif(GameBoard[0][0] == 'X' and GameBoard[0][1] == 'X' and GameBoard[0][2] == 'X'):
        print("X has Won the Game!!!")
        return "X"
    elif (GameBoard[0][0] == 'O' and GameBoard[0][1] == 'O' and GameBoard[0][2] == 'O'):
        print("O has Won the Game!!!")
        return "O"
    elif (GameBoard[1][0] == 'X' and GameBoard[1][1] == 'X' and GameBoard[1][2] == 'X'):
        print("X has Won the Game!!!")
        return "X"
    elif (GameBoard[1][0] == 'O' and GameBoard[1][1] == 'O' and GameBoard[1][2] == 'O'):
        print("O has Won the Game!!!")
        return "O"
    elif (GameBoard[2][0] == 'X' and GameBoard[2][1] == 'X' and GameBoard[2][2] == 'X'):
        print("X has Won the Game!!!")
        return "X"
    elif (GameBoard[2][0] == 'O' and GameBoard[2][1] == 'O' and GameBoard[2][2] == 'O'):
        print("O has Won the Game!!!")
        return "O"
    ## Z(across) axis
    elif (GameBoard[0][0] == 'X' and GameBoard[1][1] == 'X' and GameBoard[2][2] == 'X'):
        print("X has Won the Game!!!")
        return "X"
    elif (GameBoard[0][0] == 'O' and GameBoard[1][1] == 'O' and GameBoard[2][2] == 'O'):
        print("O has Won the Game!!!")
        return "O"
    elif (GameBoard[2][0] == 'X' and GameBoard[1][1] == 'X' and GameBoard[0][2] == 'X'):
        print("X has Won the Game!!!")
        return "X"
    elif (GameBoard[2][0] == 'O' and GameBoard[1][1] == 'O' and GameBoard[0][2] == 'O'):
        print("O has Won the Game!!!")
        return "O"
    return None

# Defining more variables
leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
    #printGameBoard()
    ## for player turn
    if(turnCounter % 2 == 1):
        printGameBoard()
        numberPicked = int(input("\nChoose a number [1=9]: "))
        if(numberPicked >=1 or numberPicked <= 9):
            modifyArray(numberPicked,'X') #CANNOT GET RID OF TURN:
            NumberChoices.remove(numberPicked)
            turnCounter += 1  # Increment turn only on valid input
        else:
            print("Invalid input. Please try again.")
            continue
        #turnCounter += 1
    ## Computer's turn
    else:
        while(True):
            cpuChoice = random.choice(NumberChoices)
            print("\nCPU choice: ", cpuChoice)
            if(cpuChoice in NumberChoices):
                modifyArray(cpuChoice, 'O')
                NumberChoices.remove(cpuChoice)
                turnCounter += 1
                break
    winner = checkForWinner(GameBoard)
    if winner:
        leaveLoop = True

printGameBoard()
print("Game Over!")