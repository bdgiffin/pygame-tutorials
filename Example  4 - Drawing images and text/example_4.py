import pygame

pygame.init()
window = pygame.display.set_mode((800,400))


# Initialize a new font for drawing text
pygame.font.init()
font_type  = 'PT Mono'
font_size  = 30 # (pixels)
title_font = pygame.font.SysFont(font_type, font_size)

# Create rendered text with the title of the game
game_title    = 'Knight Owl'
anti_aliasing = False # (adjusts pixelized appearance of rendered text)
text_color    = "Purple"
title_text = title_font.render(game_title, anti_aliasing, text_color)


# Load the background image
sky_image = pygame.image.load('sky.jpeg')

# Load the image representing the player
player_image = pygame.image.load('owl.png').convert_alpha()
# Create a rectangle containing the image of the player
player_rect   = player_image.get_rect()
player_rect.x = 180
player_rect.y = 180

# Load the image representing an enemy
enemy_image = pygame.image.load('bat.png').convert_alpha()
# Create a rectangle containing the image of an enemy
enemy_rect  = enemy_image.get_rect()
enemy_rect.x = 280
enemy_rect.y =  80

# Load the image representing a token
token_image = pygame.image.load('firefly.png').convert_alpha()
# Create a rectangle containing the image of a token
token_rect  = token_image.get_rect()
token_rect.x = 480
token_rect.y = 280


game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_rect.x -= 1
    if keys[pygame.K_RIGHT]: player_rect.x += 1
    if keys[pygame.K_DOWN]:  player_rect.y += 1
    if keys[pygame.K_UP]:    player_rect.y -= 1

    window.fill("Black")

    # Draw the background image in the game window
    background_image_top_left_corner = (0,0) # (x,y)
    window.blit(sky_image, background_image_top_left_corner)
            
    # Draw the rectangle containing the image of the player
    window.blit(player_image, player_rect)
            
    # Draw the rectangle containing the image of an enemy
    window.blit(enemy_image, enemy_rect)
            
    # Draw the rectangle containing the image of a token
    window.blit(token_image, token_rect)

    # Draw the title text
    title_position = (320,350) # (x,y)
    window.blit(title_text, title_position)
    
    pygame.display.update()
