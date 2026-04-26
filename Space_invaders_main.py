import pygame
import random

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
FPS = 60

screen_width = 1534
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

main_menu_bg = pygame.transform.scale(
    pygame.image.load("SI ain menu.png").convert(),
    (1534, 900)
)

bg = pygame.image.load("bg moving.png").convert()
bg_height = bg.get_height()

player = pygame.transform.scale(
    pygame.image.load("ship.gif").convert(),
    (96, 96)
)

player_lives = pygame.transform.scale(
    pygame.image.load("ship.gif").convert(),
    (32, 32)
)

player_x = 733
player_y = 770
player_speed = 20

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(main_menu_bg, (0, 0))

    screen.blit(player, (player_x, player_y))

    pygame.display.update()

pygame.quit()
