import os
import pygame
###########################ESSENTIAL###############################
pygame.init() # Reset 

# setting screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


# setting screen title
pygame.display.set_caption("Nado Pang") # name of game

# FPS
clock = pygame.time.Clock()
###################################################################

# 1. game setting
current_path = os.path.dirname(__file__) # return position of current file
image_path = os.path.join(current_path, "images") # return position of "images" folder

# draw background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# make stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # to put charater on the height of stage

# event loop
running = True
while running:
    dt = clock.tick(30) # setting fps/s

    # 2. process of event    
    for event in pygame.event.get(): # did any events happen?
        if event.type == pygame.QUIT: # did quit(event) happen?
            running = False # game isn't running

    # 3. justice of character's position

    # 4. process of collision

    # 5 draw on screen
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))

# end pygame
pygame.quit
