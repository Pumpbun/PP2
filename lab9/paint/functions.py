import pygame
from math import sqrt

#for circle
def radius(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
def circle_centre(x1, y1, x2, y2):
    return (min(x1,x2)+(abs(x1-x2)/2), min(y1,y2)+(abs(y1-y2)/2))

#for rect
def rect_coordinates(x1, y1, x2, y2):
    return pygame.Rect(min(x1,x2), min(y1,y2), abs(x1-x2), abs(y1-y2))

#for square
def square_coordinates(x1, y1, x2, y2):
    return pygame.Rect(min(x1,x2), min(y1,y2), abs(x1-x2), abs(x1-x2))

#for right triangle
def right_triangle(x1, y1, x2, y2):
    return ((x2, y2), (x1+(x2-x1), y1), (x1,y1+(y2-y1)))

#for equilateral triangle
def equilateral_triangle(x1, y1, x2, y2):
    return ((x2, y2), (x1, y2), ((x1+x2)/2, y1))

#for rhombus
def rhombus_coordinates(x1, y1, x2, y2):
    return ((x2+((x1-x2)/2), y2), (x1, y2+((y1-y2)/2)), (x2+((x1-x2)/2), y1), (x2, y2+((y1-y2)/2)))