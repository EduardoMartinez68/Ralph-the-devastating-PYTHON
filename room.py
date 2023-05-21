import pygame 
import Player
import Object
import ralph
import Building
import random
import puntaje

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
level=3
#create the room 
Building.createBuilding(Objects,screen,level)
for i in range(5): #floor
    Objects.append(Object.Wall(screen,Objects,i*175,516))

player=Player.Player(screen,Objects,400,500) #480
Objects.append(player)

#we will to create to ralph 
yRalph=407-(212*(level))-55
Ralp=ralph.Ralph(screen,Objects,11*32,yRalph)
Objects.append(Ralp)

#muros que collisionan con ralph 
Objects.append(Object.WallInvisible(screen,Objects,8*32-10,yRalph))
Objects.append(Object.WallInvisible(screen,Objects,16*32+10,yRalph))

def updateCamera():
    if player.y<=20:
        player.y=500
        for obj in Objects:
            if obj.name!='Player':
                obj.y=obj.y+560

    if player.y>=580:
        player.y=30
        for obj in Objects:
            if obj.name!='Player':
                obj.y=obj.y-560

#time power up 
timePowerUp=30
xW=[330,360,438,468]
yW=[295,360,410,470]

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

    player.draw_interface()
    
    #time power up
    if timePowerUp>0:
        timePowerUp-=.01
    else:
        timePowerUp=30
        power=random.randint(0, 1)
        r=random.randint(0, 3)
        if power==1:
            Objects.append(Object.powerUpHelmet(screen,Objects,xW[r],yW[r]+18))
        else:
            Objects.append(Object.powerUpPai(screen,Objects,xW[r],yW[r]+18))

    #draw the game over 
    if player.life<=0:
        puntaje.draw(player.score,screen)

    # Update the display
    updateCamera()
    pygame.display.update()

# Quit Pygame
pygame.quit()
