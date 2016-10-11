import pygame, sys, time
from pygame.locals import *

pygame.init()

Width = 800
Height = 600

window = pygame.display.set_mode((Width, Height), 0, 32)

pygame.display.set_caption('Pong')

Black = (0, 0, 0)
White = (255, 255, 255)

Y1 = 200
Y2 = 200

Player1Score = 0
Player2Score = 0



while True:

    Pong1 = pygame.draw.rect(window, White, (50, Y1, 25, 100))
    Pong2 = pygame.draw.rect(window, White, (750, Y2, 25, 100))


    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        Y2 -= 0.25
        if Y2 == -1:
            Y2 = 0
    if keys[K_DOWN]:
        Y2 += 0.25
        if Y2 == 600:
            Y2 = 599
    if keys[K_w]:
        Y1 -= 0.25
        if Y1 == 600:
            Y1 = 599
    if keys[K_s]:
        Y1 += 0.25
        if Y1 == 600:
            Y1 = 599

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()