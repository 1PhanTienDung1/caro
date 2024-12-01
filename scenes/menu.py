import pygame
from constants import color
from scenes import gameplay
from scenes import menu

pygame.init()

def show_game_name(screen):
    font = pygame.font.Font("fonts/Doto_Rounded-ExtraBold.ttf", 25)
    text = font.render("Caro", False, color.WHITE)
    text_width, text_height = text.get_size()
    
    width_target = screen.get_width() // 3
    height_target = screen.get_height() // 3
    scale = min(height_target / text_height, width_target / text_width)
    
    font = pygame.font.Font("fonts/Doto_Rounded-ExtraBold.ttf", int(25 * scale))
    text = font.render("Caro", False, color.WHITE)
    text_width, text_height = text.get_size()
    text_rect = text.get_rect(center=(screen.get_width() // 2, 
                                      screen.get_height() // 2 - text_height // 2))
    
    screen.blit(text, text_rect)

def show_start_button(screen):
    font = pygame.font.Font("fonts/VT323-Regular.ttf", 25)
    text = font.render("Caro", True, color.CYAN)
    text_width, text_height = text.get_size()
    
    width_target = screen.get_width() // 5
    height_target = screen.get_height() // 5
    scale = min(height_target / text_height, width_target / text_width)
    
    font = pygame.font.Font("fonts/VT323-Regular.ttf", int(25 * scale))
    text = font.render("Start", True, color.CYAN)
    text_width, text_height = text.get_size()
    text_rect = text.get_rect(center=(screen.get_width() // 2, 
                                      screen.get_height() // 2 + text_height // 2))
    
    screen.blit(text, text_rect)
    return text_rect

def show(screen):
    screen.fill(color.BLACK)
    show_game_name(screen)
    show_start_button(screen)

def click(screen, scene, event):
    rect = show_start_button(screen)
    if event.button == 1 and rect.collidepoint(event.pos):
        return gameplay
    return scene
        
    
pygame.quit()