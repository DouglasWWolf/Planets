import pygame, math, os

#====================================================================================================
# Initializes pygame, creates the display window and starts the frame clock
#====================================================================================================
def init_game_window():

    global clock, screen, SCREEN_X, SCREEN_Y, CX, CY

    # Create a clock object so we can have a constant frame-rate
    clock = pygame.time.Clock()

    # Initialize the PyGame system
    pygame.init()

    # Set either the full-screen display mode or the window size
    if FULL_SCREEN:
        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((700, 700))

    # Tell the user how to stop the animation
    pygame.display.set_caption('Press ESC to Quit')

    # For the sake of neatness, turn off the mouse cursor
    pygame.mouse.set_visible(False)

    # Fetch the width and height of the screen
    SCREEN_X = screen.get_width()
    SCREEN_Y = screen.get_height()

    # Compute the coordinates at the center of the screen
    CX = SCREEN_X / 2
    CY = SCREEN_Y / 2
#====================================================================================================


#====================================================================================================
# check_for_quit() - Checks to see if the user has pressed ESC or Q, and if so, exits the program
#====================================================================================================
def check_for_quit():

    # Loop through each pygame event...
    for event in pygame.event.get():

        # Has the user closed the window?
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)

        # Has the user pressed the Q key?
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            os._exit(1)

        # Has the user pressed the ESC key?
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            os._exit(1)
#====================================================================================================



#====================================================================================================
# class Planet - Describes a planet in a circular orbit around a central point
#====================================================================================================
class Planet:

    # ----------------------------------------------------------------------------------------------
    # __init__() - Sets up parameters and creates the sprite for this planet
    # ----------------------------------------------------------------------------------------------
    def __init__(self, radius, distance, speed):

        # Store the planet's radius, distance, and speed for posterity
        self.radius = radius
        self.distance = distance
        self.speed = speed

        # Initialize the position of the center of the sprite projected onto the screen
        self.tick(True)

        # Create the sprite for this planet
        self.sprite = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
        self.sprite.fill(BLACK)
        self.sprite.set_colorkey(BLACK)
        pygame.draw.circle(self.sprite, GREY, (HALF_SPRITE, HALF_SPRITE), self.radius, 0)
    # ----------------------------------------------------------------------------------------------


    # ----------------------------------------------------------------------------------------------
    # tick() - Causes the angular position of the planet to increment by self.speed
    # ----------------------------------------------------------------------------------------------
    def tick(self, initialize = False):
        if initialize:
            self.theta = 0
        else:
            self.theta = self.theta + self.speed * SPEED_SCALE
            if self.theta > TWO_PI:
                self.theta = self.theta - TWO_PI

        self.cx = CX + self.distance * math.cos(self.theta)
        self.cy = CY + self.distance * math.sin(self.theta)
    # ----------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------
    # draw() - Draws the sprite for this planet at the appropriate place on screen
    # ----------------------------------------------------------------------------------------------
    def draw(self):
        screen.blit(self.sprite, (int(self.cx - HALF_SPRITE), int(self.cy - HALF_SPRITE)))
    # ----------------------------------------------------------------------------------------------

#====================================================================================================



#====================================================================================================
# Some global constants
#====================================================================================================

# We're not going to use full-screen mode
FULL_SCREEN = False

# Sprites are square.  This is the length of one side
SPRITE_SIZE = 50

# Radius of the sun
SUN_RADIUS = 40

# This is the coordinate (both X and Y) of the center of the sprite
HALF_SPRITE = SPRITE_SIZE / 2

# Color definitions
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY  = (100, 100, 100)

# This is the number of radians in a full circle
TWO_PI = math.pi * 2

# Speed scaling factor for the planets
SPEED_SCALE = 3
#====================================================================================================



#====================================================================================================
# main-line code for this program
#====================================================================================================
if __name__ == "__main__":

    # Initialize the graphics system
    init_game_window()

    # This will hold a list of all of our planets
    Planets = []

    # Define the radius, distance, and orbital speed of each planet
    Planets.append(Planet(3, 100, .0200))
    Planets.append(Planet(6, 150, .0150))
    Planets.append(Planet(3, 200, .0100))
    Planets.append(Planet(10,250, .0090))
    Planets.append(Planet(8, 300, .0050))

    # Sit in a loop, spinning planets around forever
    while True:

        # The screen starts black
        screen.fill(BLACK)

        # Draw the central star
        pygame.draw.circle(screen, WHITE, (CX, CY), SUN_RADIUS, 0)

        # Move and draw the planets
        for planet in Planets:
            planet.tick()
            planet.draw()

        # Display the screen surface in the physical window
        pygame.display.flip()

        # Check to see if the user wants to exit the program
        check_for_quit()

        # Aim for a frame-rate of 40 FPS
        clock.tick(40)
#====================================================================================================
