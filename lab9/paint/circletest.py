import pygame
from math import sqrt
from colors import *
pygame.init()

HEIGHT = 600
WIDTH = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')
new_layer = pygame.Surface((WIDTH, HEIGHT))
screen.fill(colorWHITE)
#coordinates
c_x = 0
c_y = 0
p_x = 0
p_y = 0

def radius(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
def circle_centre(x1, y1, x2, y2):
    return (min(x1,x2)+(abs(x1-x2)/2), min(y1,y2)+(abs(y1-y2)/2))
FPS = pygame.time.Clock()
IfPressed = False
circle_mode = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                circle_mode = not circle_mode
        if event.type == pygame.MOUSEBUTTONDOWN:
            IfPressed = True
            p_x = event.pos[0]
            p_y = event.pos[1]
            print(event.pos[0], event.pos[1])
        if event.type == pygame.MOUSEBUTTONUP:
            IfPressed = False
            new_layer.blit(screen, (0,0))
        
            
        if event.type == pygame.MOUSEMOTION:
            c_x = event.pos[0]
            c_y = event.pos[1]
    if IfPressed:
        if circle_mode:
            screen.blit(new_layer, (0,0))
            pygame.draw.circle(screen, colorBLACK, circle_centre(c_x, c_y, p_x, p_y), radius(c_x, c_y, p_x, p_y), 5)
    pygame.display.flip()
    FPS.tick(60)