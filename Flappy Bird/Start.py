import pygame
import pygame_menu
if(__name__=="__main__"):
    pygame.init()
    screen = pygame.display.set_mode((520, 340))
    pygame.display.set_caption(" Flappy Bird")
    pygame_menu.start(screen)
