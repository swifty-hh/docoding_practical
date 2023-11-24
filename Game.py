import pygame

pygame.init() # Reset (essential)

# setting screen size
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# setting screen title
pygame.display.set_caption("Nado Game") # name of game

# FPS
clock = pygame.time.Clock()

#  load image
background = pygame.image.load("C:/Users/hhj56/Desktop/PythonWorkspace/pygame_basic/background.png")

# load character
character = pygame.image.load("C:/Users/hhj56/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size # size of character
character_width = character_size[0] # width of charater
character_height = character_size[1] # height of character
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# moving
to_x = 0
to_y = 0

# moving speed
character_speed = 1

# enemy character
enemy = pygame.image.load("C:/Users/hhj56/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# font
game_font = pygame.font.Font(None, 40) # make font(font, size)

# total time
total_time = 10

# starting time
start_ticks = pygame.time.get_ticks() # get starting tick

# event loop
running = True
while running:
    dt = clock.tick(30) # setting fps/s

#    print("fps : " + str(clock.get_fps()))
    
    for event in pygame.event.get(): # did any events happen?
        if event.type == pygame.QUIT: # did quit(event) happen?
            running = False # game isn't running

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # move character left
                to_x -= character_speed     # to_x == to_x - character_speed
            elif event.key == pygame.K_RIGHT: # move character right
                to_x += character_speed
            elif event.key == pygame.K_UP: # move character up
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # move character down
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # x position limitation
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # y posiotion limitation
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # rect's information update for collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #collision check
    if character_rect.colliderect(enemy_rect):
        print("Boom!")
        running = False

    screen.blit(background, (0, 0)) # draw background
    screen.blit(character, (character_x_pos, character_y_pos)) # draw character
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # draw enemy

    # timer
    # calculate passed time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #  1000 divede passed time
    # \ (ms) to show in seconds(s)


    timer = game_font.render(str(float(total_time - elapsed_time)), True, (255, 255, 255))
    # printng str, True, color of str
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("TIME OVER!")
        running = False

    pygame.display.update() # updating display continuosly

# hold
pygame.time.delay(1500) # hold for 1.5 sec

# end pygame
pygame.quit
