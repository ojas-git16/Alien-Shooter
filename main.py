import pygame
import alien
import player

pygame.init()
screen=pygame.display.set_mode((800,800))
running=True
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    if not alien.game_over:
        alien.spawn()
        alien.movement()
        player.movement()
    
    screen.fill((0,0,0))
    player.draw(screen)
    alien.draw(screen)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()