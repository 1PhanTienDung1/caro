import pygame
from constants import color
from scenes import gameplay

pygame.init()

size = 10
thisPlayer = 1
grid = []

for i in range(size):
    grid.append([])
    for j in range(size):
        grid[i].append(0)

def show_grid(screen):
    block_size = min(screen.get_width() * 6 // 10 // size,
                     screen.get_height() * 8 // 10 // size)
    
    rect = pygame.Rect(0, 0, block_size * size, block_size * size)
    rect.center = (screen.get_width() // 2,
                   screen.get_height() // 2)
    rect.x = screen.get_width() // 10
    
    line_width = min(screen.get_width() // 150,
                     screen.get_height() // 150)
    
    for i in range(size + 1):
        pygame.draw.line(screen, color.GRAY, 
                         (rect.x + i * block_size, rect.y),
                         (rect.x + i * block_size, rect.y + rect.h),
                         line_width)
    for i in range(size + 1):
        pygame.draw.line(screen, color.GRAY, 
                         (rect.x , rect.y + i * block_size),
                         (rect.x + rect.w, rect.y + i * block_size),
                         line_width)
    
    X_text = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 25).render("X", False, color.RED)
    O_text = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 25).render("O", False, color.BLUE)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                text_rect = X_text.get_rect(center=(rect.x + j * block_size + block_size // 2, rect.y + i * block_size + block_size // 2))
                screen.blit(X_text, text_rect.topleft)
            elif grid[i][j] == 2:
                text_rect = X_text.get_rect(center=(rect.x + j * block_size + block_size // 2, rect.y + i * block_size + block_size // 2))
                screen.blit(O_text, text_rect.topleft)

# def get_cell_positions(screen, size):
#     block_size = min(screen.get_width() * 6 // 10 // size,
#                      screen.get_height() * 8 // 10 // size)
    
#     rect = pygame.Rect(0, 0, block_size * size, block_size * size)

#     rect.center = (screen.get_width() // 2,
#                    screen.get_height() // 2)
#     rect.x = screen.get_width() // 10
    
#     positions = []
#     for row in range(size):
#         for col in range(size):
#             x = rect.x + col * block_size
#             y = rect.y + row * block_size
#             positions.append((x, y, block_size, block_size))
    
#     print(positions)
    
def show_player(screen):
    font = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 25);
    player1_text = font.render("Player 1: ", False, color.WHITE)    
    player2_text = font.render("Player 2: ", False, color.WHITE)    
    X_text = font.render("X", False, color.RED)    
    O_text = font.render("O", False, color.BLUE)
    
    block_w = player1_text.get_width() + X_text.get_width()
    block_h = player1_text.get_height() + player2_text.get_height()
    
    scale = min(screen.get_width() * 3 / 10 / block_w,
                screen.get_height() / block_h)
    
    font = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", int(25 * scale));
    player1_text = font.render("Player 1: ", False, color.WHITE)    
    player2_text = font.render("Player 2: ", False, color.WHITE)    
    X_text = font.render("X", False, color.RED)    
    O_text = font.render("O", False, color.BLUE)
    block_w = player1_text.get_width() + X_text.get_width()
    block_h = player1_text.get_height() + player2_text.get_height()
    
    posx, posy = (screen.get_width() - block_w,
                  screen.get_height() // 2 - block_h)
    
    screen.blit(player1_text, (posx, posy))
    screen.blit(player2_text, (posx, posy + player1_text.get_height()))
    screen.blit(X_text, (posx + player1_text.get_width(), posy))
    screen.blit(O_text, (posx + player1_text.get_width(), posy + player1_text.get_height()))    

def show(screen):
    screen.fill(color.BLACK)
    show_grid(screen)
    show_player(screen) 
    # get_cell_positions(screen)

def calculate_position(screen, pos):
    block_size = min(screen.get_width() * 6 // 10 // size,
                     screen.get_height() * 8 // 10 // size)
    
    rect = pygame.Rect(0, 0, block_size * size, block_size * size)
    rect.center = (screen.get_width() // 2,
                   screen.get_height() // 2)
    rect.x = screen.get_width() // 10
    
    col = (pos[0] - rect.x) // block_size
    row = (pos[1] - rect.y) // block_size
    
    return row, col
    

def click(screen, scene, event):
    global thisPlayer
    global grid
    pos = pygame.mouse.get_pos()
    row,col = calculate_position(screen, pos)
    if (row < 0 or row >= size or col < 0 or col >= size):
        return scene
    if grid[row][col] == 0:
        grid[row][col] = thisPlayer
        if thisPlayer == 1:
            thisPlayer = 2
        else:
            thisPlayer = 1
    show_grid(screen)
    return scene
pygame.quit()