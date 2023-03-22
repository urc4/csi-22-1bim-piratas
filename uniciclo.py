import pygame
from pygame.locals import *
import sys

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

WIDTH = 1020
HEIGHT = 720
FPS = 60


class CannonBall(pygame.sprite.Sprite):
   pass

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
      self.angle = 0
      self.color = (0,255,0)
      self.surface = pygame.Surface((25,40))
      self.surface.fill(self.color)
      self.cannon_balls = []

   def switch_sides(self):
      if(self.pos[0]>WIDTH):
         self.pos = (0,self.pos[1])
      if(self.pos[0]<0):
         self.pos = (WIDTH,self.pos[1])
      if(self.pos[1]>HEIGHT):
         self.pos = (self.pos[0],0)
      if(self.pos[1]<0):
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
      self.pos = self.switch_sides()
   
   def shoot_cannon_ball():
      pass
# centro da surface eh no ponto 0,0
# cuidado pra nao queberar o jogo pra ifcar indo e voltando no canot da tela

# def switch_sides(boat_pos):
#    if(boat_pos[0]>WIDTH):
#       boat_pos = (0,boat_pos[1])
#    if(boat_pos[0]<0):
#       boat_pos = (WIDTH,boat_pos[1])
#    if(boat_pos[1]>HEIGHT):
#       boat_pos = (boat_pos[0],0)
#    if(boat_pos[1]<0):
#       boat_pos = (boat_pos[0],HEIGHT)
#    return boat_pos

# def shoot_cannon_ball(boat_pos):
#    cannon_ball_size = 10
#    cannon_ball_color = (255,0,0)
#    cannon_ball = pygame.Surface((cannon_ball_size,cannon_ball_size))
#    cannon_ball.fill(cannon_ball_color)
#    cannon_ball_pos = boat_pos
#    speed = 30
#    screen.blit(cannon_ball,cannon_ball_pos)
#    boat_pos = (cannon_ball_pos[0],cannon_ball_pos[1]+speed)    
#    return cannon_ball


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Piratas da Guanabara')
clock = pygame.time.Clock()

# boat_pos = (WIDTH/2,HEIGHT/2)
# boat_width = 25
# boat_height = 40
# boat = pygame.Surface((boat_width,boat_height))
# boat_color = (0,255,0)
# boat.fill(boat_color)
# speed = 10
# boat_direction = 0
# cannon_balls =[]
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
         # if event.key == K_SPACE:
         #    cannon_balls.append(shoot_cannon_ball(boat_pos))
            



   # if boat_direction == UP:
   #    boat_pos = (boat_pos[0],boat_pos[1]-speed) 
   # if boat_direction == DOWN:
   #    boat_pos = (boat_pos[0],boat_pos[1]+speed) 
   # if boat_direction == LEFT:
   #    boat_pos = (boat_pos[0]-speed,boat_pos[1]) 
   # if boat_direction == RIGHT:
   #    boat_pos = (boat_pos[0]+speed,boat_pos[1]) 

   boat.update(key_pressed)
   # boat_pos = switch_sides(boat_pos)

   screen.fill((0,0,255))
   screen.blit(boat.surface,boat.pos)

   pygame.display.update()
      
