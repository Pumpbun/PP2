import pygame
from pygame.locals import *
import random, time
pygame.init()
pygame.mixer.init()

W, H = 400, 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (250, 250, 92)
speed = 5
score = 0
coin = 0
#fonts and texts
font = pygame.font.SysFont("Avenir", 60)
font_s = pygame.font.SysFont("Avenir", 20)
gameover = font.render("GAME OVER", True, black)
gameoverrect = gameover.get_rect()
gameoverrect.center = (W // 2, H // 2)
bg = pygame.image.load("street.png")
fps = pygame.time.Clock()
fps.tick(60)
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
sc.fill(white)
pygame.display.set_caption("Racer game") 
pygame.mixer.music.load("magic.mp3") #just background music
pygame.mixer.music.play()

#class for cars that are moving towars us
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > 600: 
            score += 1 #score increases as we drive past cars
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0) #cars appear randomly


#class for our playable car
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self): #keys to move out car
        pressedk = pygame.key.get_pressed()
        if pressedk[K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= 5
        if pressedk[K_RIGHT]:
            if self.rect.right < W:
                self.rect.x += 5


#class for coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0) #coins appear randomly

    def move(self):
        global coin
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

#setting up sprites
car = Car()
en = Enemy()


#creating sprites groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(en)
sprites = pygame.sprite.Group()
sprites.add(car)
sprites.add(en)

#adding a new user event
incrSpeed = pygame.USEREVENT + 1
spawnCoin = pygame.USEREVENT + 2
pygame.time.set_timer(incrSpeed, 1000)
pygame.time.set_timer(spawnCoin, 5000)

#game loop
while True:
    for event in pygame.event.get(): #cycling through all events occuring
        if event.type == pygame.QUIT:
            exit()
        if event.type == incrSpeed:
            speed += 0.5
        if event.type == spawnCoin:
            newCoin = Coin()
            coins.add(newCoin)
            sprites.add(newCoin)
    car.move()
    sc.blit(bg, (0, 0))
    scores = font_s.render("score: " + str(score), True, black)
    sc.blit(scores, (10, 10))
    coinstxt = font_s.render("coins: " + str(coin), True, black)
    sc.blit(coinstxt, (10, 35))

    #moves and re-draws all sprites
    for entity in sprites:
        sc.blit(entity.image, entity.rect)
        if isinstance(entity, (Enemy, Coin)):
            entity.move()

    #collision between enemies and our car
    if pygame.sprite.spritecollideany(car, enemies):
        pygame.mixer.music.pause()
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)
        sc.fill(red)
        sc.blit(gameover, (30, 250))
        pygame.display.update()
        for entity in sprites:
            entity.kill()
        
        time.sleep(2)
        pygame.quit()
    #collecting coins
    collected_coins = pygame.sprite.spritecollide(car, coins, True)
    if collected_coins:
        coin += len(collected_coins)
    pygame.display.update()
    fps.tick(60)   