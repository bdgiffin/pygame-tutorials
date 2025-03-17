import pygame

pygame.init()
window = pygame.display.set_mode((400,300))

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Draw different basic shapes within the game window:

    # Draw a rectangle
    color  = "Red"
    left   = 100 # (pixels)
    top    =  30 # (pixels)
    width  =  60 # (pixels)
    height =  60 # (pixels)
    pygame.draw.rect(window, color, pygame.Rect(left, top, width, height))

    # Draw a polygon (triangle)
    color  = "Blue"
    points = ((325,75),(376,125),(275,200)) # ((x1,y1), (x2,y2), (x3,y3), ...)
    pygame.draw.polygon(window, color, points)

    # Draw a circle:
    color  = "White"
    center = (180,180) # (x,y)
    radius = 60
    pygame.draw.circle(window, color, center, radius)

    # Draw a line
    color      = "Yellow"
    start_pos  = (10,200) # (x,y)
    end_pos    = (300,10) # (x,y)
    line_width = 4 # (pixels)
    pygame.draw.line(window, color, start_pos, end_pos, line_width)

    # Draw an ellipse
    color  = "Green"
    left   = 250 # (pixels)
    top    = 200 # (pixels)
    width  = 130 # (pixels)
    height =  80 # (pixels)
    pygame.draw.ellipse(window, color, (left, top, width, height))

    # Update the window to display the shapes drawn in the current event loop
    pygame.display.update()
