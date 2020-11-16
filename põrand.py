import pygame as pg
from pygame_init import *

class Põrand:    
    def __init__(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    
    def draw(self):
        #ülemine äär
        pg.draw.line(aken, (255, 0, 0), (self.x1,self.y1),(self.x2,self.y1))
        #alumine äär
        pg.draw.line(aken, (255, 0, 0), (self.x1,self.y2),(self.x2,self.y2))
        #seinad
        pg.draw.line(aken, (255, 0, 0), (self.x1,self.y1),(self.x1,self.y2))
        pg.draw.line(aken, (255, 0, 0), (self.x2,self.y1),(self.x2,self.y2))