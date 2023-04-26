import pygame
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


# arrumar atribuições de tamanho de tela, cores e posições para como padronizado em level.py
class Menu:
    def __init__(self, background=None):
        if background:
            self.background = background
        else:
            background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
            self.background = pygame.transform.scale(background, (WIDTH + 130, HEIGHT))

    def main_menu(self):
        screen = pygame.display.set_mode((WIDTH,HEIGHT))   # set the menu screen size
        font = pygame.font.SysFont('Arial',50)
        title = font.render('Piratas da Guanabara', True, 'Gray')
        font = pygame.font.SysFont('Arial', 36)
        start = font.render('Start Game', True, 'White')
        help = font.render('Help', True, 'White')
        quit = font.render('Quit', True, 'White')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 420 <= event.pos[0] <= 580 and 250 <= event.pos[1] <= 290:
                        return    # start game
                    elif 470 <= event.pos[0] <= 530 and 350 <= event.pos[1] <= 390:
                        # display help screen
                        self.help_menu()
                    elif 470 <= event.pos[0] <= 530 and 450 <= event.pos[1] <= 490:
                        pygame.quit()
                        quit()    # quit the game
                    elif 420 <= event.pos[0] <= 580 and 470 <= event.pos[1] <= 510:
                        screen.blit(self.background, (0, 0))

            screen.fill((0, 0, 0))
            screen.blit(self.background,(0,0))
            title_rect = title.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title, title_rect)
            start_rect = start.get_rect(center=(WIDTH // 2, 270))
            screen.blit(start, start_rect)
            help_rect = help.get_rect(center=(WIDTH // 2, 370))
            screen.blit(help, help_rect)
            quit_rect = quit.get_rect(center=(WIDTH // 2, 470))
            screen.blit(quit, quit_rect)

            pygame.display.update()

    def help_menu(self):
        screen = pygame.display.set_mode((WIDTH,HEIGHT))   # set the menu screen size
        font = pygame.font.SysFont('Arial',50)
        title = font.render('Help', True, 'White')
        font = pygame.font.SysFont('Arial', 36)
        info = font.render('How to play: ...', True, 'White')
        back = font.render('Back', True, 'White')

        background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
        background = pygame.transform.scale(background, (WIDTH+130,HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 470 <= event.pos[0] <= 530 and 350 <= event.pos[1] <= 390:
                        return

            screen.fill((0, 0, 0))
            screen.blit(background,(0,0))
            title_rect = title.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title, title_rect)
            info_rect = info.get_rect(center=(WIDTH // 2, 270))
            screen.blit(info, info_rect)
            back_rect = back.get_rect(center=(WIDTH // 2, 370))
            screen.blit(back, back_rect)

            pygame.display.update()
    
    def pause_menu(self):
        screen = pygame.display.set_mode((WIDTH,HEIGHT))   # set the menu screen size
        font = pygame.font.SysFont('Arial',50)
        title = font.render('Pause menu', True, 'White')
        font = pygame.font.SysFont('Arial', 36)
        score_info = font.render('Current score: ...', True, 'White') #botar score aqui
        back = font.render('Back to game', True, 'White')

        background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
        background = pygame.transform.scale(background, (WIDTH+130,HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 410 <= event.pos[0] <= 590 and 350 <= event.pos[1] <= 390:
                        screen.blit(self.background,(0,0))
                        pygame.display.update()
                        return

            screen.fill((0, 0, 0))
            screen.blit(background,(0,0))
            title_rect = title.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title, title_rect)
            score_info_rect = score_info.get_rect(center=(WIDTH // 2, 270))
            screen.blit(score_info, score_info_rect)
            back_rect = back.get_rect(center=(WIDTH // 2, 370))
            screen.blit(back, back_rect)

            pygame.display.update()
        

