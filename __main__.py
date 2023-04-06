# TODO corrigir o funcionamento das teclas tipo pra ter melhor responsivividade

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
from debug import debug

# from models import Player, EnemyBoat, EnemyPirate
from player import Player
from enemy import EnemyBoat, EnemyPirate
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS

# centro da surface eh no ponto 0,0
# cuidado pra nao queberar o jogo pra ifcar indo e voltando no canot da tela

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piratas da Guanabara")
clock = pygame.time.Clock()
count = 0

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((135, 206, 250))

boat = Player()
is_pressed = False
gen_new_enemy = False
key_pressed = None
power_up = False

boat_sprite = pygame.sprite.RenderPlain(boat)
enemy_sprites = pygame.sprite.RenderPlain()
cannonball_sprites = pygame.sprite.RenderPlain()

screen.blit(background, (0, 0))
pygame.display.flip()

while True:
    clock.tick(FPS)
    count += 1

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
                cb = boat.create_cannon_ball()
                cannonball_sprites.add(cb)
            if event.key == K_DOWN and power_up == True:
                size = 32
                cb = boat.create_cannon_ball(size)
                cannonball_sprites.add(cb)
                power_up = False
        if event.type == KEYUP:
            is_pressed = False

    if is_pressed:
        boat.update_pressed(key_pressed)
    else:
        boat.update_unpressed()

    # blit e update barco do jogador:
    screen.blit(background, boat.rect, boat.rect)  # apaga antiga posicao da tela
    boat_sprite.update()  # atualiza posicao no objeto

    # blit e update balas de canhão:
    to_remove = []
    for cannon_ball in cannonball_sprites.sprites():
        if cannon_ball.is_out_of_screen():
            to_remove.append(cannon_ball)
        else:
            screen.blit(
                background, cannon_ball.rect, cannon_ball.rect
            )  # apaga antiga posicao da tela
    cannonball_sprites.remove(*to_remove)
    cannonball_sprites.update()  # atualiza posicao no objeto

    # gera, blit e update barcos inimigos:
    scoreboard = int(count / 60)
    debug(scoreboard)
    if scoreboard % 5 == 0:
        new_enemy_pirate = EnemyPirate()
        enemy_sprites.add(new_enemy_pirate)
        count += 60
    if scoreboard % 10 == 0:
        new_enemy_boat = EnemyBoat()
        enemy_sprites.add(new_enemy_boat)
        count += 60
    if scoreboard % 15 == 0:
        power_up = True
    for enemy in enemy_sprites:
        screen.blit(background, enemy.rect, enemy.rect)  # apaga antiga posicao da tela
    enemy_sprites.update()  # atualiza posicao no objeto

    # desenha novas posicoes na tela:
    boat_sprite.draw(screen)
    cannonball_sprites.draw(screen)
    enemy_sprites.draw(screen)

    pygame.display.flip()
