# TODO corrigir o funcionamento das teclas tipo pra ter melhor responsivividade

import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE, KEYUP
import sys
from debug import debug
from models import Player, EnemyBoat
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS

# centro da surface eh no ponto 0,0
# cuidado pra nao queberar o jogo pra ifcar indo e voltando no canot da tela

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Piratas da Guanabara')
clock = pygame.time.Clock()
count = 0

all_sprites = pygame.sprite.Group()
boat = Player()
enemies = []
is_pressed = False
gen_new_enemy = False
key_pressed = None

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
            boat.create_cannon_ball() 

      if event.type == KEYUP:
         is_pressed = False


   if is_pressed:
      boat.update_pressed(key_pressed)
   else:
      boat.update_unpressed()

   screen.fill((0,0,255))
   screen.blit(boat.surface,boat.pos)
   for index,cannon_ball in enumerate(boat.cannon_balls):
      cannon_ball.update()
      if(cannon_ball.is_out_of_screen()):
         boat.cannon_balls.pop(index)
         continue
      screen.blit(cannon_ball.surface, cannon_ball.pos)

   scoreboard = int(count/60)
   debug(scoreboard)
   if scoreboard%10 == 0:
      new_enemy = EnemyBoat()
      enemies.append(new_enemy)
      count += 60
   for enemy in enemies:
      enemy.update()
      screen.blit(enemy.surface,enemy.pos)
   pygame.display.update()

      
