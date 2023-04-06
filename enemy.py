import pygame
import math
from resources_utils import load_png, spawn_random


class EnemyBoat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 50
        self.image, self.rect = load_png("ship (8).png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        angle_offset = (
            math.pi / 2
        )  # XXX este parâmetro depende da sprite (para caso não aponte na direção (1,0))
        self.image = pygame.transform.rotate(self.image, angle_offset * 180 / math.pi)
        self.original_image = self.image  # para as rotinas que rotacionam o navio
        self.pos, self.angle = spawn_random()

        self.speed = 2
        self.surface = pygame.Surface((self.width, self.height))

    def __rotate_img(self):
        # SEMPRE rotacionar a partir da imagem ORIGINAL senao a imagem fica arbitrariamente distorcida
        # (dica frequente em tutoriais e fóruns)
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
        self.__rotate_img()


# can make class enemy to inherit for both
class EnemyPirate(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 15
        self.height = 20
        self.image, self.rect = load_png("dinghyLarge1.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        angle_offset = math.pi / 2
        self.image = pygame.transform.rotate(self.image, angle_offset * 180 / math.pi)
        self.original_image = self.image
        self.pos, self.angle = spawn_random()
        self.speed = 2.5
        self.surface = pygame.Surface((self.width, self.height))

    def __rotate_img(self):
        if not (0 <= self.angle < 2 * math.pi):
            self.angle %= 2 * math.pi
        self.image = pygame.transform.rotate(
            self.original_image, -180 * self.angle / math.pi
        )
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def update(self):
        self.pos = (
            self.pos[0] + self.speed * math.cos(self.angle),
            self.pos[1] + self.speed * math.sin(self.angle),
        )
        self.rect.update(self.pos[0], self.pos[1], self.width, self.height)
        self.__rotate_img()
