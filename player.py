import pygame
import math
import random
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from resources_utils import load_png, spawn_random
from cannonball import CannonBall
from sprite import Sprite

model_player_one = {
    "png": "ship (3).png",
    "width": 40,
    "height": 40,
    "speed": 2,
    "ang_offset": math.pi / 2,
    "max_speed": 6,
    "density": 5,
    "acceleration": 0.1,
    "omega": math.pi / 36,
}


class Player(Sprite):
    def __init__(self):
        model = model_player_one
        new_player_sprite = Sprite(model)
        super().__init__(model)
        self.pos = (WIDTH / 2, HEIGHT / 2)
        self.max_speed = model["max_speed"]
        self.angle = 3 * math.pi / 2


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.width = 25
#         self.height = 40
#         self.image, self.rect = load_png("ship (3).png")
#         self.image = pygame.transform.scale(self.image, (self.width, self.height))
#         angle_offset = (
#             math.pi / 2
#         )  # XXX este parâmetro depende da sprite (para caso não aponte na direção (1,0))
#         self.image = pygame.transform.rotate(self.image, angle_offset * 180 / math.pi)
#         self.original_image = self.image  # para as rotinas que rotacionam o navio
#         self.pos = (WIDTH / 2, HEIGHT / 2)
#         # self.rect = self.rect.move(self.pos)
#         self.speed = 3
#         self.max_speed = 6
#         self.sigma = 5
#         self.mass = self.sigma * self.width * self.height
#         self.air_resistance_constant = 100
#         self.accel = 0.1
#         self.omega = math.pi / 36
#         self.angle = 3 * math.pi / 2

#     # teria que ver comom fica com rotacao acho qeu basta adicionar o calculo em relacao ao angulo
#     # poderia usar pos%width
#     def __switch_sides(self):
#         if self.pos[0] > WIDTH:
#             self.pos = (0, self.pos[1])
#         elif self.pos[0] < 0:
#             self.pos = (WIDTH, self.pos[1])
#         if self.pos[1] > HEIGHT:
#             self.pos = (self.pos[0], 0)
#         elif self.pos[1] < 0:
#             self.pos = (self.pos[0], HEIGHT)
#         return self.pos

#     def update_pressed(self, key_pressed):
#         self.air_resistance = -self.air_resistance_constant * self.speed / self.mass
#         if key_pressed == UP:
#             self.speed += self.accel + self.air_resistance
#             if self.speed > self.max_speed:
#                 self.speed = self.max_speed
#             self.pos = (
#                 self.pos[0] + self.speed * math.cos(self.angle),
#                 self.pos[1] + self.speed * math.sin(self.angle),
#             )
#         if key_pressed == LEFT:
#             self.angle = (self.angle - self.omega) % (2 * math.pi)
#             self.pos = (
#                 self.pos[0] + self.speed * math.cos(self.angle),
#                 self.pos[1] + self.speed * math.sin(self.angle),
#             )

#         if key_pressed == RIGHT:
#             self.angle = (self.angle + self.omega) % (2 * math.pi)
#             self.pos = (
#                 self.pos[0] + self.speed * math.cos(self.angle),
#                 self.pos[1] + self.speed * math.sin(self.angle),
#             )

#         self.pos = self.__switch_sides()

#     def update_unpressed(self):
#         self.air_resistance = -self.air_resistance_constant * self.speed / self.mass

#         if self.speed != 0:
#             self.speed += self.air_resistance
#         self.pos = (
#             self.pos[0] + self.speed * math.cos(self.angle),
#             self.pos[1] + self.speed * math.sin(self.angle),
#         )

#         self.pos = self.__switch_sides()

#     def __rotate_img(self):
#         # SEMPRE rotacionar a partir da imagem ORIGINAL senao a imagem fica arbitrariamente distorcida
#         # (dica frequente em tutoriais e fóruns)
#         if not (0 <= self.angle < 2 * math.pi):
#             self.angle %= 2 * math.pi  # obs: x % y >= 0 se y > 0 (diferente de C e C++)
#         if math.pi / 2 <= self.angle < 3 * math.pi / 2:
#             self.image = pygame.transform.rotate(
#                 pygame.transform.flip(self.original_image, False, True),
#                 -180 * self.angle / math.pi,
#             )
#         else:
#             self.image = pygame.transform.rotate(
#                 self.original_image, -180 * self.angle / math.pi
#             )
#         # mantém o mesmo centro:
#         center = self.rect.center
#         self.rect = self.image.get_rect(center=center)

#     def update(self):
#         self.rect.update(self.pos[0], self.pos[1], self.width, self.height)
#         self.__rotate_img()

#     def create_cannon_ball(self, size=8):
#         # talvez tenha q considersar o angulo para achar o centro depois
#         speed = 20
#         ang = self.angle
#         pos = (self.pos[0] + self.width / 2, self.pos[1] + self.height / 2)
#         new_cannon_ball = CannonBall(pos, ang, size, speed)
#         self.__conserve_momentum(new_cannon_ball)
#         return new_cannon_ball

#     def __conserve_momentum(self, cannon_ball):
#         # massa = densidade-superficial * area
#         sigma_ball = 1
#         mass_ball = sigma_ball * cannon_ball.size**2
#         sigma_player = 5
#         mass_player = sigma_player * self.width * self.height
#         self.speed = self.speed - (mass_ball / mass_player) * cannon_ball.speed
#         # nao pode deixar passar do max speed?
