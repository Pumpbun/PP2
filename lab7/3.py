import pygame
pygame.init()
W, H = 600, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Red Ball")
clock = pygame.time.Clock()
fps = 60
x = W // 2
y = H // 2  
speed = 20
flLeft = flRight = flUp = flDown = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flUp = True
            elif event.key == pygame.K_DOWN:
                flDown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                flLeft = False
            elif event.key == pygame.K_RIGHT:
                flRight = False
            elif event.key == pygame.K_UP:
                flUp = False
            elif event.key == pygame.K_DOWN:
                flDown = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h 
            sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    if flLeft:
        x = max(x - speed, 0)
    elif flRight:
        x = min(x + speed, W)
    if flUp:
        y = max(y - speed, 0)
    elif flDown:
        y = min(y + speed, H)
    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), 25)
    pygame.display.update()
    clock.tick(fps)