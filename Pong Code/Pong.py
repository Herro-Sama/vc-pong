import pygame, sys, time
from pygame.locals import *

pygame.init()

Width = 800
Height = 600

window = pygame.display.set_mode((Width, Height), 0, 32)

pygame.display.set_caption('Pong')

Black = (0, 0, 0)
White = (255, 255, 255)

Y1 = 50
Y2 = 50

while True:

    Pong1 = pygame.draw.rect(window, White, (50, Y1, 25, 100))
    Pong2 = pygame.draw.rect(window, White, (750, Y2, 25, 100))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Y1 = Y1 - 50


            if event.key == pygame.K_s:
                Y1 = Y1 + 50


            if event.key == pygame.K_UP:
                Y2 = Y2 - 50

            if event.key == pygame.K_DOWN:
                Y2 = Y2 + 50

    pygame.display.update()
