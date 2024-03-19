import sys, pygame, datetime
pygame.init()
W, H = 1000, 800
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Mickey Mouse Clock")
x = W // 2
y = H // 2 
mickey = pygame.image.load("main-clock.png")
mickeyrect = mickey.get_rect(center = (x, y))
righthand = pygame.image.load("right-hand.png")
lefthand = pygame.image.load("left-hand.png")

def rotate(image, angle, center):
    r_image = pygame.transform.rotate(image, angle)
    new_rect = r_image.get_rect(center = center)
    sc.blit(r_image, new_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    time = datetime.datetime.now()
    seconds = time.second
    mins = time.minute
    langle = (seconds / 60) * 360
    rangle = (mins / 60) * 360
    langle = 90 - langle
    rangle = 90 - rangle
    sc.fill(WHITE)
    sc.blit(mickey, mickeyrect)
    rotate(lefthand, langle, mickeyrect.center)
    rotate(righthand, rangle, mickeyrect.center)
    pygame.display.update()