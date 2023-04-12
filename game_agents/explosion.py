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
    def __init__(self, pos):
        model = model_explosion_one
        super().__init__(model)
        self.pos = pos
