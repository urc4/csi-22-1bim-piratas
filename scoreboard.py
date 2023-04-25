import pygame


class Scoreboard:
    def __init__(self):
        self.count = 0
        self.score = 0

    def tick(self):
        self.count += 1
        self.score = int(self.count / 60)

    def display(self):
        display_surface = pygame.display.get_surface()
        font = pygame.font.Font(None, 30)
        debug_surf = font.render(str(self.score), True, 'White')
        debug_rect = debug_surf.get_rect(topleft=(10, 10))
        pygame.draw.rect(display_surface, 'Black', debug_rect)
        display_surface.blit(debug_surf, debug_rect)

    def increase_difficulty(self):
        pass
