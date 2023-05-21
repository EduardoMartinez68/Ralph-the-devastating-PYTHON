import pygame
import Edificio
import Object
import Player
import ralph
import random


def createBuilding(Objects=[],screen=0,levels=1):
    x,y=200,407
    #create the room

    #parte inferior del edificio
    for i in range(levels):
        if i==0:
            Objects.append(Edificio.Edificio(screen, Objects, 200+x, y-(212*i)))
        else:
            Objects.append(Edificio.Edificio2(screen, Objects, 200+x, y-(212*i)))

    Objects.append(Edificio.Entrada(screen, Objects, 205+x, 481.5))

    #parte superior del edificio
    Objects.append(Edificio.Super(screen, Objects, 200+x,y-(212*i)-179))

    ''''''
    #xW=[330,360,438,468]
    #yW=[295,360,410,470]
    for i in range(levels):
        m=(212*i)
        xW=[330,360,438,468]
        yW=[310-m,360-m,410-m,470-m] #295
        createWindows(screen,Objects,xW,yW) 


def createWindows(screen,Objects,xW,yW):
    for xWindows in xW:
        for yWindows in yW:
            space=16
            w=Object.Windows(screen,Objects,xWindows,yWindows+space)
            w.image=random.randint(0, 1)

            Objects.append(w)

            if not yWindows==470:
                Objects.append(Object.PlataformerWindows(screen,Objects,xWindows,yWindows+w.sprite_height/2+space))