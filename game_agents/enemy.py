""" Holds classes SingleEnemy and Enemies

"""
import pygame
import math
import os.path
from .sprite import Sprite
from resources_utils import load_png
from globals import ENEMY_POS
import random

model_enemy_one = {
    "png": os.path.join("PNG", "Retina", "Ships", "ship (8).png"),
    "width": 40,
    "height": 40,
    "speed": 2,
    "ang_offset": math.pi / 2,
    "density": 5,
    "acceleration": 0.1,
    "omega": math.pi / 36,
    "type": 1
}

model_enemy_two = {
    "png": os.path.join("PNG", "Retina", "Ships", "dinghyLarge1.png"),
    "width": 15,
    "height": 20,
    "speed": 3,
    "ang_offset": math.pi / 2,
    "density": 1,
    "acceleration": 0.1,
    "omega": math.pi / 36,
    "type": 2
}

# could potentially add enemies that turn

class SingleEnemy(Sprite):
    """Enemy boat, of type 1 (big, slow, 2 shots to destroy) or 2 (small, fast, 1 shot to destroy)"""
    def __init__(self, model):
        super().__init__(model)
        self.type = model["type"]
        self.lives = 2 if model["type"] == 1 else 1  # barco type 1 precisa de 2 tiros de canhao para explodir
        self.pos = random.choice(ENEMY_POS)

    def change_image(self):
        """Update type 1 boat art (technically, a Surface  object) to indicate it received the first shot

        :return:
        """
        self.image, self.rect = load_png(os.path.join("PNG", "Retina", "Ships", "ship (14).png"))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 90)
        self.original_image = self.image  # para as rotinas que rotacionam o navio
        self.rotate_image()


class Enemies:
    """Collection of enemy boats"""
    def __init__(self):
        self.all_enemies = pygame.sprite.Group()

    def create_new_enemy(self, type):
        """ Create enemy boat

        :param type: int (1 or 2)
        :return: None
        """
        if type == 1:
            model = model_enemy_one
        elif type == 2:
            model = model_enemy_two
        else:
            model = model_enemy_one

        new_enemy_sprite = SingleEnemy(model)
        self.all_enemies.add(new_enemy_sprite)

    def update(self):
        for enemy in self.all_enemies:
            if enemy.is_out_of_screen():
                self.all_enemies.remove(enemy)
            enemy.update()
