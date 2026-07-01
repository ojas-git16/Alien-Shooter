import pygame
import alien
import bullet
import player

pygame.init()
screen=pygame.display.set_mode((800,800))
running=True
clock=pygame.time.Clock()
space_was_pressed = False   # tracks previous frame's key state, so holding Space fires only once
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    if not alien.game_over:
        alien.spawn()
        alien.movement()
        player.movement()
        bullet.movement()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not space_was_pressed:
        bullet.fire(player.x, player.y)
    space_was_pressed = keys[pygame.K_SPACE]

    screen.fill((0,0,0))
    player.draw(screen)
    alien.draw(screen)
    bullet.collision(bullet.bullets,alien.alienships,alien.width,alien.height)
    bullet.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()