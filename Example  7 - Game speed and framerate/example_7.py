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

# Create a clock to keep track of time and to control the speed of the game
clock = pygame.time.Clock()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_rect.x -= 5
    if keys[pygame.K_RIGHT]: player_rect.x += 5
    if keys[pygame.K_DOWN]:  player_rect.y += 5
    if keys[pygame.K_UP]:    player_rect.y -= 5

    player_rect.x += max(0 - player_rect.midleft[0],0)
    player_rect.x -= max(player_rect.midright[0] - window_width,0)
    player_rect.y += max(0 - player_rect.midtop[1],0)
    player_rect.y -= max(player_rect.midbottom[1] - window_height,0)

    if (player_rect.center[0] > enemy_rect.center[0]): enemy_rect.x += 2
    if (player_rect.center[0] < enemy_rect.center[0]): enemy_rect.x -= 2
    if (player_rect.center[1] > enemy_rect.center[1]): enemy_rect.y += 2
    if (player_rect.center[1] < enemy_rect.center[1]): enemy_rect.y -= 2
    
    if player_rect.collidepoint(token_rect.center):
        player_score += 1
        token_rect.center = (random.randint(32,window_width-32),random.randint(32,window_height-32))
    
    if enemy_rect.collidepoint(player_rect.center):
        player_health -= 10
        enemy_rect.center = (window_width+32,random.randint(0,window_height))
        
    window.fill("Black")

    window.blit(sky_image, (0,0))
    window.blit(player_image, player_rect)
    window.blit(enemy_image, enemy_rect)
    window.blit(token_image, token_rect)
    
    window.blit(game_font.render('Knight Owl', False, "Purple"),           (320,350))
    window.blit(game_font.render(f'Score: {player_score}', False, "Green"), (38,325))
    window.blit(game_font.render(f'Health: {player_health}', False, "Red"), (20,350))
    
    pygame.display.update()

    # Wait enough time for the game to update only 60 times per second
    framerate = 60 # (frames-per-second)
    clock.tick(framerate)
    
