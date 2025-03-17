import pygame

pygame.init()
window_width  = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))

pygame.font.init()
game_font = pygame.font.SysFont('PT Mono', 30)
title_text = game_font.render('Knight Owl', False, "Purple")

sky_image    = pygame.image.load('sky.jpeg')
player_image = pygame.image.load('owl.png').convert_alpha()
enemy_image  = pygame.image.load('bat.png').convert_alpha()
token_image  = pygame.image.load('firefly.png').convert_alpha()

player_rect = player_image.get_rect()
enemy_rect  = enemy_image.get_rect()
token_rect  = token_image.get_rect()

player_rect.center = (180,180)
enemy_rect.center  = (280, 80)
token_rect.center  = (480,280)

# ---------------------------------------------------------------------------- #

# Keep track of the player's total score
player_score = 0
score_text = game_font.render(f'Score: {player_score}', False, "Green")

# Keep track of the player's total health
player_health = 100
health_text = game_font.render(f'Health: {player_health}', False, "Red")

# ---------------------------------------------------------------------------- #

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

    # ------------------------------------------------------------------------ #

    # Make sure the player does not leave the window:
    
    # Check if the player tried to leave the LEFT edge of the window
    if (player_rect.midleft[0] < 0):
        # Push the player to the RIGHT so they are fully visible in the window
        player_rect.x += (0 - player_rect.midleft[0])
    
    # Check if the player tried to leave the RIGHT edge of the window
    if (player_rect.midright[0] > window_width):
        # Push the player to the LEFT so they are fully visible in the window
        player_rect.x -= (player_rect.midright[0] - window_width)
    
    # Check if the player tried to leave the TOP edge of the window
    if (player_rect.midtop[1] < 0):
        # Push the player DOWN so they are fully visible in the window
        player_rect.y += (0 - player_rect.midtop[1])
    
    # Check if the player tried to leave the BOTTOM edge of the window
    if (player_rect.midbottom[1] > window_height):
        # Push the player UP so they are fully visible in the window
        player_rect.y -= (player_rect.midbottom[1] - window_height)

    # ------------------------------------------------------------------------ #
        
    # Check for a collision between the player and the token
    player_touched_token = player_rect.collidepoint(token_rect.center)
    if player_touched_token:
        # If the player touched the token, increase the player's score
        player_score += 1
        score_text = game_font.render(f'Score: {player_score}', False, "Green")

    # Check for a collision between the enemy and the player
    enemy_touched_player = enemy_rect.colliderect(player_rect)
    if enemy_touched_player:
        # If the enemy touched the player, decrease the player's health
        player_health -= 1
        health_text = game_font.render(f'Health: {player_health}', False, "Red")

    # ------------------------------------------------------------------------ #
        
    window.fill("Black")

    window.blit(sky_image, (0,0))
    window.blit(player_image, player_rect)
    window.blit(enemy_image, enemy_rect)
    window.blit(token_image, token_rect)
    window.blit(title_text, (320,350))

    # Display the player's current total score
    window.blit(score_text,  (38,325))
    
    # Display the player's current total health
    window.blit(health_text, (20,350))
    
    pygame.display.update()
