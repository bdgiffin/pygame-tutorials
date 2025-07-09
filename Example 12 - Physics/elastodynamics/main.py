import asyncio

import pygame
import math

# Include the pygame_widgets module
import pygame_widgets
from pygame_widgets.slider import Slider

pygame.init()
window = pygame.display.set_mode((1000,600))

async def main():
    # Set the window title and icon
    pygame.display.set_caption('1D Elasto-dynamics')
    
    font = pygame.font.Font('Silkscreen-Regular.ttf', 24)

    density_slider = Slider(window, 230, 375, 720, 40, min=1, max=10, step=0.1)
    area_slider    = Slider(window, 230, 450, 720, 40, min=1, max=10, step=0.1)
    element_slider = Slider(window, 230, 525, 720, 40, min=1, max=10, step=1)

    initial_velocity = 0.2
    external_force = 0.0
    damping = 1.0
    time_step = 1.0e-1

    # Define material properties
    youngs_modulus = 1.0
    mass_density = 1.0
    cross_sectional_area = 1.0

    # Initialize nodes
    elevation = 200
    scaling = 600
    length = 1.0
    Nelems = element_slider.getValue()
    nodes        = [0] * (Nelems+1)
    displacement = [0] * (Nelems+1)
    velocity     = [initial_velocity] * (Nelems+1)
    for i in range(0,Nelems+1):
        nodes[i] = i*(length/Nelems)

    clock = pygame.time.Clock()
    framerate = 30

    game_running = True
    while game_running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                game_running = False
                quit()

        window.fill('White')

        # re-map problem parameters by interpolation
        if (Nelems != element_slider.getValue()):
            new_Nelems       = element_slider.getValue()
            nodes            = [0] * (new_Nelems+1)
            new_displacement = [0] * (new_Nelems+1)
            new_velocity     = [0] * (new_Nelems+1)
            for i in range(1,new_Nelems+1):
                nodes[i] = i*(length/new_Nelems)
                xi = nodes[i]/(length/Nelems)
                j = min(math.floor(xi),Nelems-1)
                xi -= j
                new_displacement[i] = (1-xi)*displacement[j] + xi*displacement[j+1]
                new_velocity[i]     = (1-xi)*velocity[j]     + xi*velocity[j+1]
            displacement = new_displacement
            velocity = new_velocity

        # dynamically adjust the problem parameters
        mass_density         = density_slider.getValue()
        cross_sectional_area = area_slider.getValue()
        Nelems               = element_slider.getValue()
        element_length       = length/Nelems

        # initialize the mass and force at all nodes
        mass      = [0] * (Nelems+1)
        force     = [0] * (Nelems+1)
        force[-1] = external_force

        # loop over all elements and sum contributions to lumped nodal masses and forces
        for i in range(0,Nelems):
            # lump the element's nodal masses
            element_mass = mass_density*cross_sectional_area*element_length
            mass[i]   += 0.5*element_mass
            mass[i+1] += 0.5*element_mass

            # compute internal forces
            strain = (displacement[i+1] - displacement[i])/element_length
            stress = youngs_modulus*strain
            internal_force = stress*cross_sectional_area
            force[i]   += internal_force
            force[i+1] -= internal_force

            # draw the element in its current deformed state
            x1 = scaling*(nodes[i]  +displacement[i])
            x2 = scaling*(nodes[i+1]+displacement[i+1])
            stretch = (x2-x1)/(scaling*element_length)
            height = 5*cross_sectional_area/max(0.1,stretch)
            color = (max(0,min(255,-600*strain)),max(0,255-600*abs(strain)),max(0,min(255,+600*strain)))
            pygame.draw.rect(window, color, pygame.Rect(x1, elevation-height/2, x2-x1, height))

        # loop over all nodes and update velocities and positions
        for i in range(1,Nelems+1):
            # draw the node in its current position
            xi = scaling*(nodes[i]+displacement[i])
            pygame.draw.circle(window, "Black", (xi,elevation), 3*mass[i])

            # update position and velocity
            acceleration = force[i]/mass[i]
            velocity[i]     += acceleration*time_step
            displacement[i] +=  velocity[i]*time_step

        pygame_widgets.update(events)
        window.blit(font.render(f'Density: {round(mass_density,1)}', False, "Black"), (10,375))
        window.blit(font.render(f'X-Area:  {round(cross_sectional_area,1)}', False, "Black"), (10,450))
        window.blit(font.render(f'Elements: {Nelems}', False, "Black"), (10,525))
        pygame.display.update()

        clock.tick(framerate)
        await asyncio.sleep(0)

asyncio.run(main())
