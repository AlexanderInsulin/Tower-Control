import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1024, 768))

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()