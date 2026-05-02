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
player_width = player.get_width()

enemy = pygame.transform.scale(
    pygame.image.load("enemyShip.gif").convert(),
    (96, 96)
)

enemy_x = [random.randint(0, screen_width - 96) for _ in range(4)]
enemy_y = [-50, -300, -600, -900]
enemy_speed = [5, 5, 5, 5]

laser_x = [733, 733, 748, 748]
laser_y = [770, 770, 770, 770]

laser_speed_x = [15]
laser_speed_y = [30]

laser1l_active = False
laser1r_active = False
laser2l_active = False
laser2r_active = False

laserl1_rect = pygame.Rect(0, 0, 64, 64)
laserl2_rect = pygame.Rect(0, 0, 64, 64)
laserr1_rect = pygame.Rect(0, 0, 64, 64)
laserr2_rect = pygame.Rect(0, 0, 64, 64)

def laser_shoot_ready():
    global laser_x, laser_y
    global laser1l_active, laser1r_active, laser2l_active, laser2r_active

    if not laser1l_active and not laser1r_active:
        laser_x[0] = player_x + 45
        laser_y[0] = player_y
        laser1l_active = True

        laser_x[2] = player_x - 15
        laser_y[2] = player_y
        laser1r_active = True

    elif not laser2l_active and not laser2r_active:
        laser_x[1] = player_x + 45
        laser_y[1] = player_y
        laser2l_active = True

        laser_x[3] = player_x - 15
        laser_y[3] = player_y
        laser2r_active = True


def laser_shoot_fire():
    global laser_y
    global laser1l_active, laser2l_active, laser1r_active, laser2r_active

    if laser1l_active:
        laser_y[0] -= laser_speed_y[0]
        if laser_y[0] <= -50:
            laser1l_active = False

    if laser1r_active:
        laser_y[2] -= laser_speed_y[0]
        if laser_y[2] <= -50:
            laser1r_active = False

    if laser2l_active:
        laser_y[1] -= laser_speed_y[0]
        if laser_y[1] <= -50:
            laser2l_active = False

    if laser2r_active:
        laser_y[3] -= laser_speed_y[0]
        if laser_y[3] <= -50:
            laser2r_active = False

game_state = "menu"

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_state == "menu" and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                game_state = "play"

            elif game_state == "play" and event.key == pygame.K_SPACE:
                laser_shoot_ready()

    if game_state == "menu":
        screen.blit(main_menu_bg, (0, 0))

    elif game_state == "play":

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed

        if player_x <= 0:
            player_x = 0

        if player_x >= screen_width - player_width:
            player_x = screen_width - player_width

        laser_shoot_fire()

        screen.blit(main_menu_bg, (0, 0))

        for i in range(len(enemy_x)):
            enemy_y[i] += enemy_speed[i]

            if enemy_y[i] >= player_y:
                game_state = "lost"

            if enemy_y[i] > screen_height:
                enemy_y[i] = -100
                enemy_x[i] = random.randint(0, screen_width - 96)

            screen.blit(enemy, (enemy_x[i], enemy_y[i]))

        if laser1l_active:
            pygame.draw.rect(screen, (255, 0, 0), (laser_x[0], laser_y[0], 5, 20))
        if laser1r_active:
            pygame.draw.rect(screen, (255, 0, 0), (laser_x[2], laser_y[2], 5, 20))
        if laser2l_active:
            pygame.draw.rect(screen, (255, 0, 0), (laser_x[1], laser_y[1], 5, 20))
        if laser2r_active:
            pygame.draw.rect(screen, (255, 0, 0), (laser_x[3], laser_y[3], 5, 20))

        screen.blit(player, (player_x, player_y))

    elif game_state == "lost":
        screen.fill((0, 0, 0))

    pygame.display.update()

pygame.quit()
