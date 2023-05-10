import pygame
import sys
#PANTALLA = pygame.display.set_mode((800, 600))


def draw(puntaje,PANTALLA):
	puntaje=f'{puntaje}'
	pygame.init()

	fondo = pygame.image.load("gmo.jpeg")
	# Especificación de título
	pygame.display.set_caption('Score')
	PANTALLA.blit(fondo, (0, 0))

	funete = pygame.font.Font(None, 80)
	textoImg1 = funete.render("SCORE", 0, (255, 255, 255))
	textoImg2 = funete.render(puntaje, 0, (255, 255, 255))

	# Calcular la posición del texto en la superficie para centrarlo
	mitdPant=PANTALLA.get_rect().center
	text_rect = textoImg1.get_rect()
	text_rect.center = mitdPant

	text_rect2 = textoImg2.get_rect()
	text_rect2.center = (mitdPant[0],mitdPant[1]+100)


	# Dibujar el texto en la superficie
	PANTALLA.blit(textoImg1, text_rect)
	PANTALLA.blit(textoImg2, text_rect2)

'''
draw(10)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
'''