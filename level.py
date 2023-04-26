"""Holds the Level class that contains important methods for the gameplay (e.g. update variables, scoreboard etc)

"""

import pygame
import os.path
from sys import stderr
from game_agents.enemy import Enemies
from game_agents.player import Player
from globals import WIDTH, HEIGHT, UP, RIGHT, LEFT, ENEMY_POS
from pygame.locals import (
    KEYDOWN,
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    KEYUP,
    K_DOWN,
    K_p
)
from scoreboard import Scoreboard
from game_agents.explosion import Explosion
from menu import Menu
from resources_utils import load_png

if not pygame.font:
    print("Warning, fonts disabled", file=stderr)


class Level:
    """Class wrapping all entities (player boat, enemies, cannonballs, etc), scoreboard, background, etc

    """
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Piratas da Guanabara")
        self.background = pygame.Surface(self.screen.get_size())
        ocean_tile, _ = load_png(os.path.join("PNG", "Retina", "Tiles", "tile_73.png"))
        land_tile, _ = load_png(os.path.join("PNG", "Retina", "Tiles", "tile_85.png"))
        tile_sz = 20
        ocean_tile = pygame.transform.scale(ocean_tile, (tile_sz, tile_sz))
        land_tile = pygame.transform.scale(land_tile, (tile_sz, tile_sz))
        for i in range(0, self.screen.get_size()[0], tile_sz):
            for j in range(0, self.screen.get_size()[1], tile_sz):
                self.background.blit(ocean_tile, (i, j))
        for pos in ENEMY_POS:
            self.background.blit(land_tile, pos)
        self.other_background = pygame.Surface(self.screen.get_size())  # to make ocean waves move
        for i in range(-tile_sz//2, self.screen.get_size()[0], tile_sz):
            for j in range(-tile_sz//2, self.screen.get_size()[1], tile_sz):
                self.other_background.blit(ocean_tile, (i, j))
        for pos in ENEMY_POS:
            self.other_background.blit(land_tile, pos)
        self.background = self.background.convert()
        self.other_background = self.other_background.convert()
        self.player = Player()
        self.player_sprite = pygame.sprite.RenderPlain(self.player)
        self.enemies = Enemies()
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        self.pressed_keys = set()
        self.power_up = False
        self.scoreboard = Scoreboard()
        self.explosions = pygame.sprite.Group()
        self.menu = Menu(self.background)
        self.game_over = False

    def display_full_background(self):
        """overwrite screen with game background (ocean)

        :return: None
        """
        self.screen.blit(self.background, (0, 0))

    def press_key(self, event):
        """ Handle user events

        :param event: pygame.event.Event
        :return: None
        """
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
                self.player.shoot_cannon(special=True)
                self.power_up = False
                self.scoreboard.power_up_counter = 0
            if event.key == K_p:  # added condition for "P" key
                self.menu.pause_menu()  # calling the pause_menu() function
        if event.type == KEYUP:
            for k, code in zip([K_UP, K_LEFT, K_RIGHT], [UP, LEFT, RIGHT]):
                if event.key == k and code in self.pressed_keys:
                    self.pressed_keys.remove(code)

    def generate_enemies(self):
        """ Randomly generates enemies

        :return: None
        """
        if self.scoreboard.score % 5 == 0:
            self.enemies.create_new_enemy(2)
            self.scoreboard.count += 60
        if self.scoreboard.score % 10 == 0:
            self.enemies.create_new_enemy(1)
            self.scoreboard.count += 60
        if self.scoreboard.power_up_counter == 900:
            self.power_up = True

    def change_background(self):
        """ Make ocean waves "move" in background and update self.background accordingly

        :return: None
        """
        if self.scoreboard.count % 60 == 0:
            self.background, self.other_background = self.other_background, self.background
            self.display_full_background()

    def blit_sprites(self):
        """ "Erases" sprites positions by overwriting their old positions with background

        :return: None
        """
        if len(self.pressed_keys) > 0:
            self.player.move(self.pressed_keys)
        else:
            self.player.move_unpressed()
        self.screen.blit(self.background, self.player.rect, self.player.rect)
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
        """ Utility that calls other functions to remove, move or, more generally, update the game sprites

        :return: None
        """
        if self.player is not None:
            self.player_sprite.update()
        self.destroy_player()
        self.destroy_enemies()
        self.destroy_explosions()
        self.player.all_cannon_balls.update()
        self.enemies.all_enemies.update()
        self.explosions.update()

    def draw_sprites(self):
        """ Draw sprites

        :return: None
        """
        self.player_sprite.draw(self.screen)
        self.player.all_cannon_balls.draw(self.screen)
        self.enemies.all_enemies.draw(self.screen)
        self.explosions.draw(self.screen)

    def destroy_enemies(self):
        """ Check which enemy boats should be destroyed due to cannonball collisions and remove them

        :return: None
        """
        for cannon_ball in self.player.all_cannon_balls:
            destroy_cannon_ball = False
            for enemy in self.enemies.all_enemies:
                if enemy.rect.colliderect(cannon_ball):
                    if enemy.lives == 1:
                        new_explosion = Explosion(enemy.pos)
                        self.explosions.add(new_explosion)
                        self.enemies.all_enemies.remove(enemy)
                        del enemy
                    else:
                        enemy.lives -= 1
                        enemy.change_image()
                    if not cannon_ball.special:  # destroy only normal/non-special cannon balls on collision
                        destroy_cannon_ball = True
            if destroy_cannon_ball:
                self.player.all_cannon_balls.remove(cannon_ball)
                del cannon_ball

    def destroy_player(self):
        """ Check if some enemy boat collided with player, and set a "Game Over" flag for the main game loop

        :return: None
        """
        for enemy in self.enemies.all_enemies:
            if enemy.rect.scale_by(0.6).colliderect(self.player.rect.scale_by(0.6)):
                self.game_over = True

    def destroy_explosions(self):
        """ Clear out explosions at end of their animation

        :return: None
        """
        for explosion in self.explosions:
            if explosion.finished:
                self.explosions.remove(explosion)
                del explosion

    def display_game_over(self):
        """ Display Game Over

        :return: None
        """
        if pygame.font:
            # "GAME OVER" message:
            font = pygame.font.Font(None, 64)
            text = font.render("GAME OVER", True, (245, 242, 66))
            textpos = text.get_rect(centerx=self.background.get_width() / 2, centery=self.background.get_height() / 2)
            self.screen.blit(text, textpos)
            # score:
            font = pygame.font.Font(None, 32)
            text = font.render(f"FINAL SCORE: {self.scoreboard.score}", True, (245, 242, 66))
            textpos = text.get_rect(centerx=self.background.get_width() / 2,
                                    centery=self.background.get_height() / 2 + 48)
            self.screen.blit(text, textpos)
            # restart message:
            font = pygame.font.Font(None, 32)
            text = font.render("PRESS ENTER TO PLAY AGAIN", True, (245, 242, 66))
            textpos = text.get_rect(centerx=self.background.get_width() / 2,
                                    centery=self.background.get_height() / 2 + 80)
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
