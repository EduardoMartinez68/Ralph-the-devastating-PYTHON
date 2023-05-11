import Obj 
class Plataform():
    def __init__(self) -> None:
        pass

class Wall(Obj.Obj):
    name='Wall'
    sprites='Wall'

class WallInvisible(Wall):
    sprites='WallInvisible'

class Plataformer(Wall):
    sprites='plataformer_1'

class PlataformerWindows(Wall):
    sprites='plataformer_2'

class brick(Obj.Obj):
    name='brick'
    sprites='brick'
    vspeed=3

    def gravity(self):
        '''
        w=self.sprite_width
        h=self.sprite_height+self.vspeed
        if not self.collision.collision_rectangle(self.x-w,self.y,self.x+w,self.y+h,'Wall'):
            self.y+=self.vspeed #if self.player_jump and self.player_jump_count<=0 else 0 #we will see if the player are jump or falling down '''
        self.y+=self.vspeed

        #we will if the bick is out of the room 
        if self.y>=610:
            self.instance_destroy()

    def update(self):
        self.draw_self()
        self.gravity()

class Windows(Obj.Obj):
    name='windows'
    sprites='windows'
    image_speed=0
    image=1
    
    def choose_windows(self):
        self.image_index=0 if self.image_index==1 else 1

    def update(self):
        self.draw_self() 

class powerUpPai(Obj.Obj):
    name='pai'
    sprites='pai'
    time=900
    timeStar=time
    image_speed=0
    image=0

    def selfDestruction(self):
        self.time-=1 if self.time>0 else 0
        #we will watch if the time be for finish 
        if self.time>=self.timeStar/4 and self.time<=self.timeStar/2:
            self.image_speed=.125
        elif self.time<=self.timeStar/4 and self.time>=1:
            self.image_speed=.25 
        elif self.time<=0:
            self.instance_destroy()

    def activatePowerUp(self,player):
        player.powerPai=True 
        player.alarm[0]=180

    def beEatingForFelix(self):
        #we will see if be a wall in front of the player
        w=self.sprite_width/2
        h=self.sprite_height/2
        player=self.collision.collision_rectangle(self.x-w,self.y-h,self.x+w,self.y+h,'Player')

        #the player will activate his power up
        if player:
            self.activatePowerUp(player[1])
            self.instance_destroy()

    def update(self):
        self.draw_self() 
        self.beEatingForFelix()
        self.selfDestruction() 


class powerUpHelmet(powerUpPai):
    name='helmet'
    sprites='helmet'


    def activatePowerUp(self,player):
        player.powerHelmet=True 
        player.alarm[1]=180