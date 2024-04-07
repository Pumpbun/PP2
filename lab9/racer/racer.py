import pygame
from pygame.locals import *
import random, time

pygame.init()
pygame.mixer.init()

W, H = 400, 600
black = (0, 0, 0)
red = (255, 0, 0)
yellow1 = (250, 250, 92)  # +1 coin
yellow2 = (255, 255, 0)   # +5 coins
white = (255, 255, 255)   # +5 coins
yellow3 = (255, 215, 0)   # +10 coins
speed = 5
score = 0
coin = 0
coin1_count = 0  # Count of type 1 coins
coin2_count = 0  # Count of type 2 coins
coin3_count = 0  # Count of type 3 coins

# Fonts and texts
font = pygame.font.SysFont("Avenir", 60)
font_s = pygame.font.SysFont("Avenir", 20)
gameover = font.render("GAME OVER", True, black)
gameoverrect = gameover.get_rect()
gameoverrect.center = (W // 2, H // 2)
bg = pygame.image.load("racer/street.png")
fps = pygame.time.Clock()
fps.tick(120)
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
sc.fill(white)
pygame.display.set_caption("Racer game")
pygame.mixer.music.load("racer/magic.mp3")  # Background music
pygame.mixer.music.play()

# Class for cars that are moving towards us
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global score, speed
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)
            if coin >= 50:  # Check if player earns 50 coins
                speed += 1  # Increase speed when 50 coins are earned

# Class for our playable car
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressedk = pygame.key.get_pressed()
        if pressedk[K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= 5
        if pressedk[K_RIGHT]:
            if self.rect.right < W:
                self.rect.x += 5

# Class for coins
class Coin1(pygame.sprite.Sprite):  # Type 1 coin
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(yellow1)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global coin
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

class Coin2(pygame.sprite.Sprite):  # Type 2 coin
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(yellow2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global coin
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

class Coin3(pygame.sprite.Sprite):  # Type 3 coin
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(yellow3)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global coin
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

# Setting up sprites
car = Car()
en = Enemy()

# Creating sprite groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(en)
sprites = pygame.sprite.Group()
sprites.add(car)
sprites.add(en)

# Adding new user events
incrSpeed = pygame.USEREVENT + 1
spawnCoin = pygame.USEREVENT + 2
pygame.time.set_timer(incrSpeed, 1000)
pygame.time.set_timer(spawnCoin, 5000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == incrSpeed:
            speed += 0.5
        if event.type == spawnCoin:
            # Randomly choose which type of coin to spawn
            coin_type = random.choice([Coin1, Coin2, Coin3])
            new_coin = coin_type()
            coins.add(new_coin)
            sprites.add(new_coin)
    
    car.move()
    sc.blit(bg, (0, 0))
    scores = font_s.render("Score: " + str(score), True, black)
    sc.blit(scores, (10, 10))
    coinstxt = font_s.render("Coins: " + str(coin), True, black)
    sc.blit(coinstxt, (10, 35))

    for entity in sprites:
        sc.blit(entity.image, entity.rect)
        if isinstance(entity, (Enemy, Coin1, Coin2, Coin3)):
            entity.move()

    if pygame.sprite.spritecollideany(car, enemies):
        # Game over logic
        pygame.mixer.music.pause()
        pygame.mixer.Sound("racer/crash.wav").play()
        time.sleep(0.5)
        sc.fill(red)
        sc.blit(gameover, (30, 250))
        pygame.display.update()
        for entity in sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
    
    # Collecting coins and updating counts
    collected_coins = pygame.sprite.spritecollide(car, coins, True)
    for collected_coin in collected_coins:
        if isinstance(collected_coin, Coin1):
            coin += 1
            coin1_count += 1
        elif isinstance(collected_coin, Coin2):
            coin += 5
            coin2_count += 1
        elif isinstance(collected_coin, Coin3):
            coin += 10
            coin3_count += 1

    pygame.display.update()
    fps.tick(120)
