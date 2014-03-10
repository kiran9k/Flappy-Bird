import  pygame
import sys
import time
import random
import pygame_menu

def get_latest_rect(rectangles,rect_flag):
    for i in range(0,len(rectangles)):
        if(rect_flag[i]==1):
            if(rect_flag[(i+1)%len(rectangles)]==0):
                return (i+1)%len(rectangles)
    return -1

def removing_rect(rectangles,rect_flag,rect_width):
    for i in range(0,len(rectangles)):
        if (rect_flag[i]==1):
            if(rectangles[i][0][0]<-rect_width):
                rectangles[i][0][0]=-rect_width
                rectangles[i][1][0]=-rect_width
                rect_flag[i]=0
    return rectangles,rect_flag

def get_rect_near_ball(rectangles,rect_flag,ballrect):
    latest_pos=0
    previous=9999
    for i in range(0,len(rectangles)):
        if(rect_flag[i]==1):
            if(rectangles[i][0][0]+rectangles[i][0][2]>ballrect[0]):
                if(rectangles[i][0][0]<previous):
                    previous=rectangles[i][0][0]
                    latest_pos=i
    return latest_pos

    
def out_condition(ballrect,rectangles,rect_flag):
    x1=ballrect[0]
    y1=ballrect[1]+2
    x2=ballrect[2]+x1
    y2=ballrect[3]+y1
    if(y1<=2):
        return True
    #print(get_rect_near_ball(rectangles,rect_flag,ballrect))
    p=get_rect_near_ball(rectangles,rect_flag,ballrect)
    p1=rectangles[p][0][0]
    p2=rectangles[p][0][2]+p1
    q1=rectangles[p][0][1]
    q2=rectangles[p][0][3]
    ##case 1 upper left :
    if(p1<=x2 and ((q1<=y1 and y1<=q2) or (q1<=y2 and y2<=q2))):
        #print "case 1"
        return True    
    p1=rectangles[p][1][0]
    p2=rectangles[p][1][2]+p1
    q1=rectangles[p][1][1]
    q2=rectangles[p][1][3]

    #case 3 : LOwer side Left:
    if(p1<=x2 and ((q1<=y1 and y1<=q2) or (q1<=y2 and y2<=q2))):
        #print "case 3"
        return True
    return False
def print_score(score,screen):
    black=0,0,0
    screen.fill(black)
    if(score<1):
        score=0
    myfont = pygame.font.SysFont("monospace", 20)
    label = myfont.render("Congragulations! : Your score  : "+str(score-1), 1, (255,255,2))
    screen.blit(label, (30,130))
    pygame.display.flip()
    time.sleep(5)
def  start_game(screen,width,height):
    score=-1
    previous_rect_passed=-1
    speed = [0,10]
    speed1=[0,5]
    black = 0, 0, 0
    white=250, 250, 250
    
    total_rect=4
    rect_width=50
    rectangles=[[[0,0,rect_width,0]for row in range(2)] for x in range(total_rect)]
    rect_flag=[0for x in range(total_rect)]
    ball = pygame.image.load("bird.bmp")
    ball = pygame.transform.scale(ball, (40, 40))
    ballrect = ball.get_rect()
    running =True
    rectspeed=int(width/100)# actual 5
    median_spacing=150
    w=random.randint(50,height-median_spacing)
    rect=[width,0,30,w]
    next_rect_min=int(width*2/5)#actual 220
    rect1=0
    rect_flag[0]=1
    ball_pos=int(width/3)
    ballrect[0]=ball_pos
    rectangles[0][0]=[width,0,rect_width,w]
    rectangles[0][1]=[width,w+median_spacing,rect_width,height-w+median_spacing]
    #rect_flag[0]=True
    myfont1 = pygame.font.SysFont("monospace", 20,bold=True)
    while running:
        time.sleep(0.02)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                sys.exit()
        background = pygame.transform.scale(ball, (width,height))
        screen.blit(background,(0,ballrect[1],ballrect[2],ballrect[3]))
        screen.fill(black)
        for i in range(0,len(rectangles)):
            if(rect_flag[i]==1):
                rectangles[i][0][0]=rectangles[i][0][0]-rectspeed
                rectangles[i][1][0]=rectangles[i][1][0]-rectspeed
        ##get rectangle approcahing the bird
        pointer=get_latest_rect(rectangles,rect_flag)
        if(pointer!=previous_rect_passed):
            previous_rect_passed=pointer
            score+=1
        
        ##creating new rectangles    
        next_rect=next_rect_min#random.randint(next_rect_min,int(width/2))
        if(pointer>-1):
            if(width-rectangles[(pointer-1)%len(rect_flag)][0][0]>next_rect):
                #break;            
                w=random.randint(100,height-median_spacing)
                rectangles[pointer][0]=[width,0,rect_width,w]
                rectangles[pointer][1]=[width,w+median_spacing,rect_width,height-w+median_spacing]
                rect_flag[pointer]=1

        #deleting old rectangles
        rectangles,rect_flag=removing_rect(rectangles,rect_flag,rect_width)
    
        ## check if key is presssed   
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]or key[pygame.K_SPACE]:
            prev=ballrect
            if(speed[1]>0):
                speed[1]=-speed[1]
            if(ballrect[1]<10):
                ballrect[1]=30
            ballrect = ballrect.move(speed)
            
        else:
            ballrect=ballrect.move(speed1)
        if(ballrect[1]>=height-ballrect[3]+2):
            print " u lost"
            running =False
            print_score(score,screen)
            print "score is"+str(score-1)
            #sys.exit()
    
        ##check for out conditions
        
        if(out_condition(ballrect,rectangles,rect_flag)==True):        
            pygame.draw.rect(screen,white,[0,0,width,2], 0)
            pygame.draw.rect(screen,white,[0,height-2,width,2], 0)
            for i in range(0,len(rectangles)):
                pygame.draw.rect(screen,white, rectangles[i][0], 0)
                pygame.draw.rect(screen,white, rectangles[i][1], 0)
            running=False
            if(score<1):
                score=1
            print "score is:"+str(score-1)
            print_score(score,screen)
            #sys.exit()

         ##printing current rectangles
        pygame.draw.rect(screen,white,[0,0,width,2], 0)
        pygame.draw.rect(screen,white,[0,height-2,width,2], 0)
        for i in range(0,len(rectangles)):
            pygame.draw.rect(screen,white, rectangles[i][0], 0)
            pygame.draw.rect(screen,white, rectangles[i][1], 0)
        screen.blit(ball,ballrect)
        ##diplay score:
        if(score<1):
            label = myfont1.render("Score : 0", 1, (255,0,0))
        else:
            label = myfont1.render("Score : "+str(score-1), 2, (255,0,0))
        screen.blit(label, (width-120, 30))      
        pygame.display.flip()   

    #fp=open("score.txt",'a')
    if(score<1):
        score=1
    with open('score.txt', 'a') as f:
        f.write(str(score-1)+"\t")
    
    pygame_menu.start(screen)
    
    
if(__name__=='__main__'):
    pygame.init()
    size = width, height = 520, 340## minimum : 520,340
    screen = pygame.display.set_mode(size)
    start_game(screen,width,height)
