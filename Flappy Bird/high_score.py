import pygame,sys
import  pygame_menu
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
def high_score(screen1):
    global menu_font
    global screen
    screen =screen1
    menu_font = pygame.font.Font(None, 30)
    options = [Option("PLAY NOW", (100, 305)), Option("MENU", (290, 305))]
    running=True
    text_font = pygame.font.Font(None, 30)
    
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
        label=text_font.render("Top   8   Scores:", True,(255,255,255))
        screen.blit(label, (200, 0))
        label=text_font.render("Sl. No.", True,(255,255,255))
        screen.blit(label, (120, 30))
        label=text_font.render("|    Levels Cleared", True,(255,255,255))
        screen.blit(label, (250, 30))
        f=open("score.txt",'r').read()
        f1=f.split("\t")       
        a=[]
        for i in range(0,len(f1)):            
            if(f1!=" "):
                try:
                    a.append(int(f1[i].replace("\n","")))
                except:
                    pass
        a.sort(reverse=True)        
        disp=30
        label=text_font.render("--------------------------------------------------", True,(255,255,255))
        screen.blit(label, (100, 40))
        for i in range(0,8):
            if(i>=len(a)):
                break           
            label=text_font.render(str(i+1), True,(255,255,255))
            screen.blit(label, (120, 30+((i+1)*disp)))
            label=text_font.render("|    "+str(a[i]), True,(255,255,255))
            screen.blit(label, (250, 30+((i+1)*disp)))
            
        pygame.display.update()

if(__name__=='__main__'):
    pygame.init()
    screen = pygame.display.set_mode((520, 340))    
    high_score(screen)
