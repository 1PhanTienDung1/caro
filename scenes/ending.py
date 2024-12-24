import pygame
from constants import color
from scenes import gameplay
from scenes import ending

def show(screen):
    screen.fill(color.PRIMARY)
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
    
    text = pygame.font.Font("fonts/VT323-Regular.ttf", 25).render("PLAY AGAIN", False, color.ON_SECOND)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    text_rect.top = screen.get_height() // 2 + 50;
    
    padding = 10  # Padding around the text
    button_rect = pygame.Rect(
        text_rect.left - padding,
        text_rect.top - padding,
        text_rect.width + 2 * padding,
        text_rect.height + 2 * padding
    )

    # button background
    pygame.draw.rect(screen, color.SECOND, button_rect, border_radius=5)  
    pygame.draw.rect(screen, color.SECOND_VAR, button_rect, width=2, border_radius=5) #border

    screen.blit(text, text_rect)
    
    pygame.display.update()
    return button_rect

def click(screen, scene, event):
    rect = show(screen)
    if rect.collidepoint(event.pos):
        gameplay.thisPlayer = 1
        gameplay.done = False
        gameplay.status = 0
        for i in range(5):
            for j in range(5):
                gameplay.grid[i][j] = 0
        return gameplay
    return scene

pygame.quit()