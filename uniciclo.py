import pygame
from pygame.locals import *
import sys
import math
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

WIDTH = 1020
HEIGHT = 720
FPS = 60

# no update tem qe remover canhao quando destroi um navio ou qundno sai da tela para diminuir tamnaho do vetor
class CannonBall(pygame.sprite.Sprite):
   def __init__(self, pos, ang):
      # super.__init__(groups)
      self.speed = 50
      self.color = (255,0,0)
      self.angle = ang
      self.size = 10
      self.pos = (pos[0]-self.size/2,pos[1]-self.size/2)
      self.surface = pygame.Surface((self.size,self.size))
   
   def update(self):
      self.pos = (self.pos[0] + self.speed*math.cos(self.angle),self.pos[1]+self.speed*math.sin(self.angle)) 

class EnemyBoat(pygame.sprite.Sprite):
   pass

class EnemyPirate(pygame.sprite.Sprite):
   pass

class Player(pygame.sprite.Sprite):
   
   def __init__(self, groups):
      # super.__init__(groups) noa ta funcionadno nao sei pq
      self.pos = (WIDTH/2,HEIGHT/2)
      self.width = 25
      self.height = 40 
      self.speed = 10
      self.angle = math.pi/2
      self.color = (0,255,0)
      self.surface = pygame.Surface((self.width,self.height))
      self.surface.fill(self.color)
      self.cannon_balls = []

   # teria que ver comom fica com rotacao acho qeu basta adicionar o calculo em relacao ao angulo

   def switch_sides(self):
      if(self.pos[0]>WIDTH - self.width/5):
         self.pos = (0,self.pos[1])
      elif(self.pos[0]<0 + self.width/5):
         self.pos = (WIDTH,self.pos[1])
      if(self.pos[1]>HEIGHT):
         self.pos = (self.pos[0],0)
      elif(self.pos[1]<0 + self.height/5):
         self.pos = (self.pos[0],HEIGHT)
      return self.pos
   
   def update(self,key_pressed):
      if key_pressed == UP:
         self.pos = (self.pos[0],self.pos[1]-self.speed) 
      if key_pressed == DOWN:
         self.pos = (self.pos[0],self.pos[1]+self.speed) 
      if key_pressed == LEFT:
         self.pos = (self.pos[0]-self.speed,self.pos[1]) 
      if key_pressed == RIGHT:
         self.pos = (self.pos[0]+self.speed,self.pos[1]) 
      # if len(self.cannon_balls) > 0:
      #    for cannon_ball in self.cannon_balls:
      #       # cannon_ball.update()
      #       pass

      self.pos = self.switch_sides()

   def create_cannon_ball(self):
      # talvez tenha q considersar o angulo para acahr o centro depois
      new_cannon_ball = CannonBall((self.pos[0] + self.width/2,self.pos[1]+self.height/2),self.angle)
      self.cannon_balls.append(new_cannon_ball)


# centro da surface eh no ponto 0,0
# cuidado pra nao queberar o jogo pra ifcar indo e voltando no canot da tela

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Piratas da Guanabara')
clock = pygame.time.Clock()

key_pressed = 0
all_sprites = pygame.sprite.Group()
boat = Player(all_sprites)
# all_sprites.add(boat)


while True:
   clock.tick(FPS)
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit() 
         sys.exit()

      if event.type == KEYDOWN:
         if event.key == K_UP:
            key_pressed = UP
         if event.key == K_DOWN:
            key_pressed = DOWN
         if event.key == K_LEFT:
            key_pressed = LEFT
         if event.key == K_RIGHT:
            key_pressed = RIGHT
         if event.key == K_SPACE:
            # new_cannon_ball = CannonBall(boat.pos,boat.angle)
            boat.create_cannon_ball()            


   boat.update(key_pressed)

   screen.fill((0,0,255))
   screen.blit(boat.surface,boat.pos)
   for cannon_ball in boat.cannon_balls:
      cannon_ball.update()
      screen.blit(cannon_ball.surface, cannon_ball.pos)

   pygame.display.update()
      
