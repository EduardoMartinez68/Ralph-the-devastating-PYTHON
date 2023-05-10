import pygame 
class collisionMask():
    def __init__(self,object):
        self.object=object

    def collision_rectangle(self,x,y,x2,y2,nameObj):
        #update coordinates
        #x,x2=70,80 if  80>70 else 80,70
        if x>x2:
            x,x2=x2,x
        else:
            x,x2
        if y>y2:
            y,y2=y2,y 
        else:
            y,y2

        #we get all the object with the name of the object that we will see if the rectangle collision
        for obj in self.object.ObjRoom:
            if obj.name==nameObj:
                #if (obj.x>=x and obj.x<=x2) and (obj.y>=y and obj.y<=y2):
                w=obj.sprite_width/2
                h=obj.sprite_height/2
                if (obj.x+w>=x and obj.x-w<=x2) and (obj.y+h>=y and obj.y-h<=y2):
                    return True , obj 
        
        return False 