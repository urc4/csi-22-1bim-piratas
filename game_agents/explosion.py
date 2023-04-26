""" Holds class Explosion

"""
import pygame.transform
import math
import os.path
from .sprite import Sprite

model_explosion_one = {
    "png": os.path.join("PNG", "Retina", "Effects", "explosion1.png"),
    "width": 10,
    "height": 10,
    "speed": 0,
    "ang_offset": math.pi / 2,
    "max_speed": 6,
    "density": 5,
    "acceleration": 0.1,
    "omega": math.pi / 36,
}


class Explosion(Sprite):
    """Explosion"""
    def __init__(self, pos):
        model = model_explosion_one
        super().__init__(model)
        self.pos = pos
        self.finished = False

    def update(self):
        # super().update()
        if self.width < 50:
            self.width *= 1.3
            self.height *= 1.3
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            # center = self.rect.center
            # self.rect = self.image.get_rect(center=center)
            self.rect.update(self.pos[0] - self.width / 2, self.pos[1] - self.height / 2, self.width, self.height)
        else:
            self.finished = True  # flag to be removed from explosion sprites group
