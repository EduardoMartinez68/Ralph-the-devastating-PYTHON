import pygame
import Edificio
import Object
import Player
import ralph
import random


def createBuilding(Objects=[],screen=0):
    x,y=200,80
    #create the room
    #parte superior del edificio
    superi=Edificio.Super(screen, Objects, 200+x, 146+y)
    Objects.append(superi)

    #parte inferior del edificio 160
    edificio = Edificio.Edificio(screen, Objects, 200+x, 170+y+superi.sprite_height)
    Objects.append(edificio)



    puerta=Edificio.Entrada(screen, Objects, 205+x, 170+y+superi.sprite_height+edificio.sprite_height/2-35)
    Objects.append(puerta)

    ''''''
    xW=[330,360,438,468]
    yW=[295,360,410,470]
    for xWindows in xW:
        for yWindows in yW:
            space=16
            w=Object.Windows(screen,Objects,xWindows,yWindows+space)
            w.image=random.randint(0, 1)

            Objects.append(w)

            if not yWindows==470:
                Objects.append(Object.PlataformerWindows(screen,Objects,xWindows,yWindows+w.sprite_height/2+space))