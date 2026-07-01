import pygame
import random

width = 45
height = 45
speed = 2

alienships=[]       # there might be multiple aliens on the screen at same time

spawn_timer = 0
spawn_delay = 120   # clock is set to 120. alien spawns every alternate second

game_over = False

def spawn():
    global spawn_timer
    global spawn_delay
    global speed
    spawn_timer += 1
    if (spawn_timer%600==0 and spawn_delay >= 80):   # increases alien spawn speed with time
        spawn_delay-=10
    if (spawn_timer == 1800):
        speed+=1
    if (spawn_timer%spawn_delay)==0:
        x = random.randint(0, 800-width)
        alienships.append({"x" : x , "y" : -height})  # y=-height because it appears above the window

def movement():
    global alienships
    global game_over
    for alien in alienships:
        alien["y"]+=speed

    for alien in alienships:
        if (alien["y"] >= 800):
            print("Game ended")
            game_over = True
            return
    
    # in case game down not end, if alien reaches bottom so updating the aliens list, so it does not overflow
    # new_aliens = []
    # for alien in alienships:
    #     if(alien["y"]<800):
    #         new_aliens.append(alien)
    # alienships = new_aliens
def draw(screen):
    for alien in alienships:
        pygame.draw.rect(screen, (0, 255, 0), (alien["x"], alien["y"], width, height))

