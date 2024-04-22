import sys

import pygame

class game:
    def __init__(self):      
        pygame.init()
        screen_width = 1280
        screen_height = 640
        
        pygame.display.set_caption('jogo')
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
        self.clock = pygame.time.Clock()
        
        self.img = pygame.image.load('cloud1.jpg')
        
        self.img_pos = [160,260]
        self.movement = [False,False]
    def run(self):
        while True:
            self.img_pos[1] += (self.movement[1] - self.movement[0])*5
            self.screen.blit(self.img, self.img_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)          
game().run()
            