import pygame
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

# Set the "game over" condition (initially True before the game starts)
game_over = True

# Keep track of the player's highest score
high_score = 0

clock = pygame.time.Clock()
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
            
    # Check if the "game over" flag has been set
    if game_over: 

        # Check if the player pressed the space bar to (re)start the game
        if keys[pygame.K_SPACE]:
            player_score  = 0
            player_health = 100
            game_over     = False
        
        window.fill("Black")
        
        if (player_health == 100): # Show the title screen
            window.blit(game_font.render('Knight Owl', False, "Purple"), (320,190))
            window.blit(game_font.render('(press space to start)', False, "Purple"), (210,220))
            
        else: # Show the game over screen
            window.blit(game_font.render('Game Over', False, "Red"), (330,190))
            window.blit(game_font.render('(press space to restart)', False, "Purple"), (190,220))
            window.blit(game_font.render(f'Score: {player_score}', False, "Green"), (340,325))
            window.blit(game_font.render(f'High Score: {high_score}', False, "Blue"), (250,350))
            
    else: # Play the game

        if keys[pygame.K_LEFT]:  player_rect.x -= 5
        if keys[pygame.K_RIGHT]: player_rect.x += 5
        if keys[pygame.K_DOWN]:  player_rect.y += 5
        if keys[pygame.K_UP]:    player_rect.y -= 5

        player_rect.x += max(0 - player_rect.midleft[0],0)
        player_rect.x -= max(player_rect.midright[0] - window_width,0)
        player_rect.y += max(0 - player_rect.midtop[1],0)
        player_rect.y -= max(player_rect.midbottom[1] - window_height,0)

        if (player_rect.center[0] > enemy_rect.center[0]): enemy_rect.x += 1
        if (player_rect.center[0] < enemy_rect.center[0]): enemy_rect.x -= 1
        if (player_rect.center[1] > enemy_rect.center[1]): enemy_rect.y += 1
        if (player_rect.center[1] < enemy_rect.center[1]): enemy_rect.y -= 1
    
        if player_rect.collidepoint(token_rect.center):
            player_score += 1
            token_rect.center = (random.randint(32,window_width-32),random.randint(32,window_height-32))
        
        if enemy_rect.collidepoint(player_rect.center):
            player_health -= 10
            enemy_rect.center = (window_width+32,random.randint(0,window_height))

        # End the game if the player's health drops to zero
        if (player_health == 0):
            # Save the player's highest score
            high_score = max(high_score,player_score)

            # Set the "game over" condition to True to end gameplay
            game_over = True
        
        window.fill("Black")

        window.blit(sky_image, (0,0))
        window.blit(player_image, player_rect)
        window.blit(enemy_image, enemy_rect)
        window.blit(token_image, token_rect)
    
        window.blit(game_font.render(f'Score: {player_score}', False, "Green"), (38,325))
        window.blit(game_font.render(f'Health: {player_health}', False, "Red"), (20,350))
    
    pygame.display.update()
    clock.tick(60)
