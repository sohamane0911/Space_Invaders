import pygame
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 60

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()