import pygame
from pygame.locals import *
import sys
import math
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

WIDTH = 500
HEIGHT = 500
FPS = 60

# no update tem qe remover canhao quando destroi um navio ou qundno sai da tela para diminuir tamnaho do vetor
class CannonBall(pygame.sprite.Sprite):
   def __init__(self, pos, ang, size, speed):
      # super.__init__(groups)
      self.speed = speed
      self.color = (255,0,0)
      self.angle = ang
      self.size = size
      self.pos = (pos[0]-self.size/2,pos[1]-self.size/2)
      self.surface = pygame.Surface((self.size,self.size))
   
   def update(self):
      self.pos = (self.pos[0] + self.speed*math.cos(self.angle),self.pos[1]+self.speed*math.sin(self.angle)) 

   def is_out_of_screen(self):
      if(self.pos[0] > WIDTH + 2*self.size or self.pos[0] < 0 - self.size):
         return True
      elif(self.pos[1] > HEIGHT + 2*self.size or self.pos[1] < 0 - self.size):
         return True
      return False

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
      self.speed = 3
      self.max_speed = 6
      self.alpha = 0.1
      self.accel = 0.1
      self.omega = 5
      self.angle = 3*math.pi/2
      self.color = (0,255,0)
      self.surface = pygame.Surface((self.width,self.height))
      self.surface.fill(self.color)
      self.cannon_balls = []

   # teria que ver comom fica com rotacao acho qeu basta adicionar o calculo em relacao ao angulo
# poderia usar pos%width
   def switch_sides(self):
      if(self.pos[0]>WIDTH):
         self.pos = (0,self.pos[1])
      elif(self.pos[0]<0):
         self.pos = (WIDTH,self.pos[1])
      if(self.pos[1]>HEIGHT):
         self.pos = (self.pos[0],0)
      elif(self.pos[1]<0):
         self.pos = (self.pos[0],HEIGHT)
      return self.pos
   
   def update_pressed(self,key_pressed):
      if key_pressed == UP:
         self.speed += self.accel
         if(self.speed > self.max_speed):
            self.speed = self.max_speed
         self.pos = (self.pos[0] + self.speed*math.cos(self.angle) ,self.pos[1]+self.speed*math.sin(self.angle)) 
      if key_pressed == LEFT:
         # self.omega += self.alpha
         ang_deg = self.angle*180/math.pi;
         ang_deg = (ang_deg - self.omega)%360;
         self.angle  = ang_deg*math.pi/180;
         self.pos = (self.pos[0] + self.speed*math.cos(self.angle) ,self.pos[1]+self.speed*math.sin(self.angle)) 

      if key_pressed == RIGHT:
         ang_deg = self.angle*180/math.pi;
         ang_deg = (ang_deg + self.omega)%360;
         self.angle  = ang_deg*math.pi/180;
         self.pos = (self.pos[0] + self.speed*math.cos(self.angle) ,self.pos[1]+self.speed*math.sin(self.angle)) 

      self.pos = self.switch_sides()


   def update_unpressed(self):
      self.omega = 5
      self.pos = (self.pos[0] + self.speed*math.cos(self.angle) ,self.pos[1]+self.speed*math.sin(self.angle)) 
      
      self.pos = self.switch_sides()




   def create_cannon_ball(self):
      # talvez tenha q considersar o angulo para acahr o centro depois
      size = 15
      speed = 20
      ang = self.angle
      pos = (self.pos[0] + self.width/2,self.pos[1]+self.height/2)
      new_cannon_ball = CannonBall(pos,ang,size,speed)
      self.cannon_balls.append(new_cannon_ball)
      self.conserve_momentum(new_cannon_ball)
   
   def conserve_momentum(self,cannon_ball):
      # massa = densidade-superficial * area
      sigma_ball = 1
      mass_ball = sigma_ball*cannon_ball.size**2
      sigma_player = 5
      mass_player = sigma_player*self.width*self.height
      self.speed = self.speed - (mass_ball/mass_player)*cannon_ball.speed


# centro da surface eh no ponto 0,0
# cuidado pra nao queberar o jogo pra ifcar indo e voltando no canot da tela

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Piratas da Guanabara')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
boat = Player(all_sprites)
# all_sprites.add(boat)

is_pressed = False

while True:
   clock.tick(FPS)
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

      if event.type == KEYDOWN:
         if event.key == K_SPACE:
            boat.create_cannon_ball() 


      if event.type == KEYUP:
         if event.key == K_UP:
            key_unpressed = UP
            # boat.accel = 0;
            is_pressed = False
         if event.key == K_LEFT:
            key_unpressed = LEFT
            is_pressed = False
         if event.key == K_RIGHT:
            key_unpressed = RIGHT         
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

   pygame.display.update()
      
