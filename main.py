import pygame

pygame.init()
pygame.mixer.init()

import alien
import bullet
import player

# -------------------------------
# Sounds
# -------------------------------
pygame.mixer.music.load("Sounds/Professor.mp3")
pygame.mixer.music.play(-1)

game_over_sound = pygame.mixer.Sound("Sounds/game_over_sound.mp3")
game_over_sound_played = False

# -------------------------------
# Window
# -------------------------------
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Alien Shooter")

# -------------------------------
# Background
# -------------------------------
background = pygame.image.load("assets/space_bg.png")
background = pygame.transform.scale(background, (800, 800))

running = True
clock = pygame.time.Clock()

space_was_pressed = False

# -------------------------------
# Fonts
# -------------------------------
font = pygame.font.Font(None, 36)
game_end = pygame.font.Font(None, 100)
restart = pygame.font.Font(None, 36)

# -------------------------------
# Game Loop
# -------------------------------
while running:

    # ---------------------------
    # Events
    # ---------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r and alien.game_over:

                alien.reset()
                bullet.reset()
                player.reset()

                game_over_sound_played = False
                pygame.mixer.music.play(-1)

    # ---------------------------
    # Update
    # ---------------------------
    if not alien.game_over:

        alien.spawn()
        player.movement()
        alien.movement(player.player_rect)
        bullet.movement()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not space_was_pressed:
        bullet.fire(player.x, player.y)

    space_was_pressed = keys[pygame.K_SPACE]

    # ---------------------------
    # Draw Background
    # ---------------------------
    screen.blit(background, (0, 0))

    score_text = font.render(
        f"Score: {bullet.score}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    player.draw(screen)
    alien.draw(screen)

    bullet.collision(
        bullet.bullets,
        alien.alienships,
        alien.width,
        alien.height
    )

    bullet.draw(screen)

    # ---------------------------
    # Game Over
    # ---------------------------
    if alien.game_over and not game_over_sound_played:

        game_over_sound.play()
        game_over_sound_played = True

        pygame.mixer.music.stop()

    if alien.game_over:

        screen.blit(background, (0, 0))

        text = game_end.render(
            "GAME OVER",
            True,
            (255, 100, 0)
        )

        text_rect = text.get_rect(center=(400, 350))

        text_restart = restart.render(
            "Press 'R' to Play Again",
            True,
            (255, 255, 255)
        )

        final_score = font.render(
            f"Score: {bullet.score}",
            True,
            (255, 255, 255)
        )

        screen.blit(text, text_rect)
        screen.blit(final_score, (340, 450))
        screen.blit(text_restart, (260, 500))

    pygame.display.update()
    clock.tick(60)

pygame.quit()