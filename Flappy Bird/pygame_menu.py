import pygame
import sys
import controls
from birdy import start_game
import high_score
class Option:
    hovered = False
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
    def get_color(self):
        if self.hovered:
            return (255,255, 255)
        else:
            return (200, 10, 100)
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
def start(screen1):
    global screen
    screen=screen1
    global menu_font
    menu_font = pygame.font.Font(None, 30)
    #options = [Option("NEW GAME", (140, 115)), Option("HIGH SCORE", (140, 165)),
    #           Option("CONTROLS", (140, 215))]
    options = [Option("NEW GAME", (40, 300)), Option("HIGH SCORE", (200, 300)),
               Option("CONTROLS", (400, 300))]
    running =True
    ball = pygame.image.load("game.bmp")
    ball = pygame.transform.scale(ball, (460, 240))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                running=False
                sys.exit()
        pygame.event.pump()
        screen.fill((0, 0, 0))
        screen.blit(ball,[40,40,480,300])
        
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True                
                if(option.text=="NEW GAME"):
                    if(pygame.mouse.get_pressed()[0]):
                        running=False
                        print"1"
                        #controls.controls(screen)
                        start_game(screen,520,340)
                elif (option.text=="HIGH SCORE"):
                    if(pygame.mouse.get_pressed()[0]):
                        running=False
                        #print"2"
                        high_score.high_score(screen)
                elif (option.text=="CONTROLS"):
                    if(pygame.mouse.get_pressed()[0]):
                        running=False
                        print"3"
                        controls.controls(screen)
            else:
                option.hovered = False
            option.draw()
        pygame.display.update()
if(__name__=='__main__'):
    pygame.init()
    screen = pygame.display.set_mode((520, 340))
    start(screen)
    
