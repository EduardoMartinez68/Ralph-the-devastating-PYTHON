import pygame
#import self as self

import Obj
import Object
import random
class Edificio(Obj.Obj):
    name = 'Edificio'
    x, y = 3, 5
    image_speed=0
    sprites = 'Edificio/edificio'

class Edificio2(Obj.Obj):
    name = 'Edificio'
    x, y = 3, 5
    image_speed=0
    sprites = 'Edificio/edificio2'
class Super(Obj.Obj):
    name = 'Super'
    x, y = 3, 5
    image_speed = 0
    sprites = 'Edificio/sup'
class Entrada(Obj.Obj):
    name = 'entrada'
    x, y = 3, 5
    image_speed = 0
    sprites = 'Edificio/puerta'
