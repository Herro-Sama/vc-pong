import pygame, sys, time
from pygame.locals import *

pygame.init()

Width = 800
Height = 600

window = pygame.display.set_mode((Width, Height), 0, 32)

pygame.display.set_caption('Pong')

Black = (0, 0, 0)
White = (255, 255, 255)

Pong1 = pygame.draw.rect(window,White,(50, 50, 25, 100))
Pong1.centerx = window.get_rect().centerx
Pong1.centery = window.get_rect().centery

Pong2 = pygame.draw.rect(window,White,(50, 50, 25, 100))
Pong2.centerx = window.get_rect().centerx
Pong2.centery = window.get_rect().centery

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
