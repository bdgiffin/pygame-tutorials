# Import the pygame library into Python
import pygame

# Initialize the pygame object
pygame.init()

# Create a new display window with fixed width and height dimensions
width  = 400 # (pixels)
height = 300 # (pixels)
window = pygame.display.set_mode((width,height))

# Execute the game "event loop" for as long as the game is running
game_running = True
while game_running:
    # Loop through any/all game "events":
    for event in pygame.event.get():
        # Check if the player has closed the window to "QUIT" the game:
        if event.type == pygame.QUIT:
            # If the player quit, stop the game from running:
            # (this will terminate the event loop and end the program)
            game_running = False
