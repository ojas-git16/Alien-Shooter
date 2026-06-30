import pygame

width = 5       # bullet width
height = 10     # bullet height
speed = 8

bullets = []    # there might be multiple bullets at the same time

def fire(player_x, player_y):
    global bullets
    player_dim = 45           # already fixed, h=45, w=45
    bul_x = player_x + player_dim // 2 - width // 2
    bul_y = player_y - height
    bullets.append({"x":bul_x, "y":bul_y})

def movement():
    global bullets
    for bullet in bullets:
        bullet["y"]-=speed
    
# remove bullets once they leave the top of the screen, so list does not overflow
    new_bullets = []
    for bullet in bullets:
        if bullet["y"] > 0:
            new_bullets.append(bullet)
    bullets = new_bullets

def draw(screen):
    for bullet in bullets:
        pygame.draw.rect(screen, (255,255,0), (bullet["x"], bullet["y"], width, height))



