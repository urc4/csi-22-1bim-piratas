import pygame
from game_agents.enemy import Enemies
from game_agents.player import Player
from globals import WIDTH, HEIGHT, UP, RIGHT, LEFT
from pygame.locals import (
    KEYDOWN,
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    KEYUP,
    K_DOWN,
)
from scoreboard import Scoreboard
from game_agents.explosion import Explosion


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
        self.explosions = pygame.sprite.Group()

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
                self.player.all_cannon_balls.remove(cannon_ball)
            else:
                self.screen.blit(self.background, cannon_ball.rect, cannon_ball.rect)
        for enemy in self.enemies.all_enemies:
            self.screen.blit(self.background, enemy.rect, enemy.rect)

    def update_sprites(self):
        if self.player is not None:
            self.player_sprite.update()
        self.destroy_player()
        self.destroy_enemies()
        self.player.all_cannon_balls.update()
        self.enemies.all_enemies.update()
        self.explosions.update()

    def draw_sprites(self):
        self.player_sprite.draw(self.screen)
        self.player.all_cannon_balls.draw(self.screen)
        self.enemies.all_enemies.draw(self.screen)
        self.explosions.draw(self.screen)

    def destroy_enemies(self):
        for cannon_ball in self.player.all_cannon_balls:
            for enemy in self.enemies.all_enemies:
                if enemy.rect.colliderect(cannon_ball):
                    new_explosion = Explosion(enemy.pos)
                    self.explosions.add(new_explosion)
                    self.enemies.all_enemies.remove(enemy)
                    del enemy
                    # self.player.all_cannon_balls.remove(cannon_ball)
                    # ideia eh bola grandona nao ser destruida com contato
                    # del cannon_ball

    def destroy_player(self):
        for enemy in self.enemies.all_enemies:
            if enemy.rect.colliderect(self.player):
                # corrigir hitbox
                # del self.player
                pass


# ideia de codigo mais inteligivel aqui

# class Level:
#     def __init__(self):
#         self.enemies = pygame.sprite.Group()
#         self.cannon_balls = pygame.sprite.Group()

#     def update_sprites(self):
#         # Update sprites
#         self.enemies.update()
#         self.cannon_balls.update()

#         # Check for collisions
#         for enemy in self.enemies:
#             for cannon_ball in self.cannon_balls:
#                 if enemy.rect.colliderect(cannon_ball.rect):
#                     # Destroy enemy
#                     enemy.kill()
#                     # Destroy cannon ball
#                     cannon_ball.kill()

#     def destroy_enemies(self):
#         # Get a list of enemies and cannon balls that have collided
#         collided_enemies = pygame.sprite.groupcollide(self.enemies, self.cannon_balls, True, True)

#         # Destroy the collided enemies
#         for enemy in collided_enemies.keys():
#             enemy.kill()
