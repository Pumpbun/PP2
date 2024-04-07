import pygame
from colors import * #function related to color changing 
from math import sqrt
from functions import * #all used functions
pygame.init()

HEIGHT = 600
WIDTH = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')
new_layer = pygame.Surface((WIDTH, HEIGHT))
screen.fill(colorWHITE)

def rhombus_coordinates(x1, y1, x2, y2):
    return ((x2+((x1-x2)/2), y2), (x1, y2+((y1-y2)/2)), (x2+((x1-x2)/2), y1), (x2, y2+((y1-y2)/2)))

#coordinates
c_x = 0
c_y = 0
p_x = 0
p_y = 0

FPS = pygame.time.Clock()

#drawing modes
IfPressed = False
rect_mode = False
circle_mode = False
square_mode = False
r_triangle_mode = False
e_triangle_mode = False
rhombus_mode = False
#figure characteristics
color = False
THICKNESS = 2
COLOR = colorBLACK

while True:
    if not rect_mode and not circle_mode and not square_mode and not r_triangle_mode and not e_triangle_mode and not rhombus_mode:
        c_x = p_x #current point start at old point 
        c_y = p_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                rect_mode = not rect_mode
                circle_mode = False
                square_mode = False
                r_triangle_mode = False
                e_triangle_mode = False
                rhombus_mode = False
            if event.key == pygame.K_2:
                circle_mode = not circle_mode
                rect_mode = False
                square_mode = False
                r_triangle_mode = False
                e_triangle_mode = False
                rhombus_mode = False
            if event.key == pygame.K_3:
                square_mode = not square_mode
                rect_mode = False
                circle_mode = False
                r_triangle_mode = False
                e_triangle_mode = False
                rhombus_mode = False
            if event.key == pygame.K_4:
                r_triangle_mode = not r_triangle_mode
                square_mode = False
                rect_mode = False
                circle_mode = False
                e_triangle_mode = False
                rhombus_mode = False
            if event.key == pygame.K_5:
                e_triangle_mode = not e_triangle_mode
                square_mode = False
                rect_mode = False
                circle_mode = False
                r_triangle_mode = False
                rhombus_mode = False
            if event.key == pygame.K_6:
                rhombus_mode = not rhombus_mode
                square_mode = False
                rect_mode = False
                circle_mode = False
                r_triangle_mode = False
                e_triangle_mode = False
            if event.key == pygame.K_e:
                rect_mode = False
                circle_mode = False
                square_mode = False
                r_triangle_mode = False
                e_triangle_mode = False
                color = not color
#color changing
            if event.key == pygame.K_SPACE:
                COLOR = next_color()
            # changing THICKNESS
            if event.key == pygame.K_LEFT and THICKNESS>1:
                THICKNESS-=1
            if event.key == pygame.K_RIGHT:
                THICKNESS+=1
#mouse tracking
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            IfPressed = True
            p_x = event.pos[0]
            p_y = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            c_x = event.pos[0]
            c_y = event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            IfPressed = False
            new_layer.blit(screen, (0,0))
            if rect_mode and square_mode:
                pygame.draw.rect(screen, COLOR, rect_coordinates(c_x, c_y, p_x, p_y), THICKNESS)
#drawing line
    if not rect_mode and not circle_mode and not square_mode and not r_triangle_mode and not e_triangle_mode and not rhombus_mode:
        if IfPressed and color == False:
            pygame.draw.line(screen, COLOR, (p_x, p_y), (c_x, c_y), THICKNESS)
        if IfPressed and color == True:
            pygame.draw.line(screen, colorWHITE, (p_x, p_y), (c_x, c_y), THICKNESS)
        p_x = c_x
        p_y = c_y #assigning outdated current coordinates to old coordinates
    if IfPressed:
        if rect_mode:
            screen.blit(new_layer, (0,0))
            pygame.draw.rect(screen, COLOR, rect_coordinates(c_x, c_y, p_x, p_y), THICKNESS)
        if circle_mode:
            screen.blit(new_layer, (0,0))
            pygame.draw.circle(screen, COLOR, circle_centre(c_x, c_y, p_x, p_y), radius(c_x, c_y, p_x, p_y), THICKNESS)
        if square_mode:
            screen.blit(new_layer, (0,0))
            pygame.draw.rect(screen, COLOR, square_coordinates(c_x, c_y, p_x, p_y), THICKNESS)
        if r_triangle_mode:
            screen.blit(new_layer, (0,0))
            pygame.draw.polygon(screen, COLOR, right_triangle(c_x, c_y, p_x, p_y), THICKNESS)
        if e_triangle_mode:
            screen.blit(new_layer, (0,0))
            pygame.draw.polygon(screen, COLOR, equilateral_triangle(c_x, c_y, p_x, p_y), THICKNESS)
        if rhombus_mode:
            screen.blit(new_layer, (0,0))
            pygame.draw.polygon(screen, COLOR, rhombus_coordinates(c_x, c_y, p_x, p_y), THICKNESS)
    pygame.display.flip()
    FPS.tick(60)
        