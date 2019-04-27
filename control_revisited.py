# control_revisited.py
# Author: Matt Wong
# 4 April 2019
# Pygame interactions w/ keyboard

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
DARK_RED = (200, 50, 50)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Mind Control"

SPEED = 10

def draw_person(screen, x, y):
    """Draws person on screen.

    Arguments:
    screen - screen on which to draw
    x - xcoord of middle of person
    y - ycoord of middle of person

    Returns:
    None
    """
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, DARK_RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, DARK_RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, DARK_RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- WORLD PROPERTIES
    pygame.mouse.set_visible(False)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # -- Person Initial Values
    person_x_coord = 10
    person_y_coord = 10
    person_x_vel = 0
    person_y_vel = 0

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            # User presses down a key
            elif event.type == pygame.KEYDOWN:
                # If it's an arrow key
                if event.key == pygame.K_LEFT:
                    person_x_vel = -SPEED
                elif event.key == pygame.K_RIGHT:
                    person_x_vel = SPEED
                elif event.key == pygame.K_UP:
                    person_y_vel = -SPEED
                elif event.key == pygame.K_DOWN:
                    person_y_vel = SPEED
            
            # User lets go of key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_x_vel = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    person_y_vel = 0

        # ----- LOGIC
        mouse_x, mouse_y = pygame.mouse.get_pos()

        person_x_coord += person_x_vel
        person_y_coord += person_y_vel

        # ----- DRAW
        screen.fill(WHITE)

        draw_person(screen, person_x_coord, person_y_coord)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
