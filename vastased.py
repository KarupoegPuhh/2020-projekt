import pygame as pg
from random import randint
from random import choice
import maailm
from player_lisad import *

class Vastane:
    def __init__(self, x, y, laius, pikkus, health, dmg, vel):
        self.laius = laius
        self.pikkus = pikkus
        self.x = x
        self.y = y - self.pikkus
        self.vel = vel
        self.värv = (150,150,150)
        self.hitbox = (self.x -1, self.y -1, self.laius+2, self.pikkus+2)
        self.health = health
        self.max_health = health
        self.elus = True
        self.elud_värv = (0,255,0)
        self.dmg = dmg
        self.raha = randint(3,6)
        
        #self.seisab = False
                    
    def draw(self):
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
        if self.health >= self.max_health:
            self.health = self.max_health
        if self.health <= 0:
            for ugu in range(self.raha):
                vars()["r"+str(len(maailm.rahad))] = Raha(self.x,self.y,choice([-1,1]),5/randint(1,10),4/randint(1,10),self.y+self.pikkus) #viimase argumendi peab ära muutma et raha õhku ei spawniks
                maailm.rahad.append(vars()["r"+str(len(maailm.rahad))])
            self.elus = False
            vastane_surm.play()
            maailm.vastased.remove(self)
            self.player_väljub(maailm.Tom)
            
    def player_siseneb(self, Tom):
        pass
    def player_väljub(self, Tom):
        pass

class Zombie(Vastane):
    def __init__(self, x, y, laius, pikkus,  health, dmg, vel,path):
        Vastane.__init__(self, x, y, laius, pikkus,  health, dmg, vel)
        self.path = [self.x, path + self.x - self.laius]
        self.värv = (27, 147, 25)
        
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
    def __init__(self, x, y, laius, pikkus, health, dmg, vel):
        Vastane.__init__(self, x, y, laius, pikkus, health, dmg, vel)
        self.jälitab = False
        self.tagane = False
        self.nägemiskaugus = 300
        self.oota = 30*5
        self.xspawn = x
        self.yspawn = self.y
        self.värv = (103,88,243)
        
    def move(self, dt, Tom):
        #märkab tomi
        if abs((self.x+self.laius/2) - (Tom.x+Tom.laius/2)) < self.nägemiskaugus and -30 < (self.y - Tom.y + self.pikkus - Tom.pikkus) <= 0 and not self.tagane:
            self.jälitab = True
            self.tagane = False
        if self.jälitab:
            #lõpetab jälitamise
            if abs((self.x+self.laius/2) - (Tom.x+Tom.laius/2)) >= self.nägemiskaugus or not(-30 < (self.y - Tom.y + self.pikkus - Tom.pikkus) <= 0) and Tom.põrandal: #and self.seisab:
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
    def __init__(self, x, y, laius, pikkus, health, dmg, vel, range, cd, path):
        Vastane.__init__(self, x, y, laius, pikkus, health, dmg, vel)
        self.range = range
        self.jälitab = False
        self.tagane = True
        self.oota = 30*5
        self.xspawn = x
        self.yspawn = self.y
        self.cooldown = 0
        self.cooldown_c = cd
        self.lõin = False
        self.xpath = x
        self.path = path
        self.suund = 1
        self.värv = (100,100,100)
        
    def move(self, dt, Tom):
        
        #märkab tomi
        if self.xspawn - self.range < Tom.x + Tom.laius/2 < self.xspawn + self.range:
            self.jälitab = True
            self.tagane = False
        if self.jälitab:
            #lõpetab jälitamise
            if self.xspawn - self.range > Tom.x + Tom.laius or Tom.x > self.xspawn + self.range:
                self.jälitab = False
                self.oota = 30
        #jälitab
        if self.jälitab:
            if Tom.x + Tom.laius/2 > self.x+self.laius/2 and self.cooldown == 0:
                if Tom.y >= self.y + self.pikkus / 2:
                    self.x += self.vel*dt
                    self.y += self.vel*dt
                else:
                    self.y -= self.vel*dt
                    self.x += self.vel*dt
                if Tom.kb != 0:
                    self.lõin = True
            elif Tom.x + Tom.laius/2 < self.x+self.laius/2 and self.cooldown == 0:
                if Tom.y >= self.y + self.pikkus / 2:
                    self.x -= self.vel*dt
                    self.y += self.vel*dt
                else:
                    self.y -= self.vel*dt
                    self.x -= self.vel*dt
                if Tom.kb != 0:
                    self.lõin = True
            if self.lõin:
                self.cooldown += 1
                self.y -= self.vel*dt
            if self.cooldown >= self.cooldown_c:
                self.cooldown = 0
                self.lõin = False
                
        #ei jälita
        else:
            self.xpath += self.vel * self.suund
            if not self.xspawn - self.path < self.xpath < self.xspawn + self.path:
                self.suund *= -1
            if self.y > self.yspawn:
                self.y -= self.vel*dt
            #ootab
            if self.oota < 0:
                self.tagane = True
            else:
                self.oota -= 1
            #taganeb
            if self.tagane:
                if self.x > self.xpath:
                    self.x -= self.vel*dt
                elif self.x < self.xpath:
                    self.x += self.vel*dt
                else:
                    self.tagane = False
        
    
