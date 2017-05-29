import pygame, sys, visualizer, game, camera
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Tower Control")
my_game = game.Game()
my_game.loadLevel()
vis = visualizer.Visualizer()
main_cam = camera.Camera()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT):
            main_cam.update(event.key)
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    vis.draw(screen, my_game, main_cam)
    my_game.update()

    pygame.display.flip()
