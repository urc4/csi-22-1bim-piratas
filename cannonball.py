import pygame
import math

from sprite import Sprite

model_cannon_ball_one = {
    "png": "cannonBall.png",
    "width": 8,
    "height": 8,
    "speed": 20,
    "ang_offset": 0,
    "max_speed": 0,
    "density": 1,
    "acceleration": 0,
    "omega": 0,
}


class CannonBall(Sprite):
    def __init__(self, ship_parameters):
        model = model_cannon_ball_one
        model["width"] = model["height"] = ship_parameters["size"]
        model["speed"] = ship_parameters["speed"]
        super().__init__(model)
        pos = ship_parameters["position"]
        self.angle = ship_parameters["angle"]
        self.size = ship_parameters["size"]
        self.pos = (pos[0] - self.size / 2, pos[1] - self.size / 2)

    def update(self):
        self.pos = (
            self.pos[0] + self.speed * math.cos(self.angle),
            self.pos[1] + self.speed * math.sin(self.angle),
        )
        self.rect.update(self.pos[0], self.pos[1], self.size, self.size)
