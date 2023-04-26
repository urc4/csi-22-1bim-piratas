""" Holds our class Sprite which inherits form pygame.sprite.Sprite

"""
import pygame
import math
from resources_utils import load_png, spawn_random
from globals import WIDTH, HEIGHT
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS

# from cannonball import CannonBall


class Sprite(pygame.sprite.Sprite):
    """Custom child class of pygame.sprite.Sprite with added utilities for initializing and updates our sprites"""
    def __init__(self, model):
        """Initializes an  object from specifications

        :param model: dict
        """
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

        self.air_resistance_constant = 100

    def rotate_image(self):
        """ Rotate the object's Surface

        :return: Note
        """
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
        """ Update position and angle of object's Surface and rectangle

        :return: None
        """
        self.pos = (
            self.pos[0] + self.speed * math.cos(self.angle),
            self.pos[1] + self.speed * math.sin(self.angle),
        )
        self.rect.update(self.pos[0], self.pos[1], self.width, self.height)
        self.rotate_image()
        self.pos = self.switch_sides()
        # essa linha que gera tudo isso

    def is_out_of_screen(self):
        """Check if object is out of game screen boundaries

        :return: bool
        """
        if self.pos[0] > WIDTH + 2 * self.size or self.pos[0] < 0 - self.size:
            return True
        elif self.pos[1] > HEIGHT + 2 * self.size or self.pos[1] < 0 - self.size:
            return True
        return False

    def switch_sides(self):
        """Allows implementing infinite screen effect by computing new position of object on the other side

        :return: (float/int, float/int)
        """
        if self.pos[0] > WIDTH:
            self.pos = (0, self.pos[1])
        elif self.pos[0] < 0:
            self.pos = (WIDTH, self.pos[1])
        if self.pos[1] > HEIGHT:
            self.pos = (self.pos[0], 0)
        elif self.pos[1] < 0:
            self.pos = (self.pos[0], HEIGHT)
        return self.pos

    def move(self, pressed_keys):
        """Update speed and angle according to basic Physics and user events

        :param pressed_keys:
        :return: None
        """
        self.air_resistance = -self.air_resistance_constant * self.speed / self.mass
        if UP in pressed_keys:
            # self.speed += self.accel + self.air_resistance
            self.speed += self.accel
            if self.speed > self.max_speed:
                self.speed = self.max_speed

        if LEFT in pressed_keys:
            self.angle = (self.angle - self.omega) % (2 * math.pi)

        if RIGHT in pressed_keys:
            self.angle = (self.angle + self.omega) % (2 * math.pi)

        if self.speed != 0:
            self.speed += self.air_resistance

    def move_unpressed(self):
        """Manage movement when user releases the key of moving forward

        :return: None
        """
        self.air_resistance = -self.air_resistance_constant * self.speed / self.mass

        if self.speed != 0:
            self.speed += self.air_resistance
