import pygame as pg
from random import randint
from random import choice
import maailm
#from ekraanid import screenide_loomine
from player_lisad import *
from math import *

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
            mkrr = kõrgus
            for p in maailm.põrandad:
                if p.x1 < self.x+self.laius and p.x2 > self.x and p.y1 >= self.y+self.pikkus and p.y1 < mkrr:
                    mkrr = p.y1
            if mkrr == kõrgus: #SIIA PANNA ET KUKUB JÄRGMISESSE SCREENI. Praefu läheb automaatselt mängijale 3 raha kui sel screenil raha dropi all pole ühtegi platvormi
                raha_pickup.play()
                maailm.Tom.raha += 3
            else:
                for ugu in range(self.raha):
                    maailm.rahad.append(Raha(self.x,self.y,choice([-1,1]),5/randint(1,10),4/randint(1,10),mkrr))
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
        self.nägemiskaugus = 500
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
        self.vel_debuff = 50
        
    def player_siseneb(self, Tom):
        self.vel_debuff = 50

    def player_väljub(self, Tom):
        self.debuff_off(Tom)

        
    def debuff_off(self, Tom):
        Tom.vel_debuff = 50
        if self.dbkontroll:
            self.dbkontroll = False
            Tom.armor = Tom.armor / self.armordb
            maailm.ling.dmg += self.dmgdb
            maailm.hernepüss.dmg += self.dmgdb
            maailm.kartulikahur.dmg += self.dmgdb
            maailm.railgun.dmg += self.dmgdb
            maailm.kiiver.armor /= self.armordb
            maailm.kasukas.armor /= self.armordb
            maailm.püksid.armor /= self.armordb
            maailm.sandaalid.armor /= self.armordb

    def debuff_on(self, Tom):
        Tom.vel_debuff = 50
        if not self.dbkontroll:
            Tom.vel *= -1
            self.dbkontroll = True
            Tom.armor *= self.armordb
            maailm.ling.dmg -= self.dmgdb
            maailm.hernepüss.dmg -= self.dmgdb
            maailm.kartulikahur.dmg -= self.dmgdb
            maailm.railgun.dmg -= self.dmgdb
            maailm.kiiver.armor *= self.armordb
            maailm.kasukas.armor *= self.armordb
            maailm.püksid.armor *= self.armordb
            maailm.sandaalid.armor *= self.armordb

    
    def move(self, dt, Tom):
        if not self.y_c > self.y > self.y_c - 30:
            self.vel *= -1
        self.y += self.vel

        if self.vel_debuff > 0:
            self.vel_debuff -= 1
        if self.vel_debuff == 0:
            self.debuff_on(Tom)
    
