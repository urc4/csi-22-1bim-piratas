"""Variables shared among many modules

"""
from itertools import product

WIDTH = 1000
HEIGHT = 800
FPS = 60
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
ENEMY_POS = [(tau1 * WIDTH, tau2 * HEIGHT) for tau1, tau2 in list(product([0.1, 0.2, 0.8, 0.9], repeat=2))]