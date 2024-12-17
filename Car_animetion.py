import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 800 # Chiều dài cửa sổ
WINDOWHEIGHT = 800 # Chiều cao cửa sổ

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

pygame.init()

### Xác định FPS ###
FPS = 120
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Animation')

class Car():
    def __init__(self):
        self.x = 0 # Vị trí của xe
        self.y = 0
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = pygame.image.load('plane1.png')
    
    def draw(self): # Hàm dùng để vẽ xe
        DISPLAYSURF.blit(self.surface, (self.x, self.y))

    def update(self, moveLeft, moveRight, moveDown, moveUp): # Hàm dùng để thay đổi vị trí xe        
        if self.x + 100 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 100
        if self.y + 100 > WINDOWWIDTH:
            self.y = WINDOWWIDTH - 100
        if moveLeft == True:
            self.x -=4
        if moveRight == True:
            self.x +=4
        if moveDown == True:
            self.y +=4
        if moveUp == True:
            self.y -=4
        if self.x < 0:
            self.x = 0
        if self.y <0:
            self.y = 0
moveLeft = False
moveRight = False
moveDown = False
moveUp = False
car = Car()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True
            if event.key == K_DOWN:
                moveDown = True
            if event.key == K_UP:
                moveUp = True

        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False 
            if event.key == K_DOWN:
                moveDown = False
            if event.key == K_UP:
                moveUp = False
    
    DISPLAYSURF.fill(WHITE)
    
    car.draw()
    car.update(moveLeft,moveRight,moveDown,moveUp)

    pygame.display.update()
    fpsClock.tick(FPS)