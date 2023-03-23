import pygame
import math
import random
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS


# TODO remover canhão no update quando destrói um navio ou quando sai da tela para diminuir tamanho do vetor
class CannonBall(pygame.sprite.Sprite):
    def __init__(self, pos, ang, size, speed):
        # super.__init__(groups)
        self.speed = speed
        self.color = (255, 0, 0)
        self.angle = ang
        self.size = size
        self.pos = (pos[0] - self.size / 2, pos[1] - self.size / 2)
        self.surface = pygame.Surface((self.size, self.size))

    def update(self):
        self.pos = (self.pos[0] + self.speed * math.cos(self.angle), self.pos[1] + self.speed * math.sin(self.angle))

    def is_out_of_screen(self):
        if (self.pos[0] > WIDTH + 2 * self.size or self.pos[0] < 0 - self.size):
            return True
        elif (self.pos[1] > HEIGHT + 2 * self.size or self.pos[1] < 0 - self.size):
            return True
        return False


class EnemyBoat(pygame.sprite.Sprite):
    def __init__(self):
        # super().__init__(groups)
        self.pos = (random.random() * WIDTH, random.random() * HEIGHT)
        self.width = 50
        self.height = 50
        self.speed = 2
        self.angle = random.random() * 2 * math.pi
        self.color = (255, 0, 0)
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.color)

    def update(self):
        self.pos = (self.pos[0] + self.speed * math.cos(self.angle), self.pos[1] + self.speed * math.sin(self.angle))


class EnemyPirate(pygame.sprite.Sprite):
    pass


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # super.__init__(groups) noa ta funcionadno nao sei pq
        self.pos = (WIDTH / 2, HEIGHT / 2)
        self.width = 25
        self.height = 40
        self.speed = 3
        self.max_speed = 6
        self.alpha = 0.1
        self.sigma = 5
        self.mass = self.sigma * self.width * self.height
        self.air_resistance_constant = 100
        self.accel = 0.1
        self.omega = 5
        self.angle = 3 * math.pi / 2
        self.color = (0, 255, 0)
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.color)
        self.cannon_balls = []

    # teria que ver comom fica com rotacao acho qeu basta adicionar o calculo em relacao ao angulo
    # poderia usar pos%width
    def switch_sides(self):
        if (self.pos[0] > WIDTH):
            self.pos = (0, self.pos[1])
        elif (self.pos[0] < 0):
            self.pos = (WIDTH, self.pos[1])
        if (self.pos[1] > HEIGHT):
            self.pos = (self.pos[0], 0)
        elif (self.pos[1] < 0):
            self.pos = (self.pos[0], HEIGHT)
        return self.pos

    def update_pressed(self, key_pressed):
        self.air_resistance = -self.air_resistance_constant * self.speed / self.mass
        if key_pressed == UP:
            self.speed += self.accel + self.air_resistance
            if (self.speed > self.max_speed):
                self.speed = self.max_speed
            self.pos = (
            self.pos[0] + self.speed * math.cos(self.angle), self.pos[1] + self.speed * math.sin(self.angle))
        if key_pressed == LEFT:
            # self.omega += self.alpha
            ang_deg = self.angle * 180 / math.pi;
            ang_deg = (ang_deg - self.omega) % 360;
            self.angle = ang_deg * math.pi / 180;
            self.pos = (
            self.pos[0] + self.speed * math.cos(self.angle), self.pos[1] + self.speed * math.sin(self.angle))

        if key_pressed == RIGHT:
            ang_deg = self.angle * 180 / math.pi;
            ang_deg = (ang_deg + self.omega) % 360;
            self.angle = ang_deg * math.pi / 180;
            self.pos = (
            self.pos[0] + self.speed * math.cos(self.angle), self.pos[1] + self.speed * math.sin(self.angle))

        self.pos = self.switch_sides()

    def update_unpressed(self):
        self.air_resistance = -self.air_resistance_constant * self.speed / self.mass

        self.omega = 5
        if self.speed != 0:
            self.speed += self.air_resistance
        self.pos = (self.pos[0] + self.speed * math.cos(self.angle), self.pos[1] + self.speed * math.sin(self.angle))

        self.pos = self.switch_sides()

    def create_cannon_ball(self):
        # talvez tenha q considersar o angulo para acahr o centro depois
        size = 15
        speed = 20
        ang = self.angle
        pos = (self.pos[0] + self.width / 2, self.pos[1] + self.height / 2)
        new_cannon_ball = CannonBall(pos, ang, size, speed)
        self.cannon_balls.append(new_cannon_ball)
        self.conserve_momentum(new_cannon_ball)

    def conserve_momentum(self, cannon_ball):
        # massa = densidade-superficial * area
        sigma_ball = 1
        mass_ball = sigma_ball * cannon_ball.size ** 2
        sigma_player = 5
        mass_player = sigma_player * self.width * self.height
        self.speed = self.speed - (mass_ball / mass_player) * cannon_ball.speed
        # nao pode deixar passar do max speed?