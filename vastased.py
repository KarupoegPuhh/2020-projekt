import pygame as pg
from random import randint
from random import choice
import maailm
from player_lisad import *

class Vastane:
    def __init__(self, x, y, laius, pikkus, vel, health, dmg, värv):
        self.laius = laius
        self.pikkus = pikkus
        self.x = x
        self.y = y - self.pikkus
        self.vel = vel
        self.värv = (0, 255, 255)
        self.hitbox = (self.x -1, self.y -1, self.laius+2, self.pikkus+2)
        self.health = health
        self.max_health = health
        self.elus = True
        self.elud_värv = (0,255,0)
        
        #self.seisab = False
                    
    def draw(self, aken):
        if self.health >= self.max_health * 0.8:
            self.elud_värv = (0,255,0)
        elif self.health >= self.max_health * 0.6:
            self.elud_värv = (200,200,0)
        elif self.health >= self.max_health * 0.4:
            self.elud_värv = (255,100,0)
        else:
            self.elud_värv = (255,50,0)
        
        pg.draw.rect(aken, (50,50,50),(self.x, self.y-15, self.laius, 10))
        pg.draw.rect(aken, self.elud_värv ,(self.x, self.y-15, self.health * (self.laius / self.max_health), 10))
        self.hitbox = (self.x -1, self.y -1, self.laius+2, self.pikkus+2)             
        pg.draw.rect(aken, (255,0,0), self.hitbox, 1)
        pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.pikkus))

    def hit(self, kuul):
        self.health -= kuul.dmg
        if self.health <= 0:
            for ugu in range(randint(3,6)):
                vars()["r"+str(len(maailm.rahad))] = Raha(self.x,self.y,choice([-1,1]),5/randint(1,10),4/randint(1,10),self.y+self.pikkus)
                maailm.rahad.append(vars()["r"+str(len(maailm.rahad))])
            self.elus = False
            vastane_surm.play()
            maailm.vastased.remove(self)

class Zombie(Vastane):
    def __init__(self, x, y, laius, pikkus, vel, health, värv, path):
        Vastane.__init__(self, x, y, laius, pikkus, vel, health, värv)
        self.path = [self.x, path + self.x - self.laius]
        
    def move(self, dt, Tom):
        if self.vel > 0:
            if self.vel + self.x < self.path[1]:
                self.x += self.vel*dt
            else:
                self.vel = -self.vel*dt
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel*dt
            else:
                self.vel = -self.vel*dt
    
class Jälitaja(Vastane):
    def __init__(self, x, y, laius, pikkus, vel, health, värv):
        Vastane.__init__(self, x, y, laius, pikkus, vel, health, värv)
        self.jälitab = False
        self.tagane = False
        self.nägemiskaugus = 300
        self.oota = 30*5
        self.xspawn = x
        self.yspawn = self.y
        
    def move(self, dt, Tom):
        #märkab tomi
        if abs((self.x+self.laius/2) - (Tom.x+Tom.laius/2)) < self.nägemiskaugus and -30 < (self.y - Tom.y + self.pikkus - Tom.pikkus) <= 0 and not self.tagane:
            self.jälitab = True
            self.tagane = False
        if self.jälitab:
            #lõpetab jälitamise
            if abs((self.x+self.laius/2) - (Tom.x+Tom.laius/2)) >= self.nägemiskaugus or not(-30 < (self.y - Tom.y + self.pikkus - Tom.pikkus) <= 0) and not Tom.jump: #and self.seisab:
                self.jälitab = False
                self.oota = 30*5
        #jälitab
        if self.jälitab:
            if Tom.x > self.x+self.laius/2:
                if maailm.pole_sein_p(dt, self.vel,self.x,self.y,self.laius,self.pikkus):
                    self.x += self.vel*dt
                    #self.seisab = False
            elif maailm.pole_sein_v(dt, self.vel,self.x,self.y,self.laius,self.pikkus):
                self.x -= self.vel*dt
                #self.seisab = False
            else:
                self.seisab = True
        #ei jälita
        else:
            #ootab
            if self.oota < 0:
                self.tagane = True
            else:
                self.oota -= 1
            #taganeb
            if self.tagane:
                if self.x > self.xspawn:
                    self.x -= self.vel*dt
                elif self.x < self.xspawn:
                    self.x += self.vel*dt
                else:
                    self.tagane = False

class Lind(Vastane):
    def __init__(self):
        Vastane.__init__(self)
    
class Vampiir(Vastane):
    def __init__(self, x, y, laius, pikkus, vel, health, värv):
        Vastane.__init__(self)
    
class Preester(Vastane):
    def __init__(self):
        Vastane.__init__(self)
    
class Boss(Vastane):
    def __init__(self):
        Vastane.__init__(self)