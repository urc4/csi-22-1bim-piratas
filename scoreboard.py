"""Holds Scoreboard class

"""
import pygame


class Scoreboard:
    """Class responsible for tracking and displaying punctuation and "Special Cannonball" loading bar

    """
    def __init__(self):
        self.count = 0
        self.score = 0
        self.power_up_counter = 0
        self.fullloadbar = pygame.Rect(400, 13, 900 // 10, 15)

    def tick(self):
        """ update "inner clock", score, and "Special Cannonball" charge

        :return: None
        """
        self.count += 1
        self.score = int(self.count / 60)
        self.power_up_counter = min(900, self.power_up_counter + 1)

    def display(self):
        """ Display scoreboard and auxiliary info

        :return: None
        """
        display_surface = pygame.display.get_surface()
        font = pygame.font.Font(None, 30)
        LIGHT_BROWN = (156, 152, 60)
        DARK_BROWN = (156, 76, 30)
        # score
        text = font.render(f"Score: {str(self.score)}", True, DARK_BROWN)
        textpos = text.get_rect(topleft=(10, 10))
        pygame.draw.rect(display_surface, (135, 206, 250), textpos)  # overwrite with background color
        display_surface.blit(text, textpos)
        # power up
        loadbar = pygame.Rect(400, 13, self.power_up_counter // 10, 15)
        if self.power_up_counter == 900:
            text = font.render(f"Special cannonball:", True, DARK_BROWN)
            textpos = text.get_rect(topleft=(200, 10))
            pygame.draw.rect(display_surface, (135, 206, 250), textpos)  # overwrite with background color
            display_surface.blit(text, textpos)
            pygame.draw.rect(display_surface, (135, 206, 250), self.fullloadbar)  # overwrite with background color
            pygame.draw.rect(display_surface, DARK_BROWN, loadbar)
        else:
            text = font.render(f"Special cannonball:", True, LIGHT_BROWN)
            textpos = text.get_rect(topleft=(200, 10))
            pygame.draw.rect(display_surface, (135, 206, 250), textpos)  # overwrite with background color
            display_surface.blit(text, textpos)
            pygame.draw.rect(display_surface, (135, 206, 250), self.fullloadbar)  # overwrite with background color
            pygame.draw.rect(display_surface, LIGHT_BROWN, loadbar)
        # remind of pause button
        text = font.render(f"[P] - pause game", True, DARK_BROWN)
        textpos = text.get_rect(topleft=(800, 10))
        pygame.draw.rect(display_surface, (135, 206, 250), textpos)  # overwrite with background color
        display_surface.blit(text, textpos)

    def increase_difficulty(self):
        """ unused

        :return: None
        """
        pass
