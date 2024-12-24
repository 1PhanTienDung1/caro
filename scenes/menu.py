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
    text = font.render("Caro", False, color.ON_PRIMARY)
    text_width, text_height = text.get_size()
    text_rect = text.get_rect(center=(screen.get_width() // 2, 
                                      screen.get_height() // 2 - text_height // 2))
    
    screen.blit(text, text_rect)

def show_start_button(screen):
    font = pygame.font.Font("fonts/VT323-Regular.ttf", 25)
    text = font.render("Start", True, color.ON_SECOND)
    text_width, text_height = text.get_size()
    
    width_target = screen.get_width() // 5
    height_target = screen.get_height() // 5
    scale = min(height_target / text_height, width_target / text_width)
    
    font = pygame.font.Font("fonts/VT323-Regular.ttf", int(25 * scale))
    text = font.render("Start", True, color.ON_SECOND)
    text_width, text_height = text.get_size()
    text_rect = text.get_rect(center=(screen.get_width() // 2, 
                                      screen.get_height() // 2 + text_height // 2))
    
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
    return button_rect

def show_exit_button(screen, strart_button):
    font = pygame.font.Font("fonts/VT323-Regular.ttf", 25)
    text = font.render("Exit", True, color.ON_SECOND)
    text_width, text_height = text.get_size()
    
    width_target = strart_button.width * 6 // 10
    height_target = strart_button.height * 6 // 10
    scale = min(height_target / text_height, width_target / text_width)
    
    font = pygame.font.Font("fonts/VT323-Regular.ttf", int(25 * scale))
    text = font.render("Exit", True, color.ON_SECOND)
    text_width, text_height = text.get_size()
    text_rect = text.get_rect(center=(strart_button.centerx, 
                                      strart_button.centery + strart_button.height))
    
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
    return button_rect

def show(screen):
    screen.fill(color.PRIMARY)
    show_exit_button(screen, show_start_button(screen))
    show_game_name(screen)
    show_start_button(screen)

def click(screen, scene, event):
    global running
    if event.button != 1:
        return scene
    if show_start_button(screen).collidepoint(event.pos):
        return gameplay
    if show_exit_button(screen, show_start_button(screen)).collidepoint(event.pos):
        running = False
        pygame.quit()
        exit()
    return scene
        
    
pygame.quit()