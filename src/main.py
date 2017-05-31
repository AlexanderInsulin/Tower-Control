import pygame, sys, visualizer, game, camera, time
from pygame.locals import *

def main():
    pygame.init()

    WIDTH = 1024
    HEIGHT = 768

    my_font = pygame.font.SysFont("Courier", 16)
    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Control")
    my_game = game.Game()
    vis = visualizer.Visualizer()
    main_cam = camera.Camera(WIDTH, HEIGHT) 

    # move somewhere
    my_game.loadLevel()
    main_cam.reset(my_game.width, my_game.height, 
        my_game.tilewidth, my_game.tileheight)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break;
        elif event.type == KEYDOWN:  
            if event.key == K_q:
                pygame.event.post(pygame.event.Event(QUIT))

        frame_count += 1
        if frame_count % 10 == 0:
            t1 = time.clock()
            frame_rate = 10 / (t1-t0)
            t0 = t1

        my_game.update()
        main_cam.update()
        vis.draw(screen, my_game, main_cam)

        the_text = my_font.render("FPS = {0:.2f} fps"
                  .format(frame_rate), True, (100, 0, 0))
        screen.blit(the_text, (10, 10))

        pygame.display.flip()
        # pygame.time.wait(1)

    pygame.quit()

main()
