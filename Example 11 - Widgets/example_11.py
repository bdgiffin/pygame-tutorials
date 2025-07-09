import pygame

import time

# Include the pygame_widgets module
import pygame_widgets
from pygame_widgets.button      import Button
from pygame_widgets.dropdown    import Dropdown
from pygame_widgets.progressbar import ProgressBar
from pygame_widgets.slider      import Slider
from pygame_widgets.textbox     import TextBox
from pygame_widgets.toggle      import Toggle
from pygame_widgets.button      import ButtonArray

startTime = time.time()

pygame.init()
window = pygame.display.set_mode((1000,600))

# Create a function to be called whenever the button is clicked
def print_dropdown():
    print(dropdown.getSelected())

# Create a function to be called when the text box entry is submitted
def output_text():
    print(textbox.getText())

# Create a simple button
left   = 10
top    = 10
width  = 100
height = 50
button = Button(window, left, top, width, height, onClick=print_dropdown,
                text='Print Value', textVAlign='center', margin=20, radius=5,
                font=pygame.font.SysFont('calibri', 10), fontSize=30,
                inactiveColour="Light Gray", pressedColour="Dark Gray")

# Creates an array of buttons
buttonArray = ButtonArray(
    # Mandatory Parameters
    window,  # Surface to place button array on
    790,  # X-coordinate
    10,  # Y-coordinate
    200,  # Width
    200,  # Height
    (2, 2),  # Shape: 2 buttons wide, 2 buttons tall
    border=20,  # Distance between buttons and edge of array
    texts=('1', '2', '3', '4'),  # Sets the texts of each button (counts left to right then top to bottom)
    # When clicked, print number
    onClicks=(lambda: print('1'), lambda: print('2'), lambda: print('3'), lambda: print('4'))
)

# Create a drop-down menu
dropdown = Dropdown(window, 120, 10, 100, 50, name='Select Color',
                    choices=['Red','Blue','Yellow'], values=[1, 2, 'true'],
                    direction='down', textHAlign='left',
                    colour=pygame.Color('green'), borderRadius=3)

# Create a progress bar
progressBar = ProgressBar(window, 100, 100, 500, 40,
                          lambda: 1 - (time.time() - startTime) / 10, curved=True)

# Create a slider
slider = Slider(window, 100, 240, 800, 40,
                min=0, max=100, step=10)

# Create a text box (acting as a label, with input disabled)
slider_textbox = TextBox(window, 475, 300, 50, 50,
                         fontSize=30)
slider_textbox.disable()

# Create a text box (accepting input)
textbox = TextBox(window, 100, 400, 800, 80,
                  fontSize=50, borderColour=(255, 0, 0), textColour=(0, 200, 0),
                  onSubmit=output_text, radius=10, borderThickness=5)

# Create a toggle button
toggle = Toggle(window, 100, 500, 100, 40)

game_running = True
while game_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            game_running = False
            quit()

    window.fill('White')

    # Set the displayed text in the text box based on the slider value
    slider_textbox.setText(slider.getValue())
    
    # Draw different widgets within the game window:
    pygame_widgets.update(events)
    
    pygame.display.update()