class Vampiir(Zombie):
    def __init__(self, x, y, laius, pikkus, health, dmg, vel, path, health_regen):
        Zombie.__init__(self, x, y, laius, pikkus, health, dmg, vel, path)
        self.health_regen = health_regen
        self.värv = (200,0,0)
    def move(self, dt, Tom):
        if self.health < self.max_health:
            self.health += self.health_regen
        if self.health > self.max_health:
            self.health = self.max_health
        Zombie.move(self, dt, Tom)       
    
    
class Preester(Vastane):
    #db nagu debuff
    def __init__(self, x, y, laius, pikkus, health, dmg, vel, dmgdb, armordb):
        Vastane.__init__(self, x, y, laius, pikkus, health, dmg, vel)
        self.dmgdb = dmgdb
        self.armordb = armordb
        self.y_c = self.y
        self.dbkontroll = False
        self.värv = (200,200,0)
        
    def player_siseneb(self, Tom):
        pass
        
    def player_väljub(self, Tom):
        if self.dbkontroll:
            self.dbkontroll = False
            Tom.vel *= -1
            Tom.armor = Tom.armor / self.armordb
            maailm.ling.dmg += self.dmgdb
            maailm.hernepüss.dmg += self.dmgdb
            maailm.kartulikahur.dmg += self.dmgdb
            maailm.railgun.dmg += self.dmgdb
            maailm.kiiver.armor /= self.armordb
            maailm.kasukas.armor /= self.armordb
            maailm.püksid.armor /= self.armordb
            maailm.sandaalid.armor /= self.armordb
    
    def move(self, dt, Tom):
        if 200 < Tom.x + Tom.laius/2 < laius -200:
            if not self.dbkontroll:
                self.dbkontroll = True
                Tom.vel *= -1
                Tom.armor *= self.armordb
                maailm.ling.dmg -= self.dmgdb
                maailm.hernepüss.dmg -= self.dmgdb
                maailm.kartulikahur.dmg -= self.dmgdb
                maailm.railgun.dmg -= self.dmgdb
                maailm.kiiver.armor *= self.armordb
                maailm.kasukas.armor *= self.armordb
                maailm.püksid.armor *= self.armordb
                maailm.sandaalid.armor *= self.armordb
                
        if 100 > Tom.x + Tom.laius/2 or Tom.x + Tom.laius/2 > laius - 100:
            if self.dbkontroll:
                self.dbkontroll = False
                Tom.vel *= -1
                Tom.armor = Tom.armor / self.armordb
                maailm.ling.dmg += self.dmgdb
                maailm.hernepüss.dmg += self.dmgdb
                maailm.kartulikahur.dmg += self.dmgdb
                maailm.railgun.dmg += self.dmgdb
                maailm.kiiver.armor /= self.armordb
                maailm.kasukas.armor /= self.armordb
                maailm.püksid.armor /= self.armordb
                maailm.sandaalid.armor /= self.armordb
        
        if not self.y_c > self.y > self.y_c - 30:
            self.vel *= -1
        self.y += self.vel
    
class Boss(Vastane):
    def __init__(self):
        Vastane.__init__(self)