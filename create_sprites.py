import pygame
import os

# Initialize pygame
pygame.init()

# Create the assets/images directory if it doesn't exist
if not os.path.exists("assets/images"):
    os.makedirs("assets/images")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Player Movement Example")

# Player sprite
def create_player_sprite():
    surface = pygame.Surface((50, 40), pygame.SRCALPHA)
    pygame.draw.polygon(surface, BLUE, [(25, 0), (0, 40), (50, 40)])
    pygame.draw.rect(surface, YELLOW, (18, 25, 14, 10))
    pygame.draw.polygon(surface, RED, [(15, 40), (20, 50), (30, 50), (35, 40)])
    pygame.image.save(surface, "assets/images/player.png")
    return surface

# Initialize player sprite
player_sprite = create_player_sprite()

# Define player position
player_width = 50  # Width of the player ship
player_height = 40  # Height of the player ship
player_x = screen_width // 2  # Start at the center of the screen
player_y = screen_height - player_height - 10  # Just above the bottom edge

# Player speed (you can adjust this value)
player_speed = 5

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement control
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        if player_x < 0:  # Prevent moving off the left edge
            player_x = 0
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
        if player_x > screen_width - player_width:  # Prevent moving off the right edge
            player_x = screen_width - player_width

    # Update player position
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Draw the player sprite
    screen.blit(player_sprite, player_rect.topleft)

    # Update the display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
