"""Entrypoint to run the game. You want to execute it :)

"""


import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    KEYUP,
    K_DOWN,
    K_RETURN
)
import sys
import os
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from level import Level
from menu import Menu

pygame.init()
clock = pygame.time.Clock()
level = Level()
menu = Menu()

pygame.display.flip()

menu.main_menu()

if os.path.isfile('data/Audio/background.mp3'):
    pygame.mixer.music.load('data/Audio/background.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)  # set loops to -1 to loop the music indefinitely
else:
    print("data/Audio/background.mp3 not found... ignoring", file=sys.stderr)

level.display_full_background()
while True:
    if level.game_over:  # entramos aqui apenas quando o jogador perde uma partida
        if os.path.isfile('data/Audio/background.mp3'):
            pygame.mixer.music.stop()
        level.display_game_over()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                level = Level()
        continue

    clock.tick(FPS)
    level.scoreboard.tick()  # NOTE scoreboard internal clock is also used in methods of level out of level.scoreboard

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        level.press_key(event)
        # usar pygame.joystick
        # permitir atirar e mover ao mesmo tempo assim como ir pra frente e girar

    level.generate_enemies()
    level.change_background()
    level.blit_sprites()
    level.update_sprites()
    level.draw_sprites()
    level.scoreboard.display()

    if os.path.isfile('data/Audio/background.mp3') and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(loops=-1)

    pygame.display.flip()

