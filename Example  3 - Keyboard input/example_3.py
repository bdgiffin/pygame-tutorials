import pygame

pygame.init()
window = pygame.display.set_mode((400,300))

# Specify the starting position of the player (circle)
player_x = 180
player_y = 180

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Get the "pressed" status of all keys on the keyboard:
    keys = pygame.key.get_pressed()
    
    # Check if the left arrow key is currently pressed:
    if keys[pygame.K_LEFT]:
        # Move the player to the left by 1 pixel:
        player_x -= 1
    
    # Check if the right arrow key is currently pressed:
    if keys[pygame.K_RIGHT]:
        # Move the player to the right by 1 pixel:
        player_x += 1
    
    # Check if the down arrow key is currently pressed:
    if keys[pygame.K_DOWN]:
        # Move the player down by 1 pixel:
        player_y += 1
    
    # Check if the up arrow key is currently pressed:
    if keys[pygame.K_UP]:
        # Move the player up by 1 pixel:
        player_y -= 1

    if (player_x < 0): player_x = 0
    if (player_x > 400): player_x = 400
    if (player_y < 0): player_y = 0
    if (player_y > 300): player_y = 300
        
    # "Erase" any shapes previously drawn in the window
    window.fill("Black") # reset window to display a full black screen
            
    # Draw the player's current position:
    pygame.draw.circle(window, "Red", (player_x,player_y), 60)
    
    pygame.display.update()
