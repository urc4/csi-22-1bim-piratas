import pygame
from enemy import Enemies
from player import Player
from globals import WIDTH, HEIGHT, UP, DOWN, RIGHT, LEFT, FPS
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    KEYUP,
    K_DOWN,
)

from scoreboard import Scoreboard


class Level:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Piratas da Guanabara")
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((135, 206, 250))
        self.player = Player()
        self.player_sprite = pygame.sprite.RenderPlain(self.player)
        self.enemies = Enemies()
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        self.is_pressed = False
        self.key_pressed = None
        self.power_up = False
        self.scoreboard = Scoreboard()

    def press_key(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.key_pressed = UP
                self.is_pressed = True
            if event.key == K_LEFT:
                self.key_pressed = LEFT
                self.is_pressed = True
            if event.key == K_RIGHT:
                self.key_pressed = RIGHT
                self.is_pressed = True
            if event.key == K_SPACE:
                self.player.shoot_cannon()
            if event.key == K_DOWN and self.power_up == True:
                size = 32
                self.player.shoot_cannon(32, 10)
                self.power_up = False
        if event.type == KEYUP:
            self.is_pressed = False

    def generate_enemies(self, score):
        if score % 5 == 0:
            self.enemies.create_new_enemy(2)
            self.scoreboard.count += 60
        if score % 10 == 0:
            self.enemies.create_new_enemy(1)
            self.scoreboard.count += 60
        if score % 15 == 0:
            self.power_up = True

    def blit_sprites(self):
        if self.is_pressed:
            self.player.move(self.key_pressed)
        else:
            self.player.move_unpressed()
        self.screen.blit(self.background, self.player.rect)
        for cannon_ball in self.player.all_cannon_balls:
            if cannon_ball.is_out_of_screen():
                pass
            else:
                self.screen.blit(self.background, cannon_ball.rect, cannon_ball.rect)
        for enemy in self.enemies.all_enemies:
            self.screen.blit(self.background, enemy.rect, enemy.rect)

    def update_sprites(self):
        self.player_sprite.update()
        self.player.all_cannon_balls.update()
        self.enemies.all_enemies.update()

    def draw_sprites(self):
        self.player_sprite.draw(self.screen)
        self.player.all_cannon_balls.draw(self.screen)
        self.enemies.all_enemies.draw(self.screen)
