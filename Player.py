import pygame 
import os 
import Obj 
class Player(Obj.Obj):
    name='Player'
    vspeed=1
    x,y=3,5
    image_speed=.025
    sprites='Felix/Sprite_felix_run'
    
    player_jump_count=0
    player_jump =True

    fix=False 

    def jump(self,keys):
        #jump 
        if keys[pygame.K_SPACE] and not self.player_jump:
            self.player_jump = True 

        # Check if player is jumping
        if self.player_jump:
            if self.player_jump_count > 0:
                self.y -=5
                self.player_jump_count -= 1                 

    def gravity(self):
        w=self.sprite_width
        h=self.sprite_height+self.vspeed
        if not self.collision.collision_rectangle(self.x-w,self.y,self.x+w,self.y+h,'Wall'):
            self.y+=self.vspeed #if self.player_jump and self.player_jump_count<=0 else 0 #we will see if the player are jump or falling down 
        else:
            #we will see if collision with the floor
            self.player_jump = False
            self.player_jump_count = 20    

         
    def move(self,keys):
        self.speed=0
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: #97
            self.image_xscale=1
            self.speed=1
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image_xscale=-1
            self.speed=1
            
        #we will see if be a wall in front of the player
        w=(self.sprite_width/2*self.image_xscale)+self.speed
        h=self.sprite_height/2
        if not (self.collision.collision_rectangle(self.x,self.y-h,self.x+w,self.y+h,'Wall')):
            self.x+=self.speed*(self.vspeed*self.image_xscale)
    
    def Fix(self,keys):
        if keys[pygame.K_p]: 
            self.sprites='Felix/Sprite_felix_fix'
            self.fix=True 
            self.image_speed=.05
        else:
            self.sprites='Felix/Sprite_felix_run'
            self.fix=False
            self.image_speed=.025

        #we will see if felix is collision with a windows 
        if self.fix:
            w=(self.sprite_width/2*self.image_xscale)+self.speed
            h=self.sprite_height/2
            windosCollision=(self.collision.collision_rectangle(self.x,self.y-h,self.x+w,self.y+h,'windows'))  
            if windosCollision:
                windosCollision[1].image=0

    def step(self,event):
        self.gravity()
        if not self.fix:
            self.move(event)
        self.Fix(event)
        self.jump(event)

