import Obj 
class Plataform():
    def __init__(self) -> None:
        pass

class Wall(Obj.Obj):
    name='Wall'
    sprites='Wall'

class brick(Obj.Obj):
    name='brick'
    sprites='brick'
    vspeed=3

    def gravity(self):
        w=self.sprite_width
        h=self.sprite_height+self.vspeed
        if not self.collision.collision_rectangle(self.x-w,self.y,self.x+w,self.y+h,'Wall'):
            self.y+=self.vspeed #if self.player_jump and self.player_jump_count<=0 else 0 #we will see if the player are jump or falling down 


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