import pygame,sys
from main import *

class mainwin():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.Clock = pygame.time.Clock()
        self.gui_font = pygame.font.Font(None,30)
        self.button1 = button('start',200,40,(250,100))
        self.button2= button('achivments',200,40,(250,150))
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
                
class button():
    def __init__(self,text,w,h,pos):
        self.pressed = False
        self.top_rect = pygame.Rect(pos,(w,h))
        self.top_color = "#475F77"
        self.text_color = (0,255,0)
        self.text = text
        main2  = mainwin()
        
        self.text_surf = main2.gui_font.render(text,True,(self.text_color))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    def draw(self):
        pygame.draw.rect(main2.screen,self.top_color,self.top_rect)
        main2.screen.blit(self.text_surf,self.text_rect)
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
                    
        
main = mainwin()