import pygame
from pygame.locals import *

class Camera:
    def __init__(self, screen_width, screen_height):
        self.x = 0
        self.y = 0
        self.max_x = 0
        self.max_y = 0
        self.width = screen_width
        self.height = screen_height
        self.step_x = 0
        self.step_y = 0
        return
    
    def update(self, delta):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: 
            self.y -= self.step_y*delta;
        if keys[pygame.K_DOWN]: 
            self.y += self.step_y*delta;           
        if keys[pygame.K_LEFT]: 
            self.x -= self.step_x*delta;
        if keys[pygame.K_RIGHT]: 
            self.x += self.step_x*delta;
        if self.x < 0:
            self.x = 0
        if self.x > (self.max_x - self.width):
            self.x = self.max_x - self.width
        if self.y < 0:
            self.y = 0
        if self.y > (self.max_y - self.height):
            self.y = self.max_y - self.height
        return

    def reset(self, max_width, max_height, step_x, step_y):
        self.max_x = max_width
        self.max_y = max_height
        self.step_x = step_x
        self.step_y = step_y
        return
