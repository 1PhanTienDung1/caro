import pygame
from constants import color
from scenes import gameplay
from scenes import ending

def show(screen):
    screen.fill(color.BLACK)
    # print(gameplay.status)
    if gameplay.status == 3:
        # game draw
        text = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 50).render("Draw", False, color.WHITE)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        text_rect.bottom = screen.get_height() // 2;
        screen.blit(text, text_rect)
    if gameplay.status == 1:
        # player 1 win
        text = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 50).render("Player 1 win", False, color.WHITE)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        text_rect.bottom = screen.get_height() // 2;
        screen.blit(text, text_rect)
    if gameplay.status == 2:
        # player 2 win
        text = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 50).render("Player 2 win", False, color.WHITE)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        text_rect.bottom = screen.get_height() // 2;
        screen.blit(text, text_rect)
    
    text = pygame.font.Font("fonts/FiraCode-Bold.ttf", 25).render("CLICK HERE TO PLAY AGAIN", False, color.SECOND)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    text_rect.top = screen.get_height() // 2;
    screen.blit(text, text_rect)
    
    pygame.display.update()
    return text_rect

def click(screen, scene, event):
    rect = show(screen)
    if rect.collidepoint(pygame.mouse.get_pos()):
        gameplay.thisPlayer = 1
        gameplay.done = False
        gameplay.status = 0
        for i in range(5):
            for j in range(5):
                gameplay.grid[i][j] = 0
        return gameplay
    return scene

pygame.quit()