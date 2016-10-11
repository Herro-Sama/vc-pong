import pygame, sys, time
from pygame.locals import *

pygame.init()

Width = 800
Height = 600

window = pygame.display.set_mode((Width,Height), 0, 32)

pygame.display.set_caption('Backdoor')

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)



font = pygame.font.SysFont(None, 48)
Backdoor = 1

text = font.render('It works!', True, Green, Blue)

Backdoor_container = text.get_rect()
Backdoor_container.centerx = window.get_rect().centerx
Backdoor_container.centery = window.get_rect().centery


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    window.fill(Black)
    pygame.draw.rect(window, White, Backdoor_container)
    window.blit(text, Backdoor_container)
    pygame.display.update()