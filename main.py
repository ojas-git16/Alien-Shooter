import pygame
import player

pygame.init
screen=pygame.display.set_mode((800,800))
running=True
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0))
    player.draw(screen)
    player.movement()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
