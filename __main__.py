# TODO corrigir o funcionamento das teclas tipo pra ter melhor responsivividade
# mudancas para melhoria da gameplay: rotacionar e driftar, so mudar velcoidade apos presiionar K_UP
# carregar o canhao especial


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

if os.path.isfile('data/Audio/background.mp3'):
    background_music = pygame.mixer.Sound('data/Audio/background.mp3') #som aqui
    background_music.set_volume(0.5) #som aqui
else:
    print("data/Audio/background.mp3 not found... ignoring", file=sys.stderr)
menu.main_menu()
if os.path.isfile('data/Audio/background.mp3'):
    background_music.play()

while True:
    clock.tick(FPS)
    level.scoreboard.tick()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        level.press_key(event)
        # usar pygame.joystick
        # permitir atirar e mover ao mesmo tempo assim como ir pra frente e girar

    level.scoreboard.display()
    level.generate_enemies(level.scoreboard.score)

    level.blit_sprites()
    level.update_sprites()
    level.draw_sprites()

    pygame.display.flip()
