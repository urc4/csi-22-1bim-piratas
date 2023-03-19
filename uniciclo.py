import pygame
from pygame.locals import *
import sys

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

WIDTH = 720
HEIGHT = 720
FPS = 60

# centro da surface eh no ponto 0,0
# cuidado pra nao queberar o jogo pra ifcar indo e voltando no canot da tela
def switch_sides(boat_pos):
   if(boat_pos[0]>WIDTH):
      boat_pos = (0,boat_pos[1])
   if(boat_pos[0]<0):
      boat_pos = (WIDTH,boat_pos[1])
   if(boat_pos[1]>HEIGHT):
      boat_pos = (boat_pos[0],0)
   if(boat_pos[1]<0):
      boat_pos = (boat_pos[0],HEIGHT)
   return boat_pos

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Piratas da Guanabara')
clock = pygame.time.Clock()

boat_pos = (WIDTH/2,HEIGHT/2)
boat_width = 15
boat_height = 15
boat = pygame.Surface((boat_width,boat_height))
boat_color = (0,255,0)
boat.fill(boat_color)
speed = 10
boat_direction = 0

while True:
   clock.tick(FPS)
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit() 

      if event.type == KEYDOWN:
         if event.key == K_UP:
            boat_direction = UP
         if event.key == K_DOWN:
            boat_direction = DOWN
         if event.key == K_LEFT:
            boat_direction = LEFT
         if event.key == K_RIGHT:
            boat_direction = RIGHT



   if boat_direction == UP:
      boat_pos = (boat_pos[0],boat_pos[1]-speed) 
   if boat_direction == DOWN:
      boat_pos = (boat_pos[0],boat_pos[1]+speed) 
   if boat_direction == LEFT:
      boat_pos = (boat_pos[0]-speed,boat_pos[1]) 
   if boat_direction == RIGHT:
      boat_pos = (boat_pos[0]+speed,boat_pos[1]) 
   
   boat_pos = switch_sides(boat_pos)

   screen.fill((0,0,255))
   screen.blit(boat,boat_pos)

   pygame.display.update()
      
