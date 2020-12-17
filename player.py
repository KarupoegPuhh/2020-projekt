import pygame as pg
from abi import *

class Player:
    def __init__(self, x, y, laius, pikkus, relv):
        self.x = x
        self.y = y
        self.laius = laius
        self.pikkus = pikkus
        self.värv = Player.kangelane_värv
        self.vaatab = 1
        self.hitbox = (self.x-1, self.y-1, self.laius+2, self.pikkus+2)
        #self.jump = False
        #self.kukub = True
        self.m = 1
        self.vel = 10
        self.velx = 0
        self.vely = 0
        self.põrandal = False
        self.laes = False
        self.initial_vh = 10.5
        self.vh = 0 #hüppe vel
        self.health = 10
        self.max_health = 10
        self.kb = 0 #knockback 1-paremale -1-vasakule 0-false
        self.kontr = True #kas saab kontrollida
        self.elus = True
        self.elud_värv = (0,255,0)
        self.raha = 0
        self.armor = 1
        self.name = "nimi"
        self.relv = relv
        self.vel_debuff = 0
    
    kangelane_värv = (0,0,0)
    kangelane_nimi = "nimi"
    kangelane_pilt = None
    
    def hit(self, vastane):    
        if self.health > 0:
            self.health = round(self.health - vastane.dmg / self.armor, 2)
        if self.health <= 0:
            self.elus = False
        
    def draw(self):
        #elude update
        if self.health >= self.max_health * 0.8:
            self.elud_värv = (0,255,0)
        elif self.health >= self.max_health * 0.6:
            self.elud_värv = (200,200,0)
        elif self.health >= self.max_health * 0.4:
            self.elud_värv = (255,100,0)
        else:
            self.elud_värv = (255,50,0)
        #Elud muudab int kui täisarv
        if round(self.health, 3) % 1 == 0:
                self.health = int(self.health)
        #elud
        pg.draw.rect(aken, (50,50,50),(self.x, self.y-15, self.laius, 10))
        pg.draw.rect(aken, self.elud_värv,(self.x, self.y-15, self.health * (self.laius / self.max_health) , 10))
        #player
        self.hitbox = (self.x-1, self.y-1, self.laius+2, self.pikkus+2)
        pg.draw.rect(aken, (255,0,0), self.hitbox, 1)
        pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.pikkus))
        
    def põrkub(self, vastane, dt):
        #kui vastane (s) läheb sulle (t) pihta saad knockback ja kaotad elud
        if self.kb == 0 and self.y + self.pikkus > vastane.y and vastane.y + vastane.pikkus > self.y: #knockbacki ajal surematu
            if self.x + self.laius >= vastane.x and self.x <= vastane.x+vastane.laius:
                if self.x + self.laius/2 < vastane.x + vastane.laius/2:
                    self.kb = 1
                else:
                    self.kb = -1

                self.vh = self.initial_vh
                self.värv = (255, 0, 0)
                self.kontr = False
                self.hit(vastane)
                valu.play()
                #return vastane.vel
        
