import pygame 
import Player
import Object
import ralph

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Set the caption of the window
pygame.display.set_caption("Ralph the devastating")

Objects=[]

#create the room 
for i in range(20):
    Objects.append(Object.Wall(screen,Objects,i*32,500))

Objects.append(Object.Wall(screen,Objects,5*32,410))
Objects.append(Object.Wall(screen,Objects,9*32,480))

player=Player.Player(screen,Objects,0,100)
Objects.append(player)


Ralp=ralph.Ralph(screen,Objects,40,3)
Objects.append(Ralp)
Objects.append(Object.Wall(screen,Objects,10*32,3))
Objects.append(Object.Wall(screen,Objects,10,3))

Objects.append(Object.Windows(screen,Objects,10,410))


# Run the game loop
running = True

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass
    keys = pygame.key.get_pressed()
    player.step(keys)
    Ralp.step()

    # Fill the background color of the window
    screen.fill((0, 0, 0))  # black color

    #update all the obj on screen 
    for i in Objects:
        i.update()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
