import pygame

# -------------------------------
# Bullet Settings
# -------------------------------
width = 5
height = 10
speed = 8

score = 0

explosion_sound = pygame.mixer.Sound("Sounds/explosion.mp3")
laser_sound = pygame.mixer.Sound("Sounds/laser.mp3")

# List to store all bullets
bullets = []


# -------------------------------
# Fire Bullet
# -------------------------------
def fire(player_x, player_y):
    global bullets

    player_width = 65

    bullet_x = player_x + player_width // 2 - width // 2
    bullet_y = player_y - height

    bullets.append({
        "x": bullet_x,
        "y": bullet_y
    })

    laser_sound.play()


# -------------------------------
# Bullet Movement
# -------------------------------
def movement():
    global bullets

    for bullet in bullets:
        bullet["y"] -= speed

    # Remove bullets that leave the screen
    bullets = [bullet for bullet in bullets if bullet["y"] > 0]


# -------------------------------
# Draw Bullets
# -------------------------------
def draw(screen):
    for bullet in bullets:
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (bullet["x"], bullet["y"], width, height)
        )


# -------------------------------
# Bullet-Alien Collision
# -------------------------------
def collision(bullets, alienships, alien_width, alien_height):
    global score

    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(
            bullet["x"],
            bullet["y"],
            width,
            height
        )

        for alien in alienships[:]:
            alien_rect = pygame.Rect(
                alien["x"],
                alien["y"],
                alien_width,
                alien_height
            )

            if bullet_rect.colliderect(alien_rect):
                bullets.remove(bullet)
                alienships.remove(alien)

                explosion_sound.play()
                score += 10
                break


# -------------------------------
# Reset Game
# -------------------------------
def reset():
    global bullets, score

    bullets = []
    score = 0