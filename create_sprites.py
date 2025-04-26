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

# Create player sprite
def create_player_sprite():
    surface = pygame.Surface((50, 40), pygame.SRCALPHA)
    pygame.draw.polygon(surface, BLUE, [(25, 0), (0, 40), (50, 40)])
    pygame.draw.rect(surface, YELLOW, (18, 25, 14, 10))
    pygame.draw.polygon(surface, RED, [(15, 40), (20, 50), (30, 50), (35, 40)])
    pygame.image.save(surface, "assets/images/player.png")

    mini = pygame.Surface((25, 20), pygame.SRCALPHA)
    pygame.draw.polygon(mini, BLUE, [(12, 0), (0, 20), (25, 20)])
    pygame.draw.rect(mini, YELLOW, (9, 12, 7, 5))
    pygame.image.save(mini, "assets/images/player_mini.png")

    return surface

# Create enemy sprites (3 different types)
def create_enemy_sprites():
    enemies = []
    
    enemy1 = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.ellipse(enemy1, RED, (0, 5, 30, 20))
    pygame.draw.ellipse(enemy1, YELLOW, (5, 0, 20, 30))
    pygame.image.save(enemy1, "assets/images/enemy1.png")
    enemies.append(enemy1)

    enemy2 = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(enemy2, PURPLE, [
        (15, 0), (25, 5), (30, 15),
        (25, 25), (15, 30), (5, 25),
        (0, 15), (5, 5)
    ])
    pygame.draw.circle(enemy2, RED, (15, 15), 5)
    pygame.image.save(enemy2, "assets/images/enemy2.png")
    enemies.append(enemy2)

    enemy3 = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.rect(enemy3, GREEN, (0, 0, 30, 30))
    pygame.draw.rect(enemy3, BLACK, (5, 5, 20, 20))
    pygame.draw.rect(enemy3, WHITE, (10, 10, 10, 10))
    pygame.image.save(enemy3, "assets/images/enemy3.png")
    enemies.append(enemy3)

    return enemies

# Create bullet sprite
def create_bullet_sprite():
    bullet = pygame.Surface((5, 10), pygame.SRCALPHA)
    pygame.draw.rect(bullet, YELLOW, (0, 0, 5, 10))
    pygame.draw.rect(bullet, WHITE, (1, 1, 3, 3))
    pygame.image.save(bullet, "assets/images/bullet.png")
    return bullet

# Create power-up sprites
def create_powerup_sprites():
    powerups = {}
    
    shield = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.circle(shield, BLUE, (10, 10), 10)
    pygame.draw.circle(shield, WHITE, (10, 10), 6, 2)
    pygame.image.save(shield, "assets/images/powerup_shield.png")
    powerups['shield'] = shield
    
    power = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.circle(power, YELLOW, (10, 10), 10)
    pygame.draw.polygon(power, RED, [(10, 2), (18, 10), (10, 18), (2, 10)])
    pygame.image.save(power, "assets/images/powerup_power.png")
    powerups['power'] = power
    
    return powerups

# Create explosion frames
def create_explosion_sprites():
    sizes = [20, 30, 40, 50, 60]
    for i, size in enumerate(sizes):
        explosion = pygame.Surface((size, size), pygame.SRCALPHA)
        radius = size // 2
        center = (radius, radius)
        
        color = (255, 255 - (i * 40), 0)
        for r in range(radius, 0, -4):
            intensity = max(0, min(255, 255 - (radius - r) * 8))
            explosion_color = (color[0], intensity, 0)
            pygame.draw.circle(explosion, explosion_color, center, r)
        
        pygame.image.save(explosion, f"assets/images/explosion{i+1}.png")

# Create all sprites
print("Creating sprites...")
create_player_sprite()
create_enemy_sprites()
create_bullet_sprite()
create_powerup_sprites()
create_explosion_sprites()
print("All sprites created successfully in assets/images/")

# Game setup
player_sprite = pygame.image.load("assets/images/player.png")
enemy_sprites = create_enemy_sprites()
bullet_sprite = create_bullet_sprite()
powerup_sprites = create_powerup_sprites()
explosion_sprites = create_explosion_sprites()

# Game loop
running = True
player_x, player_y = screen_width // 2, screen_height - 60
player_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement (basic left-right movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Prevent player from moving out of bounds
    player_x = max(0, min(screen_width - 50, player_x))

    # Check if player collides with any enemy (example collision handling)
    # In a real game, you would add actual collision logic
    if player_y <= 0:  # Example condition for losing a life
        player_lives -= 1
        if player_lives <= 0:
            print("Game Over")
            running = False  # End the game

    # Clear screen and update here
    screen.fill(BLACK)

    # Draw player
    screen.blit(player_sprite, (player_x, player_y))

    # Example of drawing enemies (simplified)
    for enemy in enemy_sprites:
        screen.blit(enemy, (100, 100))  # You should use actual coordinates here

    # Draw lives indicator (e.g., display mini player ships)
    for i in range(player_lives):
        screen.blit(pygame.image.load("assets/images/player_mini.png"), (10 + i * 30, 10))

    pygame.display.flip()  # Update the display

    # Control the frame rate (e.g., 60 FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()  # Close the game properly
