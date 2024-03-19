import pygame
import sys
import os
pygame.init()
pygame.mixer.init()
# K_PAUSE, K_SPACE, K_LEFT, K_RIGHT
W, H = 600, 400
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("My fav songs")
songs = ["TXT_Ghosting.mp3", "TXT_Skipping_Stones.mp3", "TXT_Devil_By_The_Window.mp3"]
index = 0
flPause = flNext = flPrevious = False
if os.path.exists(songs[0]):
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play() 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if flPause:
                    pygame.mixer.music.unpause()
                    flPause = False
                else:
                    pygame.mixer.music.pause()
                    flPause = True
            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(songs)
                if os.path.exists(songs[index]):
                    pygame.mixer.music.load(songs[index])
                    pygame.mixer.music.play()
                    flNext = True
            elif event.key == pygame.K_LEFT:
                index = (index - 1) % len(songs)
                if os.path.exists(songs[index]):
                    pygame.mixer.music.load(songs[index])
                    pygame.mixer.music.play()
                    flPrevious = True
    sc.fill(WHITE)
    pygame.display.flip()