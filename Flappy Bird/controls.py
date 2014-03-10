import pygame,sys
import pygame_menu 
import birdy
class Option:
    hovered = False
    #menu_font = pygame.font.Font(None, 40)
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
def controls(screen1):
    global menu_font
    global screen
    screen =screen1
    menu_font = pygame.font.Font(None, 30)
    options = [Option("PLAY NOW", (100, 305)), Option("MENU", (290, 305))]
    running=True
    text_font = pygame.font.Font(None, 40)
    
    while(running):
        
        #pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                sys.exit()
            pygame.event.pump()
        screen.fill((0, 0, 0))
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True              
                if(option.text=="PLAY NOW"):
                    if(pygame.mouse.get_pressed()[0]):
                        running=False
                        birdy.start_game(screen,520,340)
                elif (option.text=="MENU"):
                    if(pygame.mouse.get_pressed()[0]):
                        running=False                        
                        pygame_menu.start(screen)
            else:
                option.hovered = False
            option.draw()
        label=text_font.render("Use Space or Up Arrow key to ", True,(255,255,255))
        screen.blit(label, (30, 90))
        label=text_font.render("navigate bird against obstacles", True,(255,255,255))
        screen.blit(label, (30, 130))
        
        pygame.display.update()

if(__name__=='__main__'):
    pygame.init()
    screen = pygame.display.set_mode((520, 340))    
    controls(screen)
