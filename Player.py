import pygame 
import os 
import Obj 
class Player(Obj.Obj):
    name='Player'
    vspeed=1.75
    x,y=3,5
    image_speed=1#.025
    sprites='Felix/Sprite_felix_run'
    
    player_jump_count=0
    player_jump =True

    fix=False 

    #interface variables
    life=3
    time=400
    score=0

    #poweer up
    powerPai=False
    sp=0
    powerHelmet=False
    alarm=[0,0]

    def jump(self,keys):
        #jump 
        if keys[pygame.K_SPACE] and not self.player_jump:
            self.player_jump = True 

        # Check if player is jumping
        if self.player_jump:
            if self.player_jump_count > 0:
                self.y -=6
                self.player_jump_count -= 1                 

    def gravity(self):
        w=self.sprite_width/4
        h=self.sprite_height/2
        wall=self.collision.collision_rectangle(self.x-w,self.y+h,self.x+w,self.y+h-self.vspeed,'Wall')

        if not wall:
            self.y+=self.vspeed #if self.player_jump and self.player_jump_count<=0 else 0 #we will see if the player are jump or falling down 
        else:
            if wall[1].y>=self.y+self.vspeed*2:
                if self.player_jump_count<=0:
                    #we will see if collision with the floor
                    self.player_jump = False
                    self.player_jump_count = 20    
            else:
                self.y+=self.vspeed #if self.player_jump and self.player_jump_count<=0 else 0 #we will see if the player are jump or falling down 

         
    def move(self,keys):
        self.speed=0
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: #97
            self.image_xscale=1
            self.speed=1+self.sp
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image_xscale=-1
            self.speed=1+self.sp
            
        #we will see if be a wall in front of the player
        w=((self.sprite_width/4+self.speed)*self.image_xscale)
        h=self.sprite_height/4
        if not (self.collision.collision_rectangle(self.x,self.y,self.x+w,self.y+h,'Wall')):
            self.x+=self.speed*self.image_xscale
    
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
            w=((self.sprite_width/2+self.speed)*self.image_xscale)
            h=self.sprite_height/2
            windosCollision=(self.collision.collision_rectangle(self.x+w,self.y-h,self.x,self.y+h-self.vspeed,'windows'))  
            if windosCollision:
                if windosCollision[1].image!=0:
                    self.score+=10
                    windosCollision[1].image=0

                    #We will see if there are more broken windows on the room 
                    self.seeIfThereAreMoreBroken()

    def seeIfThereAreMoreBroken(self):
        for i in self.ObjRoom:
            if i.name=='windows' and i.image==1:
                return 

        #if not are more broken windows, the player wing 
        self.life=0

    def draw_interface(self):
        y,space,spacex=10,30,220
        xT=120
        xS=xT+spacex
        xV=xS+spacex+30
        self.draw_text("Time:",xT,y) 
        self.draw_text(int(self.time),xT,y+space) 

        self.draw_text("score:",xS,y) 
        self.draw_text(self.score,xS,y+space) 

        #self.draw_text("Life:",xV,y)
        for i in range(self.life):
            self.draw_sprite('items',2,xV+(i*25),y+5)

        #draw power up 
        if self.powerPai:
            self.draw_sprite('items',1,xV,y+space)
        if self.powerHelmet:
            self.draw_sprite('items',0,xV+25,y+space)

    def timeDown(self):
        self.time-=.125/12 if self.time>0 else 0

    def receiveWound(self):
        w=self.sprite_width/4
        h=self.sprite_height
        #we will see if the player collision with a brick 
        collision=self.collision.collision_rectangle(self.x-w,self.y,self.x+w,self.y+h,'brick')
        if collision:
            if not self.powerHelmet: #we will watch if the power up of the helmet is activate
                self.life-=1 
            collision[1].instance_destroy()
            

    def alarmTime(self):
        dis=.1
        self.alarm[0]+= -dis if self.alarm[0]>0 else 0
        self.alarm[1]+= -dis if self.alarm[1]>0 else 0

        self.powerPai=False if self.alarm[0]<=0 else True 
        self.powerHelmet=False if self.alarm[1]<=0 else True    

        self.sp=0 if self.alarm[0]<=0 else 1   

    def updateVariables(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_p]:
            self.image_speed=.45
        else:
            self.image=1
            self.image_speed=0


    def step(self,event):
        self.gravity()
        if not self.fix:
            self.move(event)
        self.Fix(event)
        self.jump(event)
        self.timeDown()
        self.receiveWound()
        self.alarmTime()
