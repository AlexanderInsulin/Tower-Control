import pygame, sys, visualizer, game, camera
from pygame.locals import *

def main():
    pygame.init()

    WIDTH = 1024
    HEIGHT = 768

    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Control")
    my_game = game.Game()
    vis = visualizer.Visualizer()
    main_cam = camera.Camera(WIDTH, HEIGHT) 

    # move somewhere
    my_game.loadLevel()
    main_cam.reset(my_game.width, my_game.height, 
        500, 500)

    clock = pygame.time.Clock()
    while True:
        delta = clock.tick(60)
        delta /= 1000.0
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        elif event.type == KEYDOWN:  
            if event.key == K_q:
                pygame.event.post(pygame.event.Event(QUIT))

        my_game.update(delta)
        main_cam.update(delta)
        vis.draw(screen, my_game, main_cam)
        
        the_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, (100, 0, 0))
        screen.blit(the_text, (10, 10))

        pygame.display.flip()
        

    pygame.quit()

main()
