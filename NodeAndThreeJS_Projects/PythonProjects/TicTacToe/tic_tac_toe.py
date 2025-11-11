# to generate random choice for CPU
import pygame
import random

# Screen Settings
pygame.init() #initialize all PyGame module
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10    #Line Thickness for Board Grid
BG_COLOR = (18, 30, 60)  #Bkgd color (r,g,b)
LINE_COLOR = (13, 22, 46)    #Grid Line Color
XCOLOR = (148, 254, 172)
OCOLOR = (199, 240, 254)
FONT = pygame.font.Font("assets/nintendo-nes-font.ttf", 80)

# Creating game window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) #creates PyGame window with given w x h
pygame.display.set_caption("Welcome to my Little Tic-Tac-Toe! ✺◟(∗❛ัᴗ❛ั∗)◞✺")
screen.fill(BG_COLOR)   #Fills entire screen with Bkgd color before drawing

# Game variables
rows, cols = 3, 3
cell_size = WIDTH // cols
GameBoard = [["", "", ""], ["", "", ""], ["", "", ""]]
turn = "X"  # Player starts as X
running = True
winner = None

# drawing the board
def Board():
    for row in range(1, rows):
        pygame.draw.line(screen, LINE_COLOR, (0, row * cell_size), (WIDTH, row * cell_size), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * cell_size, 0), (row * cell_size, HEIGHT), LINE_WIDTH)

def marks():
    for row in range(rows):
        for col in range(cols):
            if GameBoard[row][col] == "X":
                text = FONT.render("X", True, XCOLOR)
                screen.blit(text, (col * cell_size + 50, row * cell_size + 30))
            elif GameBoard[row][col] == "O":
                text = FONT.render("O", True, OCOLOR)
                screen.blit(text, (col * cell_size + 50, row * cell_size + 30))


def checkForWinner(GameBoard):
    global winner
    for row in range(rows):
        if GameBoard[row][0] == GameBoard[row][1] == GameBoard[row][2] and GameBoard[row][0] != "":
            winner = GameBoard[row][0]
            return True

    for col in range(cols):
        if GameBoard[0][col] == GameBoard[1][col] == GameBoard[2][col] and GameBoard[0][col] != "":
            winner = GameBoard[0][col]
            return True
    ## Z(across) axis
    if GameBoard[0][0] == GameBoard[1][1] == GameBoard[2][2] and GameBoard[0][0] != "":
        winner = GameBoard[0][0]
        return True
    if GameBoard[0][2] == GameBoard[1][1] == GameBoard[2][0] and GameBoard[0][2] != "":
        winner = GameBoard[0][2]
        return True
    return False

# CPU's move
def cpuMove():
    empty_cells = [(r, c) for r in range(rows) for c in range(cols) if GameBoard[r][c] == ""]
    if empty_cells:
        r, c = random.choice(empty_cells)
        GameBoard[r][c] = "O"

# Game loop
while running:
    screen.fill(BG_COLOR)
    Board()
    marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and turn == "X" and not winner:
            x, y = event.pos
            row, col = y // cell_size, x // cell_size

            if GameBoard[row][col] == "":
                GameBoard[row][col] = "X"
                turn = "O"

                if checkForWinner(GameBoard):
                    print(f"{winner} wins!")
                    running = False  # stops game after a win
                elif checkForWinner(GameBoard):
                    print(f"{winner} wins!")
                    running = False  # stops game after a win

            else:
                pygame.time.delay(500)  # Simulate CPU delay
                cpuMove()
                turn = "X"

                if checkForWinner(GameBoard):
                    print(f"{winner} wins!")
                    running = False #stops game after a win
                elif checkForWinner(GameBoard):
                    print(f"{winner} wins!")
                    running = False #stops game after a win

    pygame.display.update()

pygame.quit()
