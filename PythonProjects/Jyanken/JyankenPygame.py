import pygame
import random
# Initializing Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's play Rock Scissors Paper!")

# Load image
intro_img = pygame.image.load("assets/introgon.PNG")
rock_img = pygame.image.load("assets/goo.png")
paper_img = pygame.image.load("assets/paa.png")
scissors_img = pygame.image.load("assets/tyoki.png")
win_img = pygame.image.load("assets/win.png")
lose_img = pygame.image.load("assets/lose.png")

# Define button positions
rock_rect = rock_img.get_rect(center=(200, 450))
paper_rect = paper_img.get_rect(center=(400, 450))
scissors_rect = scissors_img.get_rect(center=(600, 450))

# Game Variables
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
best_of_three = 2  # First to 2 wins
player_choice = None
computer_choice = None
result = ""
game_state = "intro"
waiting_for_next_round = False
font = pygame.font.Font("assets/nintendo-nes-font.ttf", 40)
font2 = pygame.font.Font("assets/nintendo-nes-font.ttf", 28)
font3 = pygame.font.Font("assets/nintendo-nes-font.ttf", 24)

# determining winner
def determine_winner(player, computer):
    """ Determines the winner based on the choices """
    global player_score, computer_score
    if player == computer:
        return "Tie!"
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
        player_score += 1
        return "Win!"
    else:
        computer_score += 1
        return "Lose!"

    # Game Loop
running = True
while running:
    screen.fill((199, 240, 254))

    if game_state == "intro":
        # Show intro screen
        screen.blit(intro_img, (WIDTH // 2 - intro_img.get_width() // 2, 100))
        intro_text = font.render("Press SPACE to Start", True, (0, 0, 0))
        screen.blit(intro_text, (WIDTH // 2 - intro_text.get_width() // 2, 600))

    elif game_state == "directions":
        # Show directions page
        directions_text1 = font.render("How to Play", True, (0, 0, 0))
        directions_text2 = font2.render("Click on the symbol icons", True, (0, 0, 0))
        directions_text3 = font3.render("to play against the computer.", True, (0, 0, 0))
        directions_text4 = font3.render("2 out of 3 wins beats the game!", True, (0, 0, 0))
        directions_text5 = font2.render("Best of Luck!", True, (0, 0, 0))
        directions_text6 = font3.render("Press SPACE to Start", True, (0, 0, 0))

        screen.blit(directions_text1, (WIDTH // 2 - directions_text1.get_width() // 2, 300))
        screen.blit(directions_text2, (WIDTH // 2 - directions_text2.get_width() // 2, 350))
        screen.blit(directions_text3, (WIDTH // 2 - directions_text3.get_width() // 2, 400))
        screen.blit(directions_text4, (WIDTH // 2 - directions_text4.get_width() // 2, 450))
        screen.blit(directions_text5, (WIDTH // 2 - directions_text5.get_width() // 2, 600))
        screen.blit(directions_text6, (WIDTH // 2 - directions_text6.get_width() // 2, 650))

    elif game_state == "game":
        screen.blit(rock_img, rock_rect)
        screen.blit(paper_img, paper_rect)
        screen.blit(scissors_img, scissors_rect)


        # Show score
        score_text = font2.render(f"Player: {player_score}  vs.  Computer: {computer_score}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 50))

        # Show choices if made
        if player_choice and computer_choice:
            player_choice_text = font2.render(f"Player chose: {player_choice.capitalize()}", True, (0, 0, 0))
            computer_choice_text = font2.render(f"Computer chose: {computer_choice.capitalize()}", True, (0, 0, 0))

            screen.blit(player_choice_text, (WIDTH // 2 - player_choice_text.get_width() // 2, 200))
            screen.blit(computer_choice_text, (WIDTH // 2 - computer_choice_text.get_width() // 2, 250))

        # Show result
        if result:
            result_text = font2.render(result, True, (255, 255, 255))
            screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 120))

        # Show final win/lose image if game ends
        if player_score == best_of_three:
            screen.blit(win_img, (WIDTH // 2 - win_img.get_width() // 2, 200))
        elif computer_score == best_of_three:
            screen.blit(lose_img, (WIDTH // 2 - lose_img.get_width() // 2, 200))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "intro":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = "directions"

        elif game_state == "directions":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = "game"

        elif game_state == "game":
            # Player selects rock, paper, or scissors
            if event.type == pygame.MOUSEBUTTONDOWN and player_score < best_of_three and computer_score < best_of_three:
                if rock_rect.collidepoint(event.pos):
                    player_choice = "rock"
                elif paper_rect.collidepoint(event.pos):
                    player_choice = "paper"
                elif scissors_rect.collidepoint(event.pos):
                    player_choice = "scissors"

                if player_choice:
                    computer_choice = random.choice(choices)
                    result = determine_winner(player_choice, computer_choice)

                    # Delay before next round (makes transition smoother)
                    waiting_for_next_round = True
                    pygame.time.delay(3000)  # 3 second delay
                    waiting_for_next_round = False

pygame.quit()