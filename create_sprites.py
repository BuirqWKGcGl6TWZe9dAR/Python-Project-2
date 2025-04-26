import pygame
import os
import sys

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

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# Player initial lives
player_lives = 3

# Player sprite creation
def create_player_sprite():
    surface = pygame.Surface((50, 40), pygame.SRCALPHA)
    pygame.draw.polygon(surface, BLUE, [(25, 0), (0, 40), (50, 40)])
    pygame.draw.rect(surface, YELLOW, (18, 25, 14, 10))
    pygame.draw.polygon(surface, RED, [(15, 40), (20, 50), (30, 50), (35, 40)])
    pygame.image.save(surface, "assets/images/player.png")
    return surface

# Create enemy sprites (simple versions for demo)
def create_enemy_sprites():
    enemies = []
    
    enemy1 = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.ellipse(enemy1, RED, (0, 5, 30, 20))
    pygame.draw.ellipse(enemy1, YELLOW, (5, 0, 20, 30))
    pygame.image.save(enemy1, "assets/images/enemy1.png")
    enemies.append(enemy1)
    
    return enemies

# Initialize all sprites
player_sprite = create_player_sprite()
enemy_sprites = create_enemy_sprites()

# Game setup
player_x, player_y = screen_width // 2, screen_height - 60
player_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement (left-right)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Prevent player from moving out of bounds
    player_x = max(0, min(screen_width - 50, player_x))

    # Handle collisions (example: enemy collision)
    # For simplicity, let's say the player loses a life if they collide with an enemy
    # (this is simplified, so you should use actual collision detection logic)
    for enemy in enemy_sprites:
        if player_x < 100 + 30 and player_y < 100 + 30:  # Check if player is near enemy (simplified)
            player_lives -= 1
            enemy_sprites.remove(enemy)  # Example of "destroying" the enemy after collision
            if player_lives <= 0:
                print("Game Over")
                running = False  # End the game

    # Clear the screen and draw everything
    screen.fill(BLACK)

    # Draw player sprite
    screen.blit(player_sprite, (player_x, player_y))

    # Draw enemies
    for enemy in enemy_sprites:
        screen.blit(enemy, (100, 100))  # Example position for the enemy

    # Display remaining lives (as mini player sprites)
    for i in range(player_lives):
        screen.blit(pygame.image.load("assets/images/player.png"), (10 + i * 50, 10))

    # Update the screen
    pygame.display.flip()

    # Control the frame rate (60 FPS)
    pygame.time.Clock().tick(60)

# Clean up and close the game properly
pygame.quit()
sys.exit()
