import pygame
from pygame.locals import *

key_to_direction = {
    K_UP: (0, -1),
    K_DOWN: (0, 1),
    K_RIGHT: (-1, 0),
    K_LEFT: (1, 0),
}

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        return
    def update(self, key):
        self.x = self.x + key_to_direction[key][0]*16
        self.y = self.y + key_to_direction[key][1]*16
        return
