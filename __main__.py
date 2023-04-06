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
from enemy import Enemies
from scoreboard import Scoreboard
from player import Player
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from debug import debug

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piratas da Guanabara")
clock = pygame.time.Clock()
scoreboard = Scoreboard()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((135, 206, 250))

is_pressed = False
gen_new_enemy = False
key_pressed = None
power_up = False

boat = Player()
boat_sprite = pygame.sprite.RenderPlain(boat)
enemies = Enemies()
enemy_sprites = enemies.all_enemies
cannonball_sprites = boat.all_cannon_balls

screen.blit(background, (0, 0))
pygame.display.flip()

while True:
    clock.tick(FPS)
    scoreboard.tick()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                key_pressed = UP
                is_pressed = True
            if event.key == K_LEFT:
                key_pressed = LEFT
                is_pressed = True
            if event.key == K_RIGHT:
                key_pressed = RIGHT
                is_pressed = True
            if event.key == K_SPACE:
                boat.shoot_cannon()
            if event.key == K_DOWN and power_up == True:
                size = 32
                boat.shoot_cannon(32)
                power_up = False
        if event.type == KEYUP:
            is_pressed = False
    if is_pressed:
        boat.move(key_pressed)
    else:
        boat.move_unpressed()
    screen.blit(background, boat.rect, boat.rect)
    boat_sprite.update()

    # blit e update balas de canhão:
    to_remove = []
    for cannon_ball in boat.all_cannon_balls:
        if cannon_ball.is_out_of_screen():
            # to_remove.append(cannon_ball)
            pass
        else:
            screen.blit(
                background, cannon_ball.rect, cannon_ball.rect
            )  # apaga antiga posicao da tela
    # cannonball_sprites.remove(*to_remove)
    # cannonball_sprites.update()  # atualiza posicao no objeto
    boat.all_cannon_balls.update()

    # gera, blit e update barcos inimigos:
    scoreboard.display()
    if scoreboard.score % 5 == 0:
        enemies.create_new_enemy(2)
        scoreboard.count += 60
    if scoreboard.score % 10 == 0:
        enemies.create_new_enemy(1)
        scoreboard.count += 60

    if scoreboard.score % 15 == 0:
        power_up = True
    if power_up == True:
        debug("power up", 10, 100)
    else:
        debug("", 10, 100)

    for enemy in enemy_sprites:
        screen.blit(background, enemy.rect, enemy.rect)  # apaga antiga posicao da tela
    enemy_sprites.update()  # atualiza posicao no objeto

    # desenha novas posicoes na tela:
    boat_sprite.draw(screen)
    cannonball_sprites.draw(screen)
    enemy_sprites.draw(screen)

    pygame.display.flip()