class Boss(Vastane):
    def __init__(self, x, y, laius, pikkus, health, dmg, vel):
        Vastane.__init__(self, x, y, laius, pikkus, health, dmg, vel)
        self.state = 0
        self.x_c = x
        self.y_c = y
        self.l_c = laius
        self.p_c = pikkus
        self.vihane = False
        self.rage = False
        self.paremal = False
        self.vel_hingamine = vel
        self.vel_x = vel
        self.vel_y = vel
        self.kuulide_vel_c = vel * 2
        self.lendab_aeg = 0
        self.tomi_kohal = False
        self.health_rg = 0.1
        self.sound = False
        self.vihane_buff = True
        self.rage_buff = True

    PUHKAB = 0
    TULISTAB = 1
    JOOKSEB = 2
    LENDAB = 3


    def move(self, dt, Tom):
        if self.max_health * 0.7 < self.health:
            self.värv = (200,100,0)
            self.vihane = False
            self.rage = False
        if self.max_health * 0.4 < self.health < self.max_health * 0.7 and not self.vihane:
            self.vihane = True
            self.rage = False
            if self.vihane_buff:
                self.vihane_buff = False
                self.vel_hingamine *= 5
                self.vel *= 2
                self.vel_x *= 1.5
                self.vel_y *= 1.5
                self.värv = (200, 0, 0)
        if self.health < self.max_health * 0.4 and not self.rage:
            self.vihane = False
            self.rage = True
            if self.rage_buff:
                self.rage_buff = False
                self.vel_hingamine *= 2
                self.vel *= 2
                self.vel_x *= 2
                self.vel_y *= 2
                self.värv = (0, 0, 0)
                Boss_rage.play()

        if self.state == Boss.PUHKAB:
            self.sound = True
            if self.health < self.max_health:
                self.health += self.health_rg
            puhkamine_done = randint(0, 100)
            if 70 < puhkamine_done < 75:
                self.state = Boss.JOOKSEB
            if 90 < puhkamine_done < 100:
                self.state = Boss.TULISTAB
            if 80 < puhkamine_done < 85:
                self.state = Boss.LENDAB
            aeg = pg.time.get_ticks() * 0.005
            self.pikkus = sin(aeg) * self.vel_hingamine + self.p_c
            self.y = self.y_c - self.pikkus

        elif self.state == Boss.TULISTAB:
            if self.sound:
                Boss_tulistab.play()
                self.sound = False
            if self.paremal:
                kuulide_vel = self.kuulide_vel_c * -1
            else:
                kuulide_vel = self.kuulide_vel_c
            kogus = randint(1, 6)
            crit = randint(0, 10)
            if crit == 10:
                for i in range(kogus):
                    y = randint(self.y_c - self.p_c, self.y_c + round(self.pikkus))
                    maailm.vastased.append(KuulBoss(self.x, y, 10, 120, kuulide_vel + 5, (0,255,0)))
            else:
                for i in range(kogus):
                    y = randint(self.y_c - self.p_c, self.y_c)
                    maailm.vastased.append(KuulBoss(self.x, y, 7, 40, kuulide_vel, (200,0,0)))
            self.state = Boss.PUHKAB

        elif self.state == Boss.JOOKSEB:
            if self.sound:
                Boss_jookseb.play()
                self.sound = False
            if self.paremal:
                self.x -= self.vel
                if self.x + self.laius / 2 <= 100:
                    self.paremal = False
                    self.state = Boss.PUHKAB
            else:
                self.x += self.vel
                if self.x + self.laius / 2 >= 1200:
                    self.paremal = True
                    self.state = Boss.PUHKAB

        elif self.state == Boss.LENDAB:
            if self.sound:
                Boss_lendab.play()
                self.sound = False
            if self.x + self.laius < maailm.Tom.x + maailm.Tom.laius / 2 < self.x:
                print("kohal")
                self.tomi_kohal = True
            else:
                self.tomi_kohal = False
            if not self.tomi_kohal:
                if self.lendab_aeg < 150:
                    self.lendab_aeg += 1
                    self.x += self.vel_x
                    self.y += self.vel_y
                    if self.x + self.laius >= laius or self.x <= 0:
                        self.vel_x *= -1
                    if self.y + self.pikkus > 500 or self.y <= 0:
                        self.vel_y *= -1
            else:
                self.y += abs(self.vel_y)
            if self.lendab_aeg >= 150:
                self.y += abs(self.vel_y)
                if self.y + self.pikkus > 500:
                    self.lendab_aeg = 0
                    self.state = Boss.PUHKAB

    def player_väljub(self, Tom):
        if self.health <= 0:
            maailm.itemid.append(Võit(self.x, self.y))

    def hit(self, kuul):
        if kuul.dmg > 15:
            self.health -= 15
        else:
            self.health -= kuul.dmg
        if self.health >= self.max_health:
            self.health = self.max_health
        if self.health <= 0:
            self.elus = False
            vastane_surm.play()
            maailm.vastased.remove(self)
            self.player_väljub(maailm.Tom)

class KuulBoss():
    def __init__(self, x, y, raadius, dmg, vel, värv):
        self.x = x
        self.y = y
        self.raadius = raadius
        self.raadius2 = raadius * 0.6
        self.dmg = dmg
        self.vel = vel
        self.värv = värv
        self.värv2 = (200, 200, 0)
        self.elus = True
        self.pikkus = raadius
        self.laius = raadius
        self.hitbox = (0,0,0,0)

    def draw(self):
        pg.draw.circle(aken, self.värv, (self.x + self.raadius, self.y + self.raadius), self.raadius)
        pg.draw.circle(aken, self.värv2, (self.x + self.raadius, self.y + self.raadius), self.raadius2)

    def move(self, dt, Tom):
        self.x += self.vel
        if self.x > laius or self.x < 0:
            maailm.vastased.remove(self)

    def hit(self):
        pass

    def player_väljub(self,Tom):
        pass
    def player_siseneb(self,Tom):
        pass