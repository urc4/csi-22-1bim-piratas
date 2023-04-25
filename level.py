import pygame
from sys import stderr
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

if not pygame.font:
    print("Warning, fonts disabled", file=stderr)


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
        self.pressed_keys = set()
        self.power_up = False
        self.scoreboard = Scoreboard()
        self.explosions = pygame.sprite.Group()
        self.game_over = False

    def press_key(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.pressed_keys.add(UP)
            if event.key == K_LEFT:
                self.pressed_keys.add(LEFT)
            if event.key == K_RIGHT:
                self.pressed_keys.add(RIGHT)
            if event.key == K_SPACE:
                self.player.shoot_cannon()
            if event.key == K_DOWN and self.power_up:
                self.player.shoot_cannon(32, 10)
                self.power_up = False
        if event.type == KEYUP:
            for k, code in zip([K_UP, K_LEFT, K_RIGHT], [UP, LEFT, RIGHT]):
                if event.key == k and code in self.pressed_keys:
                    self.pressed_keys.remove(code)

    def generate_enemies(self, score):
        if score % 5 == 0:
            self.enemies.create_new_enemy(2)
            self.scoreboard.count += 60
        if score % 10 == 0:
            self.enemies.create_new_enemy(1)
            self.scoreboard.count += 60
        if score % 15 == 0:
            self.power_up = True

    def blit_sprites(self):  # "apaga" a antiga posicao das sprites (na verdade sobrescreve com um pedaço do background)
        if len(self.pressed_keys) > 0:
            self.player.move(self.pressed_keys)
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
        for explosion in self.explosions:
            self.screen.blit(self.background, explosion.rect, explosion.rect)

    def update_sprites(self):
        if self.player is not None:
            self.player_sprite.update()
        self.destroy_player()
        self.destroy_enemies()
        self.destroy_explosions()
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
                self.game_over = True

    def destroy_explosions(self):
        for explosion in self.explosions:
            if explosion.finished:
                self.explosions.remove(explosion)
                del explosion

    def display_game_over(self):
        if pygame.font:
            font = pygame.font.Font(None, 64)
            text = font.render("GAME OVER", True, (245, 242, 66))
            textpos = text.get_rect(centerx=self.background.get_width() / 2, centery=self.background.get_height() / 2)
            self.screen.blit(text, textpos)

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
