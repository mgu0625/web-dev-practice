import pygame

pygame.init()
screen = pygame.display.set_mode((350, 350))
pygame.display.set_caption("PyGame Testing Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()