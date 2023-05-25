import pygame
import button
import os 

#create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ralph the wrecker')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
logo=pygame.image.load('logo.png').convert_alpha()

#create button instances
logo= button.Button(SCREEN_WIDTH/2-225+30,25,logo,.8)

x,y=SCREEN_WIDTH/2-199+30,SCREEN_HEIGHT/2+25
start_button = button.Button(x,y-43, start_img, 0.8)
exit_button = button.Button(x,y+43, exit_img, 0.8)


#game loop
run = True
while run:
	screen.fill((0, 0, 0))

	if start_button.draw(screen):
		import room 
	if exit_button.draw(screen):
		run=False
	if logo.draw(screen):
		pass 
	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()