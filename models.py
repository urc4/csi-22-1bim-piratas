import pygame
import math
import random
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from resources_utils import load_png, spawn_random


# TODO remover canhão no update quando destrói um navio ou quando sai da tela para diminuir tamanho do vetor
#   (ver pygame.event.pump())
