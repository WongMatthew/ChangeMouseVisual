# functions.py

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
RED = (255, 0, 0)
DARK_RED = (255, 100, 100)
GREEN = (0, 255, 0)
DARK_GREEN = (100, 255, 100)
WIDTH = 800
HEIGHT = 600
TITLE = "<Skeet>"
SPEED = 5

# ----- Drawing
def draw_person(screen, x, y):
    # HEAD
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
    # LEGS
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
    # BODY                                                              
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    # Arms
    pygame.draw.line(screen, DARK_RED, [5 + x, 9 + y], [1 + x, 17 + y], 2)
    pygame.draw.line(screen, DARK_RED, [5 +  x, 9 + y], [9 + x, 17 + y], 2)

def draw_person(screen, x, y):
    # HEAD
    pygame.draw.ellipse(screen, YELLOW, [1 + x, y, 10, 10], 4)
    # LEGS
    pygame.draw.line(screen, SKY_BLUE, [5 + x, 17 + y], [10 + x, 27 + y], 6)
    pygame.draw.line(screen, SKY_BLUE, [5 + x, 17 + y], [x, 27 + y], 6)
    # BODY                                                              
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [5 + x, 7 + y], 6)
    # Arms
    pygame.draw.line(screen, DARK_GREEN, [5 + x, 9 + y], [1 + x, 17 + y], 6)
    pygame.draw.line(screen, DARK_GREEN, [5 +  x, 9 + y], [9 + x, 17 + y], 6)

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
    person_x_cord = 10
    person_y_cord = 10
    person_x_vel = 0
    person_y_vel = 0

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # User Presses down a key
            elif event.type == pygame.KEYDOWN:
                # If its an arrow key
                if event.key == pygame.K_LEFT:
                    person_x_vel = -SPEED
                elif event.key == pygame.K_RIGHT:
                    person_x_vel = SPEED
                elif event.key == pygame.K_UP:
                    person_y_vel = -SPEED
                elif event.key == pygame.K_DOWN                                                                                                                                                                                                                                                                                                                                                                                                               :
                    person_y_vel = SPEED                                            

        # User lets go of key
            elif event.type == pygame.KEYUP:
                # If its an arrow key
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    person_x_vel = 0  
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    person_y_vel = 0                                         

        # ----- LOGIC
        mouse_x, mouse_y = pygame.mouse.get_pos()

        draw_person(screen, person_x_cord, person_y_cord)

        # ----- DRAW
        screen.fill(BLACK)

        draw_person(screen, mouse_x, mouse_y)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()