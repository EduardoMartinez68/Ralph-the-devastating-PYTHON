import pygame 
from physical import Collision
import os 
class Obj:
    #character
    name=''
    x,y=0,0

    #grafich 
    sprites=''
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
    gravity=1
    space=1
    speed=1
    vspeed=0
    hspeed=0

    star=True

    def __init__(self,screen,ObjRoom,x,y):
        self.x=x
        self.y=y
        self.screen=screen
        self.ObjRoom=ObjRoom
        self.collision=Collision.collisionMask(self)
        self.loadSprite()

    def loadSprite(self):
        self.sprite_index=[]
        path=f'{self.getPath()}/Sprite/{self.sprites}/'
        for i in self.get_name_sprite(path):
            self.sprite_index.append(pygame.image.load(path+i))

        #get the size of the sprite 
        sprite_size = self.sprite_index[0].get_size()
        self.sprite_width=sprite_size[0]
        self.sprite_height=sprite_size[1]

    def get_name_sprite(self,path):
        name_sprite = []
        for sprite in os.listdir(path):
            ruta_archivo = os.path.join(path, sprite)
            if os.path.isfile(ruta_archivo):
                name_sprite.append(sprite)
        return name_sprite

    def getPath(self):
        # Get the absolute path of the current file
        return os.path.dirname(os.path.abspath(__file__))
    
    def step(self):
        pass
    
    def draw_self(self):
        self.loadSprite()
        #update sprite 
        self.image+=self.image_speed if self.image<(len(self.sprite_index)) else -self.image
        self.image_index=0 if self.image>=len(self.sprite_index) else int(self.image)

        #change the scale
        image_direction=False if self.image_xscale==1 else True 
        image = pygame.transform.flip(self.sprite_index[self.image_index], image_direction, False)
        self.screen.blit(image, (self.x, self.y))


    def update(self):
        self.draw_self()