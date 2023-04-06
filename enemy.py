import pygame
import math
from sprite import Sprite


model_enemy_one = {
    "png": "ship (8).png",
    "width": 40,
    "height": 40,
    "speed": 2,
    "ang_offset": math.pi / 2,
    "density": 5,
    "acceleration": 0.1,
    "omega": math.pi / 36,
}

model_enemy_two = {
    "png": "dinghyLarge1.png",
    "width": 15,
    "height": 20,
    "speed": 2.5,
    "ang_offset": math.pi / 2,
    "density": 1,
    "acceleration": 0.1,
    "omega": math.pi / 36,
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
