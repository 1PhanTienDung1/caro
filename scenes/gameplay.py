import pygame
from constants import color
from scenes import gameplay
from scenes import ending

pygame.init()

size = 5
thisPlayer = 1
done = False
grid = []
status = 0

for i in range(size):
    grid.append([])
    for j in range(size):
        grid[i].append(0)

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

def show_grid(screen):
    block_size = min(screen.get_width() * 6 // 10 // size,
                    screen.get_height() * 8 // 10 // size)
    
    rect = pygame.Rect(0, 0, block_size * size, block_size * size)
    rect.center = (screen.get_width() // 2,
                screen.get_height() // 2)
    rect.x = screen.get_width() // 10
    
    line_width = min(screen.get_width() // 150,
                    screen.get_height() // 150)
    
    grid_background_color = color.PRIMARY_VAR
    pygame.draw.rect(screen, grid_background_color, rect)
    
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
        
    mouse_pos = pygame.mouse.get_pos()
    mouse_row, mouse_col = calculate_position(screen, mouse_pos)
    
    X_text = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 25).render("X", False, color.RED)
    O_text = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 25).render("O", False, color.BLUE)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                text_rect = X_text.get_rect(center=(rect.x + j * block_size + block_size // 2, rect.y + i * block_size + block_size // 2))
                screen.blit(X_text, text_rect.topleft)
            elif grid[i][j] == 2:
                text_rect = O_text.get_rect(center=(rect.x + j * block_size + block_size // 2, rect.y + i * block_size + block_size // 2))
                screen.blit(O_text, text_rect.topleft)
            elif i == mouse_row and j == mouse_col:
                if thisPlayer == 1:
                    text_rect = X_text.get_rect(center=(rect.x + j * block_size + block_size // 2, rect.y + i * block_size + block_size // 2))
                    screen.blit(X_text, text_rect.topleft)
                else:
                    text_rect = O_text.get_rect(center=(rect.x + j * block_size + block_size // 2, rect.y + i * block_size + block_size // 2))
                    screen.blit(O_text, text_rect.topleft)
    
def show_player(screen):
    font = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", 25);
    player1_text = font.render("Player 1: ", False, color.ON_PRIMARY)    
    player2_text = font.render("Player 2: ", False, color.ON_PRIMARY)    
    X_text = font.render("X", False, color.RED)    
    O_text = font.render("O", False, color.BLUE)
    
    block_w = player1_text.get_width() + X_text.get_width()
    block_h = player1_text.get_height() + player2_text.get_height()
    
    scale = min(screen.get_width() * 3 / 10 / block_w,
                screen.get_height() / block_h)
    
    font = pygame.font.Font("fonts/Parkinsans-ExtraBold.ttf", int(25 * scale));
    player1_text = font.render("Player 1: ", False, color.ON_PRIMARY)    
    player2_text = font.render("Player 2: ", False, color.ON_PRIMARY)    
    X_text = font.render("X", False, color.RED)    
    O_text = font.render("O", False, color.BLUE)
    block_w = player1_text.get_width() + X_text.get_width()
    block_h = player1_text.get_height() + player2_text.get_height()
    
    margin_x = int(screen.get_width() * 0.05)
    posx, posy = (screen.get_width() - block_w - margin_x,
                  screen.get_height() // 2 - block_h)
    
    screen.blit(player1_text, (posx, posy))
    screen.blit(player2_text, (posx, posy + player1_text.get_height()))
    screen.blit(X_text, (posx + player1_text.get_width(), posy))
    screen.blit(O_text, (posx + player1_text.get_width(), posy + player1_text.get_height()))    

def show(screen):
    screen.fill(color.BLACK)
    show_grid(screen)
    show_player(screen) 

def check_win():
    is_full = True
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                is_full = False
                continue
            if j + 4 < size:
                if grid[i][j] == grid[i][j + 1] == grid[i][j + 2] == grid[i][j + 3] == grid[i][j + 4]:
                    return grid[i][j]
            if i + 4 < size:
                if grid[i][j] == grid[i + 1][j] == grid[i + 2][j] == grid[i + 3][j] == grid[i + 4][j]:
                    return grid[i][j]
            if i + 4 < size and j + 4 < size:
                if grid[i][j] == grid[i + 1][j + 1] == grid[i + 2][j + 2] == grid[i + 3][j + 3] == grid[i + 4][j + 4]:
                    return grid[i][j]
            if i + 4 < size and j - 4 >= 0:
                if grid[i][j] == grid[i + 1][j - 1] == grid[i + 2][j - 2] == grid[i + 3][j - 3] == grid[i + 4][j - 4]:
                    return grid[i][j]
    return (3 if is_full else 0)
    
def click(screen, scene, event):
    global thisPlayer
    global grid
    global status
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
    status = check_win()
    # print(status)
    if status != 0:
        return ending
    return scene

pygame.quit()