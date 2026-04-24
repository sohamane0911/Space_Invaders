import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Game window setup (same as main code)
screen_width = 1534
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
