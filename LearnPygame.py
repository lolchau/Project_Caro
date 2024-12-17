# import pygame, sys
# from pygame.locals import *
# import pygame
# pygame.init()

# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello world!')
# RED=(0,0,0)
# while True:
#     DISPLAYSURF.fill(RED)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 400 # Chiều dài cửa sổ
WINDOWHEIGHT = 300 # Chiều cao cửa sổ

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

pygame.init()

### Xác định FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Animation')

### Tạo surface và vẽ hình chiếc xe ###
car_x = 0 # Hoành độ của xe
carSurface = pygame.Surface((100, 50), SRCALPHA )
pygame.draw.polygon(carSurface, RED, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15)))
pygame.draw.circle(carSurface, GREEN, (15, 40), 10)
pygame.draw.circle(carSurface, GREEN, (85, 40), 10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(carSurface, (car_x, 100))

    ### Thay đổi vị trí xe ###
    car_x += 1
    if car_x + 100 > WINDOWWIDTH:
        car_x = WINDOWWIDTH - 100

    pygame.display.update()
    fpsClock.tick(FPS)