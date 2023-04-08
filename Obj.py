import pygame 
from physical import Collision
import os 
class Obj():
    #character
    name=''
    x,y=0,0

    #grafich 
    sprites=[]
    sprite_index=[]
    image_index=0
    image_speed=0
    image_xscale=1
    image=0

    sprite_width,sprite_height=0,0

    #physical 
    player_jump=False
    player_jump_vel = 10
    player_jump_count = 10
    gravity=0.9
    space=1
    speed=1
    vspeed=0
    hspeed=0

    def __init__(self,screen,ObjRoom,x,y):
        self.x=x
        self.y=y
        self.screen=screen
        self.ObjRoom=ObjRoom
        self.collision=Collision.collisionMask(self)
        self.loadSprite()

    def loadSprite(self):
        path=self.getPath()+'/Sprite/'
        for i in self.sprites:
            self.sprite_index.append(pygame.image.load(path+i))

        #get the size of the sprite 
        sprite_size = self.sprite_index[0].get_size()
        self.sprite_width=sprite_size[0]
        self.sprite_height=sprite_size[1]

    def getPath(self):
        # Get the absolute path of the current file
        return os.path.dirname(os.path.abspath(__file__))
    
    def step(self):
        pass
    
    def draw_self(self):
        #update sprite 
        self.image+=self.image_speed if self.image<(len(self.sprite_index)) else -self.image
        self.image_index=0 if self.image>=len(self.sprite_index) else int(self.image)

        #change the scale
        self.screen.blit(self.sprite_index[self.image_index], (self.x, self.y))


    def update(self):
        self.draw_self()