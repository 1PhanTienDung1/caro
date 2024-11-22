import pygame
from scenes import *
from constants import *

pygame.init()
pygame.display.set_caption(game.NAME);

screen = pygame.display.set_mode((int(pygame.display.Info().current_w / 1.5),
                                  int(pygame.display.Info().current_h / 1.5)));
scene = menu

running = True
while running:
    scene.show(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            scene = scene.click(screen, scene, event)
        
    pygame.display.flip()
    
pygame.quit()