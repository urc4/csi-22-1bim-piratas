""" This module contains some miscellaneous utilities used by many other modules

"""
import os
import pygame
import random
import math
from globals import WIDTH, HEIGHT


def load_png(name):
    """Load image and return image object

    :return: Surface, Rect
    """
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()


def get_random_angle(min_ang, max_ang):
    """ Get a random angle

    :param min_ang: float
    :param max_ang: float
    :return: float
    """
    return min_ang + random.random() * (max_ang - min_ang)


def spawn_random():
    """ Get random position and angle e.g. for a new enemy boat

    :return: (float, float), float (we may get an int instead of float somewhere, e.g. (int, float), float)
    """
    border = math.floor(random.random() * 4)
    if border == 0:  # UP
        ang = get_random_angle(0, math.pi)
        pos = (random.random() * WIDTH, 0)
        return (pos, ang)
    elif border == 1:  # RIGHT
        ang = get_random_angle(math.pi / 2, 3 * math.pi / 2)
        pos = (WIDTH, random.random() * HEIGHT)
        return (pos, ang)
    elif border == 2:  # DOWN
        ang = get_random_angle(math.pi, 2 * math.pi)
        pos = (HEIGHT, random.random() * WIDTH)
        return (pos, ang)
    else:  # LEFT
        ang = get_random_angle(3 * math.pi / 2, 5 * math.pi / 2)
        pos = (0, random.random() * HEIGHT)
        return (pos, ang)
