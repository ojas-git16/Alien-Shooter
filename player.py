import pygame

x=400
y=730
speed=5
width=45

def movement():
    global x,y
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed
    if x>=800-width:
        x=800-width
    if x<=width:
        x=width
    if y>=800-width:
        y=800-width
    if y<width:
        y=width
def draw(screen):
    pygame.draw.rect(screen,(255,0,255),(x,y,width,width))