import pygame
import math
from resources_utils import load_png, spawn_random
from globals import WIDTH, HEIGHT
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from cannonball import CannonBall


class Sprite(pygame.sprite.Sprite):
    def __init__(self, model):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = model["width"], model["height"]
        self.image, self.rect = load_png(model["png"])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(
            self.image, model["ang_offset"] * 180 / math.pi
        )
        self.original_image = self.image  # para as rotinas que rotacionam o navio
        #   nao basta rotaaiconar de um angulo extra?
        self.pos, self.angle = spawn_random()
        self.speed = model["speed"]
        self.accel = model["acceleration"]
        self.omega = model["omega"]
        self.surface = pygame.Surface((self.width, self.height))
        self.mass = model["density"] * model["width"] * model["height"]

        self.all_cannon_balls = pygame.sprite.Group()

    def rotate_image(self):
        if not (0 <= self.angle < 2 * math.pi):
            self.angle %= 2 * math.pi  # obs: x % y >= 0 se y > 0 (diferente de C e C++)
        if math.pi / 2 <= self.angle < 3 * math.pi / 2:
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.original_image, False, True),
                -180 * self.angle / math.pi,
            )
        else:
            self.image = pygame.transform.rotate(
                self.original_image, -180 * self.angle / math.pi
            )
        # mantém o mesmo centro:
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def update(self):
        self.pos = (
            self.pos[0] + self.speed * math.cos(self.angle),
            self.pos[1] + self.speed * math.sin(self.angle),
        )
        self.rect.update(self.pos[0], self.pos[1], self.width, self.height)
        self.rotate_image()
        self.pos = self.switch_sides()

    def is_out_of_screen(self):
        if self.pos[0] > WIDTH + 2 * self.size or self.pos[0] < 0 - self.size:
            return True
        elif self.pos[1] > HEIGHT + 2 * self.size or self.pos[1] < 0 - self.size:
            return True
        return False

    def switch_sides(self):
        if self.pos[0] > WIDTH:
            self.pos = (0, self.pos[1])
        elif self.pos[0] < 0:
            self.pos = (WIDTH, self.pos[1])
        if self.pos[1] > HEIGHT:
            self.pos = (self.pos[0], 0)
        elif self.pos[1] < 0:
            self.pos = (self.pos[0], HEIGHT)
        return self.pos

    def move(self, key_pressed=None):
        self.air_resistance = -self.air_resistance_constant * self.speed / self.mass
        if key_pressed == UP:
            self.speed += self.accel
            if self.speed > self.max_speed:
                self.speed = self.max_speed

        if key_pressed == LEFT:
            self.angle = (self.angle - self.omega) % (2 * math.pi)

        if key_pressed == RIGHT:
            self.angle = (self.angle + self.omega) % (2 * math.pi)

        if self.speed != 0:
            self.speed += self.air_resistance

    def shoot_cannon(self, size=8):
        cannon_speed = 20
        cannon_ang = self.angle
        cannon_pos = (self.pos[0] + self.width / 2, self.pos[1] + self.height / 2)
        new_cannon_ball = CannonBall(cannon_pos, cannon_ang, size, cannon_speed)
        self.conserve_momentum(new_cannon_ball)
        self.all_cannon_balls.add(new_cannon_ball)

    def conserve_momentum(self, cannon_ball):
        self.speed = self.speed - (cannon_ball.mass / self.mass) * cannon_ball.speed
