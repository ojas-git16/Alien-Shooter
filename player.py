import pygame

# -------------------------------
# Player Settings
# -------------------------------
x = 400
y = 730
speed = 5

width = 65
height = 65

# -------------------------------
# Load Player Image
# -------------------------------
player_img = pygame.image.load("assets/player_ship.png")
player_img = pygame.transform.scale(player_img, (width, height))

player_rect = pygame.Rect(x, y, width, height)

# -------------------------------
# Player Movement
# -------------------------------
def movement():
    global x, y, player_rect

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Keep player inside the screen
    if x < 0:
        x = 0
    elif x > 800 - width:
        x = 800 - width

    if y < 0:
        y = 0
    elif y > 800 - height:
        y = 800 - height

    player_rect = pygame.Rect(x, y, width, height)

# -------------------------------
# Draw Player
# -------------------------------
def draw(screen):
    screen.blit(player_img, (x, y))

# -------------------------------
# Reset Player
# -------------------------------
def reset():
    global x, y, player_rect

    x = 400
    y = 730
    player_rect = pygame.Rect(x, y, width, height)