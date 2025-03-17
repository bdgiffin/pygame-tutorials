import pygame

# Import the Python "random" package to generate randomized numbers
import random

pygame.init()
window_width  = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))

pygame.font.init()
game_font = pygame.font.SysFont('PT Mono', 30)

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

player_score  = 0
player_health = 100

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_rect.x -= 3
    if keys[pygame.K_RIGHT]: player_rect.x += 3
    if keys[pygame.K_DOWN]:  player_rect.y += 3
    if keys[pygame.K_UP]:    player_rect.y -= 3

    player_rect.x += max(0 - player_rect.midleft[0],0)
    player_rect.x -= max(player_rect.midright[0] - window_width,0)
    player_rect.y += max(0 - player_rect.midtop[1],0)
    player_rect.y -= max(player_rect.midbottom[1] - window_height,0)

    # Move the enemy in the direction of the player
    if (player_rect.center[0] > enemy_rect.center[0]): enemy_rect.x += 1
    if (player_rect.center[0] < enemy_rect.center[0]): enemy_rect.x -= 1
    if (player_rect.center[1] > enemy_rect.center[1]): enemy_rect.y += 1
    if (player_rect.center[1] < enemy_rect.center[1]): enemy_rect.y -= 1
    
    if player_rect.collidepoint(token_rect.center):
        player_score += 1
        
        # Move the token to a new randomized position inside the window
        distance_from_edge = 32
        min_x = 0             + distance_from_edge
        max_x = window_width  - distance_from_edge
        min_y = 0             + distance_from_edge
        max_y = window_height - distance_from_edge
        token_new_x = random.randint(min_x, max_x)
        token_new_y = random.randint(min_y, max_y)
        token_rect.center = (token_new_x, token_new_y)
    
    if enemy_rect.colliderect(player_rect):
        player_health -= 5
        
        # Move the enemy to a new randomized position outside the window
        distance_from_edge = 32
        enemy_new_x = window_width + distance_from_edge
        enemy_new_y = random.randint(0, window_height)
        enemy_rect.center = (enemy_new_x, enemy_new_y)
        
    window.fill("Black")

    window.blit(sky_image, (0,0))
    window.blit(player_image, player_rect)
    window.blit(enemy_image, enemy_rect)
    window.blit(token_image, token_rect)
    
    window.blit(game_font.render('Knight Owl', False, "Purple"),           (320,350))
    window.blit(game_font.render(f'Score: {player_score}', False, "Green"), (38,325))
    window.blit(game_font.render(f'Health: {player_health}', False, "Red"), (20,350))
    
    pygame.display.update()
