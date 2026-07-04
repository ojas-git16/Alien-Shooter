import pygame
import random

# -------------------------------
# Alien Settings
# -------------------------------
width = 65
height = 65
speed = 2

alienships = []

spawn_timer = 0
spawn_delay = 120

game_over = False

# -------------------------------
# Load Alien Image
# -------------------------------
alien_img = pygame.image.load("assets/alien_ship.png")
alien_img = pygame.transform.scale(alien_img, (width, height))

# -------------------------------
# Spawn Alien
# -------------------------------
def spawn():
    global spawn_timer, spawn_delay, speed

    spawn_timer += 1

    # Increase spawn rate every 10 seconds
    if spawn_timer % 600 == 0 and spawn_delay >= 80:
        spawn_delay -= 10

    # Increase alien speed after 30 seconds
    if spawn_timer == 1800:
        speed += 1

    if spawn_timer % spawn_delay == 0:
        x = random.randint(0, 800 - width)
        alienships.append({
            "x": x,
            "y": -height
        })

# -------------------------------
# Alien Movement
# -------------------------------
def movement(player_rect):
    global game_over

    for alien in alienships:
        alien["y"] += speed

    for alien in alienships:
        alien_rect = pygame.Rect(
            alien["x"],
            alien["y"],
            width,
            height
        )

        # Game ends if an alien touches the player
        # or reaches the bottom
        if alien_rect.colliderect(player_rect) or alien["y"] >= 800:
            print("Game Over")
            game_over = True
            return

# -------------------------------
# Draw Aliens
# -------------------------------
def draw(screen):
    for alien in alienships:
        screen.blit(alien_img, (alien["x"], alien["y"]))

# -------------------------------
# Reset Game
# -------------------------------
def reset():
    global alienships
    global spawn_timer
    global spawn_delay
    global speed
    global game_over

    alienships.clear()
    spawn_timer = 0
    spawn_delay = 120
    speed = 2
    game_over = False