import pygame 
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set the screen dimensions and FPS
W, H = 1200, 800
FPS = 60

# Create the game screen
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
bg = (0, 0, 0)

# Load and play the background music
pygame.mixer.music.load("arkanoid/music.mp3")
pygame.mixer.music.play()

# Define paddle attributes
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Define ball attributes
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Define game score attributes
game_score = 0
game_score_fonts = pygame.font.SysFont('Arcade Classic', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Load collision sound
collision_sound = pygame.mixer.Sound('arkanoid/catch.mp3')

# Define collision detection function
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Define block class
class Block:
    def __init__(self, block_rect, color_list, unbreakable=False, bonus=False):
        self.rect = block_rect
        self.color = color_list
        self.unbreakable = unbreakable
        self.bonus = bonus
        self.num_hits = 3 if bonus else 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color[0], self.rect)

    def hit(self):
        if not self.unbreakable:
            self.num_hits -= 1
            if self.num_hits == 0:
                if self.bonus:
                    return self.handle_bonus()
                else:
                    return True
        return False

    def handle_bonus(self):
        global ballRadius
        ballRadius += 5  # Increase ball size
        return True

# Create blocks
block_list = []
for i in range(10):
    for j in range(4):
        block_rect = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
        unbreakable = (i % 3 == 0)
        bonus = (i % 6 == 0 and j % 2 == 0)
        if unbreakable:
            color_list = (230, 230, 250)
        elif bonus:
            color_list = (220, 20, 60)
        else:
            color_list = [(random.randrange(0, 255), random.randrange(0, 255),  random.randrange(0, 255))] 
        block_list.append(Block(block_rect, color_list, unbreakable, bonus))

# Define game over screen
losefont = pygame.font.SysFont('Arcade Classic', 40)
losetext = losefont.render('GAME OVER', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Define win screen
winfont = pygame.font.SysFont('Arcade Classic', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Set up timer events
incrSpeed = pygame.USEREVENT + 1
shrinkPaddle = pygame.USEREVENT + 2
pygame.time.set_timer(incrSpeed, 2000)
pygame.time.set_timer(shrinkPaddle, 2000)

# Define main menu class
class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pygame.image.load('arkanoid/ark.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (W, H))
        self.font = pygame.font.SysFont('Upheaval TT BRK Font', 40)
        self.start_button_rect = pygame.Rect(W // 2 - 100, H // 2 - 50, 300, 100)
        self.start_button_text = self.font.render('press ENTER to start', True, (255, 255, 255))
        self.start_button_text_rect = self.start_button_text.get_rect(center=self.start_button_rect.center)

    def render(self):
        self.screen.blit(self.bg_image, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 150), self.start_button_rect)
        self.screen.blit(self.start_button_text, self.start_button_text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    return True  # Start button clicked
        return False

# Define pause button class
class Button:
    def __init__(self, image_path, pos):
        self.image = pygame.image.load("arkanoid/pause.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.clicked = False

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Space key
                self.clicked = True

# Create pause button instance
pause_button = Button("arkanoid/pause.png", (10, 10))

# Create main menu instance
main_menu = MainMenu(screen)
in_menu = True

# Main game loop
start_game = False
paused = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Space key
                if start_game:  # Check if the game has started
                    paused = not paused  # Toggle pause state
                    pygame.mixer.music.pause()  # Pause the background music
                    pygame.mixer.Sound("arkanoid/start.mp3").play()  # Play pause sound

if start_game:
    if not paused:
        # Render pause button
        pause_button.render(screen)

        main_menu.render()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == incrSpeed:
                ballSpeed += 0.5
            if event.type == shrinkPaddle:
                paddleW -= 5  # Decrease paddle width
                paddle.width = paddleW
            pause_button.handle_events(event)

        # Inside the game loop
        screen.fill(bg)
        
        # Render pause button
        pause_button.render(screen)
        
        for block in block_list:
            block.draw(screen)
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

        # Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        # Collision left 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        # Collision top
        if ball.centery < ballRadius + 50: 
            dy = -dy
        # Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        # Collision blocks
        hitIndex = ball.collidelist([block.rect for block in block_list])

        if hitIndex != -1:
            block = block_list[hitIndex]
            if block.unbreakable:
                dx, dy = detect_collision(dx, dy, ball, block.rect)
            else:
                dx, dy = detect_collision(dx, dy, ball, block.rect)
                if block.hit():
                    block_list.pop(hitIndex)
                    game_score += 1
                    collision_sound.play()

        # Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
        
        # Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
        elif not len(block_list):
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)
            
        # Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

    else:
        # Render pause screen
        pause_screen_text = pause_font.render('Paused', True, (255, 255, 255))
        pause_screen_rect = pause_screen_text.get_rect(center=(W // 2, H // 2))
        screen.blit(pause_screen_text, pause_screen_rect)

else:
    # Render main menu
    main_menu.render()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter key
                pygame.mixer.music.pause()
                pygame.mixer.Sound("arkanoid/start.mp3").play()
                start_game = True

pygame.display.flip()
clock.tick(FPS)