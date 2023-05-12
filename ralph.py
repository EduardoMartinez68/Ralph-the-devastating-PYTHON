import pygame 
import Obj 
import Object
import random
class Ralph(Obj.Obj):
    name='Ralph'
    vspeed=.8
    x,y=3,5
    image_speed=.0125
    sprites='Ralph/Sprite_ralph_move'


    loser=False
    time=30
    speed=1
    canAtack=True 
    up=False

    def gravity(self):
        w=self.sprite_width
        h=self.sprite_height+self.vspeed
        if not self.collision.collision_rectangle(self.x-w,self.y,self.x+w,self.y+h,'Wall'):
            self.y+=self.vspeed #if self.player_jump and self.player_jump_count<=0 else 0 #we will see if the player are jump or falling down 

         


    def move(self):
        #we will see if be a wall in front of ralph
        w=(self.sprite_width/2*self.image_xscale)+self.speed
        h=self.sprite_height/2
        if not (self.collision.collision_rectangle(self.x,self.y-h,self.x+w,self.y+h,'Wall')):
            self.x+=self.speed*(self.vspeed*self.image_xscale)
        else:
            self.image_xscale= -1 if self.image_xscale==1 else 1 #choose of direction 

    def timeAtack(self):
        if self.time>0:
            self.time-=.125
        else:
            self.canAtack=False 
            self.time=40

            #choose the sprite of ralph
            self.sprites='Ralph/Sprite_ralph_atack_one' 

            #we will create the bick of atack
            for i in range(4):
                self.ObjRoom.append(Object.brick(self.screen,self.ObjRoom,random.randint(260, 517),self.y))

    def timeMove(self):
        if self.time>0:
            self.time-=.125
        else:
            self.canAtack=True      
            self.time=120  

            #choose the sprite of ralph
            self.sprites='Ralph/Sprite_ralph_move' 

    def atack(self):
        space=12
        if self.up:
            #self.y+=space
            self.up=False
        else:
            #self.y-=space
            self.up=True 

    def updateVariables(self):
        self.image_speed=.125

    def step(self):
        if self.loser:
            self.gravity()
        else:
            if self.canAtack:
                self.move()
                self.timeAtack()
            else:
                self.atack()
                self.timeMove()
