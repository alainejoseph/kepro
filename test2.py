import pygame,sys
from main import *


class button():
    def __init__(self,text,w,h,pos):
        self.pressed = False
        self.top_rect = pygame.Rect(pos,(w,h))
        self.top_color = "#475F77"
        self.text_color = (0,255,0)
        self.text = text
        
        self.text_surf = gui_font.render(text,True,(self.text_color))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(self.text_surf,self.text_rect)
        self.check()
    def check(self):
        i=0
        mousepos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mousepos):
            self.top_color = "#FFFFFF"
            if pygame.mouse.get_pressed()[2]:
                self.pressed= True
            else:
                
                if self.pressed == True:
                    if self.text=="start":
                        print("click 1")
                        i+=1
                        game = Game(500,500 )
                    if self.text == 'achivments':
                        print("click 2",)
                    if i==1:
                            self.pressed=False
        else:
            self.top_color = "#475F77"
                    
        
    
#


pygame.init()
screen = pygame.display.set_mode((500,500))
Clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)
button1 = button('start',200,40,(250,100))
button2= button('achivments',200,40,(250,150))
while True:
    for event in pygame.event.get():
        screen.fill("#475F77")
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        button1.draw()
        button2.draw()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("a")
                #s1()
            if event.key == pygame.K_s:
                print("s")
                #s2()
        pygame.display.update()