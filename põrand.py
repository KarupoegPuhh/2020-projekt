import pygame as pg
from pygame_init import *

class põrand:
    instances = []
    
    def __init__(self,x1,x2,y):
        self.__class__.instances.append(self)

        self.y = y
        self.x1 = x1
        self.x2 = x2
    
    def draw(self, aken):
        pg.draw.line(aken, (255, 0, 0), (self.x1,self.y),(self.x2,self.y))
        #seinad
        pg.draw.line(aken, (255, 0, 0), (self.x1,self.y),(self.x1,kõrgus))
        pg.draw.line(aken, (255, 0, 0), (self.x2,self.y),(self.x2,kõrgus))

def pole_sein_v(dt,v,x,y,lai,pikk,umb=0,obj=põrand):
    #absoluutväärtus vel
    if v < 0:
        v = -v
    #seinad vasakule minnes
    for i in obj.instances:
        if x <= i.x2+(v*dt)+umb and x > i.x2 + 1-umb and not y < i.y - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
            return False
    return True
    
def pole_sein_p(dt,v,x,y,lai,pikk,umb=0,obj=põrand):
    #seinad paremale minnes
    for i in obj.instances:
        if x+lai+(v*dt) >= i.x1 and x+lai < i.x1 + 1 and not y < i.y - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
            return False
    return True
