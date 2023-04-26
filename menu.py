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

#arrumar atribuições de tamanho de tela, cores e posições para como padronizado em level.py
class Menu:
    def main_menu(self):
        # dictionary to map text surfaces to main_menu_figures
        main_menu_figures = {
            'start': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'),(240,60)),
            'help': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'),(120,60)),
            'quit': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'),(120,60))
        }
        
        screen = pygame.display.set_mode((WIDTH,HEIGHT))   # set the menu screen size
        font = pygame.font.SysFont('Rust',50)
        title = font.render('PIRATAS DA GUANABARA', True, 'Gray')
        font = pygame.font.SysFont('Arial', 36)
        start = font.render('Start Game', True, 'White')
        help = font.render('Help', True, 'White')
        quit = font.render('Quit', True, 'White')

        background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
        background = pygame.transform.scale(background, (WIDTH+130,HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 420 <= event.pos[0] <= 580 and 250 <= event.pos[1] <= 290:
                        return   
                    elif 470 <= event.pos[0] <= 530 and 380 <= event.pos[1] <= 420:
                        self.help_menu()
                    elif 470 <= event.pos[0] <= 530 and 510 <= event.pos[1] <= 550:
                        pygame.quit()
                        sys.exit()

            screen.fill((0, 0, 0))
            screen.blit(background,(0,0))
            title_rect = title.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title, title_rect)
            
            # blit the main_menu_figures behind the respective text surfaces when the mouse hovers over the text
            start_rect = start.get_rect(center=(WIDTH // 2, 270))
            if start_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(main_menu_figures['start'], (start_rect.x - 45, start_rect.y - 8))
            screen.blit(start, start_rect)
            
            help_rect = help.get_rect(center=(WIDTH // 2, 400))
            if help_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(main_menu_figures['help'], (help_rect.x - 30, help_rect.y - 8))
            screen.blit(help, help_rect)
            
            quit_rect = quit.get_rect(center=(WIDTH // 2, 530))
            if quit_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(main_menu_figures['quit'], (quit_rect.x - 33, quit_rect.y - 8))
            screen.blit(quit, quit_rect)

            pygame.display.update()


    def help_menu(self):

        help_menu_figures = {
            'back': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'),(120,60)),
        }

        screen = pygame.display.set_mode((WIDTH,HEIGHT))   
        font = pygame.font.SysFont('Arial',50)
        title = font.render('HELP', True, 'White')
        font = pygame.font.SysFont('Arial', 36)
        info = font.render('How to play: ...', True, 'White')
        back = font.render('Back', True, 'White')

        background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
        background = pygame.transform.scale(background, (WIDTH+130,HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

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
            if back_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(help_menu_figures['back'], (back_rect.x - 30, back_rect.y - 5))
            screen.blit(back, back_rect)

            pygame.display.update()
    
    def pause_menu(self):

        pause_menu_figures = {
            'resume': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'),(240,60)),
            'exit': pygame.transform.scale(pygame.image.load('data/PNG/Retina/Effects/explosion2.png'),(170,60)),
        }
        pygame.mixer.music.pause()
        screen = pygame.display.set_mode((WIDTH,HEIGHT))   
        font = pygame.font.SysFont('Arial',50)
        title = font.render('GAME PAUSE MENU', True, 'White')
        font = pygame.font.SysFont('Arial', 36)
        ## score_info = font.render('Current score: ...', True, 'White') #botar score aqui
        resume = font.render('Resume', True, 'White')
        exit = font.render('Exit', True, 'White')

        background = pygame.image.load('data/PNG/Retina/Menu/background.jpg')
        background = pygame.transform.scale(background, (WIDTH+130,HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 410 <= event.pos[0] <= 590 and 300 <= event.pos[1] <= 340:
                        screen.fill((135, 206, 250))
                        pygame.display.update()
                        pygame.mixer.music.unpause()
                        return
                    elif 410 <= event.pos[0] <= 590 and 460 <= event.pos[1] <= 500:
                        pygame.quit()
                        sys.exit()

            screen.fill((0, 0, 0))
            screen.blit(background,(0,0))
            title_rect = title.get_rect(center=(WIDTH // 2, 100))
            screen.blit(title, title_rect)
            ## score_info_rect = score_info.get_rect(center=(WIDTH // 2, 270)) 
            ##screen.blit(score_info, score_info_rect)

            resume_rect = resume.get_rect(center=(WIDTH // 2, 320))
            if resume_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(pause_menu_figures['resume'], (resume_rect.x - 60, resume_rect.y - 10))
            screen.blit(resume, resume_rect)

            exit_rect = exit.get_rect(center=(WIDTH // 2, 480))
            if exit_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(pause_menu_figures['exit'], (exit_rect.x - 60, exit_rect.y - 10))
            screen.blit(exit, exit_rect)

            pygame.display.update()
        

