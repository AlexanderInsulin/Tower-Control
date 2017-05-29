import pygame, game

class Visualizer:
    def draw(self, surface, my_game, camera):
        surface.fill(pygame.Color(my_game.background_color))
        for layer in my_game.level.layers:
            for x, y, image in layer.tiles():
                surface.blit(image, (x * my_game.tilewidth - camera.x, 
                                     y * my_game.tileheight - camera.y))
        return
