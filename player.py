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
