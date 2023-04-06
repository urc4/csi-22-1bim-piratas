import pygame
import math
import random
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from resources_utils import load_png, spawn_random


class CannonBall(pygame.sprite.Sprite):
    def __init__(self, pos, ang, size, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("cannonBall.png")
        self.speed = speed
        self.angle = ang
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.pos = (pos[0] - self.size / 2, pos[1] - self.size / 2)
        self.surface = pygame.Surface((self.size, self.size))
        self.density = 1
        self.mass = self.density * self.size**2

    def update(self):
        self.pos = (
            self.pos[0] + self.speed * math.cos(self.angle),
            self.pos[1] + self.speed * math.sin(self.angle),
        )
        self.rect.update(self.pos[0], self.pos[1], self.size, self.size)

    def is_out_of_screen(self):
        if self.pos[0] > WIDTH + 2 * self.size or self.pos[0] < 0 - self.size:
            return True
        elif self.pos[1] > HEIGHT + 2 * self.size or self.pos[1] < 0 - self.size:
            return True
        return False
