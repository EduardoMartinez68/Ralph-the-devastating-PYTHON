import pygame
import Edificio
import Object
import Player
import ralph
import random


def createBuilding(Objects=[],screen=0):
    x,y=100,0
    #create the room
    #parte inferior del edificio
    edificio = Edificio.Edificio(screen, Objects, 200+x, 300+y)
    Objects.append(edificio)

    #parte superior del edificio
    superi=Edificio.Super(screen, Objects, 200+x, 146+y)
    Objects.append(superi)


    puerta=Edificio.Entrada(screen, Objects, 290+x, 458+y)
    Objects.append(puerta)

    ''''''
    xW=[330,360,430,460,]
    yW=[295,360,410,470]
    for xWindows in xW:
        for yWindows in yW:
            w=Object.Windows(screen,Objects,xWindows,yWindows)
            w.image=random.randint(0, 1)

            Objects.append(w)

            if not yWindows==470:
                Objects.append(Object.PlataformerWindows(screen,Objects,xWindows,yWindows+w.sprite_height))