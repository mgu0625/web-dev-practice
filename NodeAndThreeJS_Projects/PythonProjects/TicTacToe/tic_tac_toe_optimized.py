# to generate random choice for CPU
import pygame
import math

# Screen Settings
pygame.init() #initialize all PyGame module
WIDTH, HEIGHT = 600, 700
GRID_HEIGHT = 600
LINE_WIDTH = 10    #Line Thickness for Board Grid
BG_COLOR = (18, 30, 60)  #Bkgd color (r,g,b)
LINE_COLOR = (13, 22, 46)    #Grid Line Color
XCOLOR = (148, 254, 172)
OCOLOR = (199, 240, 254)
FONT = pygame.font.Font("assets/nintendo-nes-font.ttf", 80)
FONT2 = pygame.font.Font("assets/nintendo-nes-font.ttf", 40)

# Creating game window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) #creates PyGame window with given w x h
pygame.display.set_caption("Welcome to my Little Tic-Tac-Toe! ✺◟(∗❛ัᴗ❛ั∗)◞✺")
screen.fill(BG_COLOR)   #Fills entire screen with Bkgd color before drawing

# Game variables
rows, cols = 3, 3
cell_size = WIDTH // cols
gameboard = [["", "", ""], ["", "", ""], ["", "", ""]]
turn = "X"  # Player starts as X
running = True
winner = None
button_rect = pygame.Rect(200, 620, 200, 50)

# drawing the board
def board():
    for row in range(1, rows):
        pygame.draw.line(screen, LINE_COLOR, (0, row * cell_size), (WIDTH, row * cell_size), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * cell_size, 0), (row * cell_size, GRID_HEIGHT), LINE_WIDTH)

def marks():
    for row in range(rows):
        for col in range(cols):
            if gameboard[row][col] == "X":
                text = FONT.render("X", True, XCOLOR)
                screen.blit(text, (col * cell_size + 50, row * cell_size + 30))
            elif gameboard[row][col] == "O":
                text = FONT.render("O", True, OCOLOR)
                screen.blit(text, (col * cell_size + 50, row * cell_size + 30))


class Button:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load('assets/ResetButton.png')
        self.image = pygame.transform.scale(self.image, (200, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x,y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
# create restart button instance
reset_button = Button(300, GRID_HEIGHT + 100, "assets/reset.png")

def reset_game():
    global gameboard, turn, winner
    gameboard = [["", "", ""], ["", "", ""], ["", "", ""]]  # Reset board
    turn = "X"  # Reset player turn
    winner = None

def check_for_winner():
    global winner
    for row in range(rows):
        if gameboard[row][0] == gameboard[row][1] == gameboard[row][2] and gameboard[row][0] != "":
            winner = gameboard[row][0]
            return winner

    for col in range(cols):
        if gameboard[0][col] == gameboard[1][col] == gameboard[2][col] and gameboard[0][col] != "":
            winner = gameboard[0][col]
            return winner
    ## Z(across) axis
    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] and gameboard[0][0] != "":
        winner = gameboard[0][0]
        return winner
    if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] and gameboard[0][2] != "":
        winner = gameboard[0][2]
        return winner
    return None

# Checking for Ties
def check_if_board_is_full():
    return all(cell != "" for row in gameboard for cell in row)

# Minimax Algorithm for CPU
def minimax(depth, Maximizing):
    if check_for_winner():
        return 1 if winner == "O" else -1
    if check_if_board_is_full():
        return 0 #for tie
    if Maximizing:
        BestScore = -math.inf
        for row in range(3):
            for col in range(3):
                if gameboard[row][col] =="":
                    gameboard[row][col] = "O"
                    score = minimax(depth + 1, False)
                    gameboard[row][col] = "" #Undo move
                    BestScore = max(score, BestScore)
        return BestScore
    else:
        BestScore = math.inf
        for row in range(3):
            for col in range(3):
                if gameboard[row][col] =="":
                    gameboard[row][col] = "X"
                    score = minimax(depth + 1, True)
                    gameboard[row][col] = "" #Undo move
                    BestScore = min(score, BestScore)
        return BestScore

# CPU's move
def cpu_move():
    BestScore = -math.inf
    BestMove = None

    for row in range(3):
        for col in range(3):
            if gameboard[row][col] == "":
                gameboard[row][col] = "O"
                score = minimax(0, False)
                gameboard[row][col] = ""

                if score > BestScore:
                    BestScore = score
                    BestMove = (row, col)

    if BestMove:
        gameboard[BestMove[0]][BestMove[1]] = "O"

def display_message(text):
    """ Game Over ((((･ิ(･ิω(･ิω･ิ)ω･ิ)･ิ)))) """
    screen.fill(BG_COLOR)  # Clear screen to ensure visibility
    board()
    marks()
    reset_button.draw()

    message = FONT2.render(text, True, (255, 223, 224))
    text_rect = message.get_rect(midtop=(WIDTH // 2, GRID_HEIGHT + 20))
    screen.blit(message, text_rect)
    pygame.display.flip()  # Force screen update
    pygame.time.delay(3000)

# Game loop
runing = True
while running:
    screen.fill(BG_COLOR)
    board()
    marks()

    if winner or check_if_board_is_full():
        display_message("Game Over!!" if not winner else f"{winner} Wins!")
        pygame.display.update()
        reset_button.draw()
    if reset_button.draw():
        display_message("Game Reset!")  # Debugging message
        print("Game Reset!")
        pygame.display.update()
        reset_game()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect if Reset Button was Clicked
        if reset_button.is_clicked(event):
            display_message("Game Reset!")
            print("Game Reset!")# Debugging message
            pygame.display.update()
            reset_game()

        if event.type == pygame.MOUSEBUTTONDOWN and turn == "X" and not winner:
            x, y = event.pos
            row, col = y // cell_size, x // cell_size

            # Player move inside grid
            if y < GRID_HEIGHT and turn == "X" and not winner:
                row, col = y // cell_size, x // cell_size

                if 0 <= row < 3 and 0 <= col < 3:
                    if gameboard[row][col] == "":
                        gameboard[row][col] = "X"
                        turn = "O"

                        winner = check_for_winner()
                        if check_if_board_is_full():
                            display_message("It's a tie!")
                            print("It's a tie!")
                            pygame.display.update()
                        elif check_for_winner():
                            display_message(f"{winner} wins!")
                            print(f"{winner} wins!")
                            pygame.display.update()


                        else:
                            pygame.time.delay(500)  # Simulate CPU delay
                            cpu_move()
                            turn = "X"

                            winner = check_for_winner()
                            if check_if_board_is_full():
                                print("It's a tie!")
                                display_message("It's a tie!")
                                pygame.display.update()
                                running = False
                            elif check_for_winner():
                                print(f"{winner} wins!")
                                display_message(f"{winner} wins!")
                                pygame.display.update()
                                running = False
                else:
                    print("Invalid click! Click inside the grid.")


pygame.quit()
