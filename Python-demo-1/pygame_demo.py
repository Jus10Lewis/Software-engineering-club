import pygame
import sys
import random

# 1. Initialize Pygame
pygame.init()

# 2. Setup the Display
# We create a window that is 800 pixels wide and 600 pixels tall.
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 3. Define Colors (Using RGB values)
BACKGROUND_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 100, 255)
ENEMY_COLOR = (255, 50, 50)

# 4. Player Properties
# We start the player in the middle of the screen
player_pos = [screen_width // 2, screen_height // 2]
player_radius = 25
player_speed = 5

# 5. Enemy Properties
# The enemy is a red circle that moves when collected.
enemy_radius = 15
enemy_pos = [
    random.randint(enemy_radius, screen_width - enemy_radius),
    random.randint(enemy_radius, screen_height - enemy_radius)
]
score = 0

# 6. The Game Loop
# This loop runs continuously until we close the window.
running = True
clock = pygame.time.Clock()

while running:
    # --- A. Event Handling ---
    # We check if the user clicked the [X] to close the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- B. Movement Logic ---
    # Check which keys are currently being pressed.
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # --- C. Boundary Checks ---
    # Keep the player inside the screen boundaries.
    if player_pos[0] < player_radius:
        player_pos[0] = player_radius
    if player_pos[0] > screen_width - player_radius:
        player_pos[0] = screen_width - player_radius
    if player_pos[1] < player_radius:
        player_pos[1] = player_radius
    if player_pos[1] > screen_height - player_radius:
        player_pos[1] = screen_height - player_radius

    # --- D. Collision Detection ---
    # Check if the player is touching the enemy.
    # We use the distance formula (Pythagorean theorem) to check for overlaps.
    distance = ((player_pos[0] - enemy_pos[0])**2 + (player_pos[1] - enemy_pos[1])**2)**0.5
    
    if distance < player_radius + enemy_radius:
        # Increment score and print it
        score += 1
        print(f"Score: {score}")
        
        # Move the enemy to a new random spot!
        enemy_pos = [
            random.randint(enemy_radius, screen_width - enemy_radius),
            random.randint(enemy_radius, screen_height - enemy_radius)
        ]

    # --- E. Drawing ---
    # First, clear the screen with a background color.
    screen.fill(BACKGROUND_COLOR)

    # Draw the enemy (red circle).
    pygame.draw.circle(screen, ENEMY_COLOR, enemy_pos, enemy_radius)

    # Draw our player (blue circle).
    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, player_radius)

    # Update the display to show the changes.
    pygame.display.flip()

    # --- F. Control the Frame Rate ---
    # Limit the demo to 60 frames per second.
    clock.tick(60)

# 7. Clean up and exit
pygame.quit()
sys.exit()
