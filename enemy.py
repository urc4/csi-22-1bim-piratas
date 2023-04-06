import pygame
import math
from resources_utils import load_png, spawn_random
from globals import WIDTH, HEIGHT
from sprite import Sprite


model_enemy_one = {
    "png": "ship (8).png",
    "width": 40,
    "height": 40,
    "speed": 2,
    "ang_offset": math.pi / 2,
    "density": 5,
}

model_enemy_two = {
    "png": "dinghyLarge1.png",
    "width": 15,
    "height": 20,
    "speed": 2.5,
    "ang_offset": math.pi / 2,
    "density": 1,
}

# could potentially add enemies that turn


class Enemies:
    def __init__(self):
        self.all_enemies = pygame.sprite.Group()

    def create_new_enemy(self, type):
        if type == 1:
            model = model_enemy_one
        elif type == 2:
            model = model_enemy_two
        else:
            model = model_enemy_one

        new_enemy_sprite = Sprite(model)
        self.all_enemies.add(new_enemy_sprite)

    def update(self):
        for enemy in self.all_enemies:
            if enemy.is_out_of_screen():
                self.all_enemies.remove(enemy)
            enemy.update()


# class EnemySprite(pygame.sprite.Sprite):
#     def __init__(self, model):
#         pygame.sprite.Sprite.__init__(self)
#         self.width = model["width"]
#         self.height = model["height"]
#         self.image, self.rect = load_png(model["png"])
#         self.image = pygame.transform.scale(self.image, (self.width, self.height))
#         angle_offset = math.pi / 2
#         self.image = pygame.transform.rotate(self.image, angle_offset * 180 / math.pi)
#         self.original_image = self.image  # para as rotinas que rotacionam o navio
#         self.pos, self.angle = spawn_random()
#         self.speed = model["speed"]
#         self.surface = pygame.Surface((self.width, self.height))

#     def __rotate_img(self):
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
#         self.pos = (
#             self.pos[0] + self.speed * math.cos(self.angle),
#             self.pos[1] + self.speed * math.sin(self.angle),
#         )
#         self.rect.update(self.pos[0], self.pos[1], self.width, self.height)
#         self.__rotate_img()

#     def is_out_of_screen(self):
#         if self.pos[0] > WIDTH + 2 * self.size or self.pos[0] < 0 - self.size:
#             return True
#         elif self.pos[1] > HEIGHT + 2 * self.size or self.pos[1] < 0 - self.size:
#             return True
#         return False
