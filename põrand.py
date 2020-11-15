import pygame as pg
from pygame_init import *

class Põrand:    
    def __init__(self,x1,x2,y):
        self.y = y
        self.x1 = x1
        self.x2 = x2
    
    def draw(self):
        pg.draw.line(aken, (255, 0, 0), (self.x1,self.y),(self.x2,self.y))
        #seinad
        pg.draw.line(aken, (255, 0, 0), (self.x1,self.y),(self.x1,kõrgus))
        pg.draw.line(aken, (255, 0, 0), (self.x2,self.y),(self.x2,kõrgus))