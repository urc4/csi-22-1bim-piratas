""" Holds Menu class

"""
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
import sys
import os.path


# arrumar atribuições de tamanho de tela, cores e posições para como padronizado em level.py
class Menu:
    """ class for creating and displaying menu

    """
    def __init__(self, background=None):
        if background:
            self.background = background
        else:
            background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
            self.background = pygame.transform.scale(background, (WIDTH + 130, HEIGHT))

    def main_menu(self):
        """ displays and manages main menu when game starts running

        :return: None
        """
        # dictionary to map text surfaces to main_menu_figures
        main_menu_figures = {
            'start': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'), (250, 60)),
            'help': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'), (350, 60)),
            'quit': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'), (460, 70))
        }
        screen = pygame.display.set_mode((WIDTH,HEIGHT))   # set the menu screen size
        font = pygame.font.SysFont('chiller',70)
        title = font.render('PIRATAS DA GUANABARA', True, (255,255,250))
        font = pygame.font.SysFont('Arial', 36)
        start = font.render('Start the battle', True, 'White')
        help = font.render('Help, I am sinking!', True, 'White')
        quit = font.render('Quit, the sea is not for me', True, 'White')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 405 <= event.pos[0] <= 595 and 250 <= event.pos[1] <= 290:
                        return
                    elif 380 <= event.pos[0] <= 620 and 380 <= event.pos[1] <= 420:
                        self.help_menu()
                    elif 335 <= event.pos[0] <= 665 and 530 <= event.pos[1] <= 570:
                        pygame.quit()
                        sys.exit()    # quit the game
                    # elif 420 <= event.pos[0] <= 580 and 470 <= event.pos[1] <= 510:
                    #     screen.blit(self.background, (0, 0))

            screen.fill((0, 0, 0))
            screen.blit(self.background,(0,0))
            title_rect = title.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title, title_rect)

            # blit the main_menu_figures behind the respective text surfaces when the mouse hovers over the text
            start_rect = start.get_rect(center=(WIDTH // 2, 270))
            if start_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(main_menu_figures['start'], (start_rect.x - 30, start_rect.y - 8))
            screen.blit(start, start_rect)

            help_rect = help.get_rect(center=(WIDTH // 2, 400))
            if help_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(main_menu_figures['help'], (help_rect.x - 50, help_rect.y - 8))
            screen.blit(help, help_rect)

            quit_rect = quit.get_rect(center=(WIDTH // 2, 550))
            if quit_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(main_menu_figures['quit'], (quit_rect.x - 63, quit_rect.y - 8))
            screen.blit(quit, quit_rect)

            pygame.display.update()

    def help_menu(self):
        """ Displays and manage help menu teaching how to play the game

        :return: None
        """
        # Set up the fonts
        title_font = pygame.font.SysFont('chiller', 60)
        info_font = pygame.font.SysFont('Arial', 25)
        space_font = pygame.font.SysFont('Times New Roman', 30)
        back_font = pygame.font.SysFont('Arial', 36)

        # Set up the symbols
        arrow_up = u"\u2191"
        arrow_down = u"\u2193"
        arrow_right = u"\u2192"
        arrow_left = u"\u2190"

        help_menu_figures = {
            'back': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'), (240, 60)),
        }

        screen = pygame.display.set_mode((WIDTH,HEIGHT))   # set the menu screen size
        title = title_font.render('HELP, I AM SINKING!', True, 'White')
        # left side of help_menu
        keyboard_info = back_font.render('Keyboard commands:', True, 'White')
        move_front_info = info_font.render(f"Press {arrow_up} to move forward", True, 'White')
        move_right_info = info_font.render(f"Press {arrow_right} to move to the right", True, 'White')
        move_left_info = info_font.render(f"Press {arrow_left} to move to the left", True, 'White')
        shoot_cannon_info1 = info_font.render('Press', True, 'White')
        shoot_cannon_info2 = space_font.render('space', True, 'White')
        shoot_cannon_info3 = info_font.render('to fire the normal cannon', True, 'White')
        shoot_special_cannon_info = info_font.render(f"Press {arrow_down} to fire the special cannon (when loaded)",
                                                     True, 'White')
        pause_info = info_font.render('Press P to pause the game', True, 'White')

        # right side of help_menu
        back = back_font.render('Back to battle', True, 'White')

        background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
        background = pygame.transform.scale(background, (WIDTH+130,HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 410 <= event.pos[0] <= 590 and HEIGHT - 110 <= event.pos[1] <= HEIGHT - 70:
                        return

            screen.fill((0, 0, 0))
            screen.blit(background,(0,0))
            title_rect = title.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title, title_rect)
            keyboard_info_rect = keyboard_info.get_rect(center=(WIDTH // 4, 220))
            screen.blit(keyboard_info, keyboard_info_rect)
            move_front_info_rect = move_front_info.get_rect(center=(WIDTH // 4, 270))
            screen.blit(move_front_info, move_front_info_rect)
            move_right_info_rect = move_right_info.get_rect(center=(WIDTH // 4, 320))
            screen.blit(move_right_info, move_right_info_rect)
            move_left_info_rect = move_left_info.get_rect(center=(WIDTH // 4, 370))
            screen.blit(move_left_info, move_left_info_rect)

            screen.blit(shoot_cannon_info1, (50, 400))
            screen.blit(shoot_cannon_info2, (shoot_cannon_info1.get_width() + 60, 397))
            screen.blit(shoot_cannon_info3, (shoot_cannon_info1.get_width() + shoot_cannon_info2.get_width() + 70, 400))

            shoot_special_cannon_info_rect = shoot_special_cannon_info.get_rect(center=(WIDTH // 4, 460))
            screen.blit(shoot_special_cannon_info, shoot_special_cannon_info_rect)

            pause_info_rect = pause_info.get_rect(center=(WIDTH // 4, 505))
            screen.blit(pause_info, pause_info_rect)

            back_rect = back.get_rect(center=(WIDTH // 2, HEIGHT - 90))
            if back_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(help_menu_figures['back'], (back_rect.x - 35, back_rect.y - 5))
            screen.blit(back, back_rect)

            pygame.display.update()
    
    def pause_menu(self):
        """ Displays and manages pause menu that user can access anytime during gameplay

        :return: None
        """
        pause_menu_figures = {
            'resume': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'), (400, 60)),
            'help': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'), (350, 60)),
            'exit': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'), (300, 60)),
        }
        if os.path.isfile('data/Audio/background.mp3'):
            pygame.mixer.music.pause()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        font = pygame.font.SysFont('chiller', 60)
        title = font.render('PAUSE, I NEED A BIT OF RUM', True, 'White')
        font = pygame.font.SysFont('Arial', 36)
        resume = font.render('Resume the battle', True, 'White')
        help = font.render('Help, I am sinking!', True, 'White')
        exit = font.render('Exit the battle', True, 'White')

        background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
        background = pygame.transform.scale(background, (WIDTH+130,HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 350 <= event.pos[0] <= 650 and 250 <= event.pos[1] <= 290:
                        screen.blit(self.background,(0,0))
                        pygame.display.update()
                        if os.path.isfile('data/Audio/background.mp3'):
                            pygame.mixer.music.unpause()
                        return
                    elif 380 <= event.pos[0] <= 620 and 380 <= event.pos[1] <= 420:
                        self.help_menu()
                    elif 390 <= event.pos[0] <= 610 and 530 <= event.pos[1] <= 570:
                        pygame.quit()
                        sys.exit()

            screen.fill((0, 0, 0))
            screen.blit(background,(0,0))
            title_rect = title.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title, title_rect)

            resume_rect = resume.get_rect(center=(WIDTH // 2, 270))
            if resume_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(pause_menu_figures['resume'], (resume_rect.x - 50, resume_rect.y))
            screen.blit(resume, resume_rect)

            help_rect = help.get_rect(center=(WIDTH // 2, 400))
            if help_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(pause_menu_figures['help'], (help_rect.x - 50, help_rect.y - 8))
            screen.blit(help, help_rect)

            exit_rect = exit.get_rect(center=(WIDTH // 2, 550))
            if exit_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(pause_menu_figures['exit'], (exit_rect.x - 45, exit_rect.y))
            screen.blit(exit, exit_rect)

            pygame.display.update()
        

