import pygame as pg
from abi import *

class Kuul:
    def __init__(self, x, y, suund, relv):
        self.x = x
        self.y = y
        self.raadius = relv.raadius
        self.värv = relv.värv
        self.vel = relv.vel * suund
        self.dmg = relv.dmg
        
    def draw(self, aken):
        pg.draw.circle(aken, self.värv, (self.x , self.y), self.raadius)
            
class Raha:
    def __init__(self,x,y,v,suund,xoff,mkr):
        self.x = x
        self.y = y
        self.v = v
        self.suund = suund
        self.xoff = xoff
        self.kukkumas = True
        self.mkr = mkr
    def kukub(self, dt):
        self.y += 0.5*(self.v**2)*dt
        self.x += self.xoff 
        self.v -= 1
        if self.y+5 >= self.mkr:
            self.y = self.mkr-5
            self.kukkumas = False
    
    def draw(self, aken):
        pg.draw.circle(aken, (255,215,0), (self.x , self.y), 5)
            
class Relvad:
    def __init__(self, dmg, cd, raadius, värv, vel, equipped, unlocked, nimi, nimi_data):
        self.dmg = dmg
        self.cd = cd
        self.raadius = raadius
        self.värv = värv
        self.vel = vel
        self.unlocked = unlocked
        self.nimi = nimi
        self.nimi_data = nimi_data
        
class Varustus:
    def __init__(self, speed, armor, equipped, unlocked, nimi, x, y):
        self.armor = armor
        self.speed = speed
        self.equipped = equipped
        self.unlocked = unlocked
        self.collision = False
        self.nimi = nimi
        self.x = x
        self.y = y
        self.laius = 60
        self.kõrgus = 60
        self.aeg = 0
        
    def equip(self, Tom):
        if not self.equipped:
            self.equipped = True
            Tom.armor += self.armor
            
    def unequip(self, Tom):
        if self.equipped:
            self.equipped = False
            Tom.armor -= self.armor

class Collectable():
    def __init__(self, x, y, laius, kõrgus, asi):
        self.x = x
        self.y = y
        self.laius = laius
        self.kõrgus = kõrgus
        self.asi = asi
    
    def draw(self, aken):
        if not self.unlocked:
            pg.draw.rect(aken, (255,255,0), (self.x, self.y, self.laius, self.kõrgus))
        if not self.unlocked and self.collision:
            self.unlocked = True
            self.aeg = pg.time.get_ticks()
        self.unlocked_sõnum()
        
    def unlocked_sõnum(self):
        aeg = pg.time.get_ticks()
        if self.unlocked and self.aeg + 2000 >= aeg:
            #self.aeg += 1
            TextSurf, TextRect = text_objects("Sa leidsid midagi", largeText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            pg.display.update()
    