import pygame
import math
import os.path
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from .cannonball import CannonBall
from .sprite import Sprite

model_player_one = {
    "png": os.path.join("PNG", "Retina", "Ships", "ship (3).png"),
    "width": 40,
    "height": 40,
    "speed": 0,
    "ang_offset": math.pi / 2,
    "max_speed": 6,
    "density": 5,
    "acceleration": 0.1,
    "omega": math.pi / 36,
}


class Player(Sprite):
    def __init__(self):
        model = model_player_one
        super().__init__(model)
        self.pos = (WIDTH / 2, HEIGHT / 2)
        self.max_speed = model["max_speed"]
        self.angle = 3 * math.pi / 2
        self.all_cannon_balls = pygame.sprite.Group()
        self.cannon_sound = pygame.mixer.Sound('data/Audio/cannon.mp3') #Som aqui
        self.cannon_sound.set_volume(0.3)
        #explosion_sound = pygame.mixer.Sound('data/Audio/explosion.mp3') #Som aqui
        
    def shoot_cannon(self, size=8, speed=20):
        ship_parameters = {}
        ship_parameters["angle"] = self.angle
        ship_parameters["position"] = (
            self.pos[0] + self.width / 2,
            self.pos[1] + self.height / 2,
        )
        ship_parameters["size"] = size
        ship_parameters["speed"] = speed
        new_cannon_ball = CannonBall(ship_parameters)
        self.conserve_momentum(new_cannon_ball)
        self.all_cannon_balls.add(new_cannon_ball)
        self.cannon_sound.play()

    def conserve_momentum(self, cannon_ball):
        self.speed = self.speed - (cannon_ball.mass / self.mass) * cannon_ball.speed
