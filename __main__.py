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
    K_RETURN
)
import sys
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from level import Level

pygame.init()
clock = pygame.time.Clock()
level = Level()

pygame.display.flip()

while True:
    if level.game_over:  # entramos aqui apenas quando o jogador perde uma partida
        level.display_game_over()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key in [K_RETURN, K_SPACE]:
                level = Level()
        continue

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
    level.generate_enemies()

    level.blit_sprites()
    level.update_sprites()
    level.draw_sprites()

    pygame.display.flip()

