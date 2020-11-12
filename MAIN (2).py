import pygame as pg
import sys
from random import randint
from random import choice
import os

dirr = os.path.dirname(os.path.abspath(__file__))
#print(dirr)
global helidir
helidir = dirr+"\helid"
print(helidir)

pg.init()


laius = 1280
kõrgus = 720
aken = pg.display.set_mode((laius, kõrgus))
pg.display.set_caption('D-day')
pg.display.flip()

global nupp_hover
nupp_hover = pg.mixer.Sound(helidir+"\click_h.wav")
global nupp_klikk
nupp_klikk = pg.mixer.Sound(helidir+"\click.wav")

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

hiir_all = False
def nupp(text, x, y, laius, kõrgus, värv_tuhm, värv_hele, action=None):
    global hiir_all
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
        
    if x + laius > mouse[0] > x and y + kõrgus > mouse[1] > y:
        pg.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
        pg.draw.rect(aken, värv_hele, (x-5, y-5, laius, kõrgus))
        hiir_vabastatud = False
        if hiir_all and not click[0]:
            hiir_vabastatud = True
        hiir_all = click[0]
        if hiir_vabastatud:
            nupp_klikk.play()
            action()

    else:
        pg.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x+x+laius)//2, (y+y+kõrgus)//2)
    aken.blit(textSurf, textRect)

def intro():
    
    #Teksdi suurused
    global largeText
    largeText = pg.font.Font("RL.ttf", 150)
    global mediumText
    mediumText = pg.font.Font("RM.ttf", 70)
    global smallText
    smallText = pg.font.Font("RM.ttf", 22)
    global veneText
    veneText = pg.font.SysFont("MIROSLN.ttf", 36)

    intro = True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        aken.fill((119,81,87))
         
        TextSurf, TextRect = text_objects("D-day", largeText)
        TextRect.center = ((laius // 2), (170))
        aken.blit(TextSurf, TextRect)
        
        nupp("Minek!",laius/2-100, 300, 200, 100, (155,114,98), (185,144,128), main_loop)
        nupp("Vali oma sõdalane!", laius/2-100, 425, 200, 100, (72,58,78), (102,88,108), vali_sõdalane)
        nupp("Annan alla...", laius/2-100, 550, 200, 100, (42,42,50), (72,72,89), quit)
        
        pg.display.update()
        
def vali_sõdalane():
    global valin_sõdalane
    valin_sõdalane = True
    while valin_sõdalane:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        aken.fill((70,70,70))
        TextSurf, TextRect = text_objects("Vali oma sõdalane!", largeText)
        TextRect.center = ((laius // 2), (100))
        aken.blit(TextSurf, TextRect)
    
        
        nupp("Valik tehtud!", laius/2-100 , 600, 200, 100, (100,100,0), (255,255,0), sõdalane_valitud)
        #Relva valik
        nupp("Tahan olla kuninglik!", 170, 300, 200, 100, (113,16,15), (163,66,65), esimene_sõdalane)
        nupp("Tahan olla camo!", 540, 300, 200, 100, (112,130,56), (162,180,106), teine_sõdalane)
        nupp("Vidi vini vici", 910 , 300, 200, 100, (80,5,94), (130,55,144), kolmas_sõdalane)
        
        pg.display.update()
        
kangelane_värv = (113,16,15)        
def sõdalane_valitud():
    global valin_sõdalane
    valin_sõdalane = False
    
def esimene_sõdalane():
    global kangelane_värv
    kangelane_värv = (113,16,15)    
        
def teine_sõdalane():
    global kangelane_värv
    kangelane_värv = (112,130,56)

def kolmas_sõdalane():
    global kangelane_värv
    kangelane_värv = (80,5,94)
    
def pood():
    global Tom
    global hernepüss
    global poes
    poes = True
    while poes:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        aken.fill((70,70,70))
        TextSurf, TextRect = text_objects("Mida teile?", largeText)
        TextRect.center = ((laius // 2), (100))
        aken.blit(TextSurf, TextRect)
        #Registreerime kus on kursor
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
                    
        nupp("Ostud tehtud!", laius/2-100 , 600, 200, 100, (100,100,0), (255,255,0), pood_done)
        #Relva valik
        nupp("Jõujooki!", 170, 300, 200, 100, (113,16,15), (163,66,65), jõujook_ost)
        nupp("Hernepüssi!", 540, 300, 200, 100, (112,130,56), (162,180,106), hernepüss_ost)
        nupp("Ritaliini!", 910 , 300, 200, 100, (80,5,94), (130,55,144), ritaliin_ost)
        
        raha = veneText.render(str(Tom.raha)+" рубль", False, (255,215,0))
        aken.blit(raha, (laius-100, 20))
        
        pg.display.update()
        
kangelane_värv = (113,16,15)

def pood_done():
    global poes
    poes = False
    
def jõujook_ost():
    if Tom.raha >= 1 and Tom.health < Tom.max_health:
        Tom.raha -= 1
        Tom.health += 1
        
def hernepüss_ost():
    if Tom.raha >= 5 and not hernepüss.unlocked:
        hernepüss.unlocked = True
        Tom.raha -= 5
        
def ritaliin_ost():
    if Tom.raha >= 1 and Tom.vel <= 20:
        Tom.vel *= 1.5
        Tom.raha -= 1

def main_loop():
    global Tom
    global hernepüss
    global pause
    
    class Player:
        def __init__(self, x, y, laius, pikkus):
            self.x = x
            self.y = y
            self.laius = laius
            self.pikkus = pikkus
            self.värv = kangelane_värv
            self.vaatab = 1
            self.hitbox = (self.x-1, self.y-1, self.laius+2, self.pikkus+2)
            self.jump = False
            self.kukub = True
            self.m = 1
            self.vel = 10
            self.vh = 10 #hüppe vel
            self.health = 10
            self.max_health = 10
            self.kb = 0 #knockback 1-paremale -1-vasakule 0-false
            self.kontr = True #kas saab kontrollida
            self.elus = True
            self.elud_värv = (0,255,0)
            self.raha = 0
        
        def hit(self):
            if self.health >= self.max_health * 0.8:
                self.elud_värv = (0,255,0)
            elif self.health >= self.max_health * 0.6:
                self.elud_värv = (200,200,0)
            elif self.health >= self.max_health * 0.4:
                self.elud_värv = (255,100,0)
            else:
                self.elud_värv = (255,50,0)
                
            if self.health > 1:
                self.health -= 1
                self.x -= 20
            else:
                self.elus = False
                surm()
            
        def draw(self, aken):
            #elud
            pg.draw.rect(aken, (50,50,50),(self.x, self.y-15, self.laius, 10))
            pg.draw.rect(aken, self.elud_värv,(self.x, self.y-15, self.health * (self.laius / self.max_health) , 10))
            #player
            self.hitbox = (self.x-1, self.y-1, self.laius+2, self.pikkus+2)
            pg.draw.rect(aken, (255,0,0), self.hitbox, 1)
            pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.pikkus))
            #raha
            raha = veneText.render(str(self.raha)+" рубль", False, (255,215,0))
            aken.blit(raha, (laius-100, 20))
            
    class Kuul:
        def __init__(self, x, y, suund):
            self.x = x
            self.y = y
            self.raadius = Relvad.instance.r
            self.värv = Relvad.instance.värv
            self.vel = Relvad.instance.vel * suund
            
        def draw(self, aken):
            pg.draw.circle(aken, self.värv, (self.x , self.y), self.raadius)

    class raha:
        raha_maas = 0
        instances = []
        def __init__(self,x,y,v,suund,xoff):
            self.__class__.instances.append(self)
            self.x = x
            self.y = y
            self.v = v
            self.suund = suund
            self.xoff = xoff
            self.kukkumas = True
        
        def kukub(self):
            self.y += 0.5*(self.v**2)*dt
            self.x += self.xoff 
            self.v -= 1
            if self.y >= mk:
                self.y = mk
                self.kukkumas = False
        
        def draw(self, aken):
            pg.draw.circle(aken, (255,215,0), (self.x , self.y), 5)

    class Vastane:
        instances = []
        def __init__(self, x, y, lõpp, vel, health, jälitaja):
            self.__class__.instances.append(self)
            self.x = x
            self.y = y
            self.xspawn = x
            self.yspawn = y
            self.lõpp = lõpp
            self.path = [self.x, self.lõpp]
            self.vel = vel
            self.laius = 20
            self.pikkus = 60
            self.värv = (0, 255, 255)
            self.hitbox = (self.x -1, self.y -1, self.laius+2, self.pikkus+2)
            self.health = health
            self.max_health = health
            self.elus = True
            self.elud_värv = (0,255,0)
            self.jälitaja = jälitaja #choice([True,False])
            self.jälitab = False
            self.tagane = False
            self.nägemiskaugus = 270
            self.oota = 30*5
            #self.seisab = False
            
        def move(self):
            if self.jälitaja:
                #märkab tomi
                if abs(self.x+self.laius/2) - abs(Tom.x+Tom.laius/2) < self.nägemiskaugus and self.y == Tom.y and not self.tagane:
                    self.jälitab = True
                    self.tagane = False
                if self.jälitab:
                    #lõpetab jälitamise
                    if not abs(self.x+self.laius/2) - abs(Tom.x+Tom.laius/2) < self.nägemiskaugus or self.y and self.y != Tom.y: #and self.seisab:
                        self.jälitab = False
                        self.oota = 30*5
                #jälitab
                if self.jälitab:
                    if Tom.x+Tom.laius/2 > self.x+self.laius/2:
                        if pole_sein_p(self.vel,self.x,self.y,self.laius,self.pikkus):
                            self.x += self.vel*dt
                            #self.seisab = False
                    elif pole_sein_v(self.vel,self.x,self.y,self.laius,self.pikkus):
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
            
            else:
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
                    
        def draw(self, aken):
            if self.health >= self.max_health * 0.8:
                self.elud_värv = (0,255,0)
            elif self.health >= self.max_health * 0.6:
                self.elud_värv = (200,200,0)
            elif self.health >= self.max_health * 0.4:
                self.elud_värv = (255,100,0)
            else:
                self.elud_värv = (255,50,0)
                
            if self.elus:
                self.move()
                pg.draw.rect(aken, (50,50,50),(self.x, self.y-15, self.laius, 10))
                pg.draw.rect(aken, self.elud_värv ,(self.x, self.y-15, self.health * (self.laius // self.max_health), 10))
                self.hitbox = (self.x -1, self.y -1, self.laius+2, self.pikkus+2)             
                pg.draw.rect(aken, (255,0,0), self.hitbox, 1)
                pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.pikkus))

        def hit(self):
            self.health -= Relvad.instance.dmg
            if self.health <= 0:
                for ugu in range(randint(3,6)):
                    vars()["r"+str(raha.raha_maas)] = raha(self.x,self.y,choice([-1,1]),5/randint(1,10),4/randint(1,10))
                    raha.raha_maas += 1
                self.elus = False
                vastane_surm.play()
                self.instances.remove(self)
            
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
            
    class Relvad:
        instance = None
        
        def __init__(self, dmg, cd, r, värv, vel, equipped, unlocked):
            self.dmg = dmg
            self.cd = cd
            self.r = r
            self.värv = värv
            self.vel = vel
            self.unlocked = unlocked
            
        def equip(self):
            if self.unlocked:
                Relvad.instance = self
                
    
    def unpause():
        global pause
        global start
        pause = False
        pos = pg.mixer.music.get_pos()
        pg.mixer.music.stop()
        pg.mixer.music.load(helidir+"\game.mp3")
        start = start + pos/1000.0
        pg.mixer.music.play(-1, start)
    
    def paused():
        
        while pause:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                    
            aken.fill((70,70,70))
            TextSurf, TextRect = text_objects("Tõmban hinge", largeText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            
            keys = pg.key.get_pressed()
      
            if keys [pg.K_i]:
                inventory()
            
        
            nupp("Jätkan!", 170, 300, 200, 100, (0,100,0), (0,255,0), unpause)
            nupp("Annan alla", 540, 300, 200, 100, (100,100,0), (255,255,0), quit)
            nupp("Varustuse juurde", 910, 300, 200, 100, (0,100,0), (0,255,0), inventory)
            nupp("Konsum", 540, 450, 200, 100, (0,100,0), (0,255,0), pood)
            
            pg.display.update()
    
    def redrawGameWindow():
        aken.fill((0,0,0))

        for prr in põrand.instances:
            prr.draw(aken)

        Tom.draw(aken)
        for p1 in Vastane.instances:
            p1.draw(aken)
        
        for rah in raha.instances:
            rah.draw(aken)
        for kuul in kuulid:
            kuul.draw(aken)
        
        pg.display.update()
        dt = clock.tick(30)
    
    def pole_sein_v(v,x,y,lai,pikk,umb=0,obj=põrand):
        #seinad vasakule minnes
        for i in obj.instances:
            if x <= i.x2+(v*dt)+umb and x > i.x2 + 1-umb and not y < i.y - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                return False
        return True
        
    def pole_sein_p(v,x,y,lai,pikk,umb=0,obj=põrand):
        #seinad paremale minnes
        for i in obj.instances:
            if x+lai+(v*dt) >= i.x1 and x+lai < i.x1 + 1 and not y < i.y - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                return False
            return True

    def maa_kõrgus(px,lai,obj=põrand):
        global mk
        eelm_mk = mk
        y = []
        for i in obj.instances:
            if px >= i.x1-lai and px <= i.x2:
                #print(i.x1)
                #print(px+lai)
                #print(px)
                #print(i.x2)
                y.append(i.y)

        if not y:
            mk = eelm_mk
        else:
            mk = (min(y))

    def põrkub(e,t):
        #kui vastane (s) läheb sulle (t) pihta saad knockback ja kaotad elud
        if t.kb == 0: #knockbacki ajal surematu
            if t.x+t.laius+(t.vel*dt) >= e.x and t.x+t.laius < e.x + e.laius/2 and not t.y < e.y - t.pikkus:
                Tom.kb = 1
                Tom.kontr = False
                Tom.hit()
                valu.play()
                return e.vel
            elif t.x <= e.x+e.laius+(t.vel*dt) and t.x > e.x+e.laius/2 and not t.y < e.y - t.pikkus:
                Tom.kb = -1
                Tom.kontr = False
                Tom.hit()
                valu.play()
                return e.vel
            else:
                Tom.kb = 0
                return t.vh

    def surm():
        psurm.play()
        pg.mixer.music.stop()
        surm = True
        while surm:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            aken.fill((70,70,70))
            
            TextSurf, TextRect = text_objects("Hummid tampisid su ära...", largeText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            
            nupp("Annan alla", 400, 375, 200, 100, (100,0,0), (255,0,0), intro)
            nupp("Proovin uuesti", 400, 250, 200, 100, (0,100,0), (0,255,0), main_loop)
            
            pg.display.update()

    def võit():
        if len(Vastane.instances) == 0 and raha.raha_maas == 0:
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                        
                aken.fill((70,70,70))
                TextSurf, TextRect = text_objects("Sa said hakkama!", largeText)
                TextRect.center = ((laius // 2), (170))
                aken.blit(TextSurf, TextRect)
                
            
                
                nupp("Aitab kah...", laius/2-100 , 500 , 200, 100, (100,100,0), (255,255,0), intro)
                
                pg.display.update()
                
    def inventory():
        global inventory_tab
        inventory_tab = True
        while inventory_tab:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                    
            aken.fill((70,70,70))
            TextSurf, TextRect = text_objects("Vali oma varustus", largeText)
            TextRect.center = ((laius // 2), (100))
            aken.blit(TextSurf, TextRect)
            
        
            
            nupp("Olen valmis naasma!", laius/2-100 , 600, 200, 100, (100,100,0), (255,255,0), invent_stop)
            #Relva valik
            nupp("lingu viskama!", 170, 300, 200, 100, (100,100,100), (200,200,200), ling_equip)
            nupp("Ma leidsin hernepüssi!", 540, 300, 200, 100, (100,100,100), (200,200,200), hernepüss_equip)
            nupp("Ohh kartulikahur!", 910 , 300, 200, 100, (100,100,100), (200,200,200), kartulikahur_equip)
            nupp("Tulevik in nüüd, vanamees!", 540, 450, 200, 100, (100, 100, 100), (200, 200, 200), railgun_equip)
            
            pg.display.update()
            
    def invent_stop():
        global inventory_tab
        inventory_tab = False
        
    def ling_equip():
        ling.equip()
        
    def hernepüss_equip():
        hernepüss.equip()
    
    def kartulikahur_equip():
        kartulikahur.equip()
        
    def railgun_equip():
        railgun.equip()
        

    #VARS ja objektid
    if True: #et saaks collapsida
        #OBJEKTID
        #level layout
        põrand1 = põrand(0,laius,500)#(0,600,500)
        global screen
        screen = 0
        global screenid
        screenid = {
        -1:["põrand(750+400,800+400,250)"],
        0:["põrand(750+400,800+400,250)","põrand(100,200,400)","põrand(700,850,400)"],
        1:["põrand(10+400,800+400,250)","põrand(100,400,400)","põrand(700,720,600)"]
        }
        #uued platformide objektid
        for o in range(len(screenid[screen])):
            exec("plat"+str(o)+" = "+screenid[screen][o])
        
        #Tomi asjad
        Tom = Player(580, 100, 40, 60)
        vh = Tom.vh
        Tom.vh = 0
        #Kuulid
        #kuul = None #Kuul(laius + Tom.x // 2, kõrgus + Tom.y // 2, Tom.vaatab)
        #Pahad
        paha = Vastane(400, 0, 500, 5, 10,True)
        paha.y = põrand1.y-paha.pikkus
        paha1 = Vastane(100, 0, 400, 15, 2,False)
        paha1.y = põrand1.y-paha1.pikkus
        #Relvad
        ling = Relvad(2, 30, 5, (255,255,255), 15, 1, True)
        hernepüss = Relvad(1, 5, 3, (0,255,0), 20, 0, False)
        kartulikahur = Relvad(20, 40, 10, (161,127,27), 13, 0, True)
        railgun = Relvad(0.2, 0, 20, (4,217,255),10 , 0, True)
        #Et mängjal oleks alguses relv
        ling.equip()

        #vars
        kuulid = []
        kuulide_cd = 0
        kuulide_maxcount = 500

        pause = False
        running = True
        clock = pg.time.Clock()
        global dt
        dt = 1
        global mk #maa kõrgus (suurem arv = madalam kõrgus)
        mk = 500
        global eelmine_mk
        eelmine_mk = 500
    
    #sound vars, hiljem eraldi class vms
    if True:
        pg.mixer.music.load(helidir+"\game.mp3")
        pg.mixer.music.play(-1)
        pos = 0
        global start
        start = 0

        vastane_valu = pg.mixer.Sound(helidir+"\Zhurt.mp3")
        vastane_valu2 = pg.mixer.Sound(helidir+"\Zhurt1.mp3")
        vastane_surm = pg.mixer.Sound(helidir+"\Zdeath.mp3")
        valu = pg.mixer.Sound(helidir+"\hurt.mp3")
        psurm = pg.mixer.Sound(helidir+"\death.mp3")
        shoot = pg.mixer.Sound(helidir+"\shoot.mp3")
        whit = pg.mixer.Sound(helidir+"\hit.mp3")
        hop = pg.mixer.Sound(helidir+"\hop.mp3")
        hop2 = pg.mixer.Sound(helidir+"\hop1.mp3")
        pg.mixer.Sound.set_volume(shoot,0.4)
        pg.mixer.Sound.set_volume(whit,0.4)
        raha_pickup = pg.mixer.Sound(helidir+"\gold_pickup.mp3")
        raha_drop = pg.mixer.Sound(helidir+"\gold_drop.mp3")

    while running:
        
        #exit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        #KUULID
        if True: #lihtsalt et saaks collapsida seda
            if kuulide_cd > 0:
                kuulide_cd += 1
            if kuulide_cd > Relvad.instance.cd:
                kuulide_cd = 0
            for kuul in kuulid:
                #Pahade tulistamine
                for p in Vastane.instances:
                    if kuul.y - kuul.raadius < p.hitbox[1] + p.hitbox[3] and kuul.y + kuul.raadius > p.hitbox[1] and p.elus:
                        if kuul.x - kuul.raadius < p.hitbox[0] + p.hitbox[2] and kuul.x + kuul.raadius > p.hitbox[0]:
                            kuulid.pop(kuulid.index(kuul))
                            p.hit() 
                            if randint(0,2):
                                vastane_valu.play()
                            else:
                                vastane_valu2.play()

                #sein
                if not pole_sein_v(kuul.vel,kuul.x,kuul.y,0,0,5):
                    if kuul in kuulid:
                        kuulid.pop(kuulid.index(kuul))
                        whit.play()
                if not pole_sein_p(kuul.vel,kuul.x,kuul.y,0,0,5):
                    if kuul in kuulid:
                        kuulid.pop(kuulid.index(kuul))
                        whit.play()
                #liikumine
                if kuul.x < Tom.x + 500 and kuul.x > Tom.x - 500:
                    kuul.x += kuul.vel*dt  # Moves the kuul by its vel
                else:
                    if kuul in kuulid:
                        kuulid.pop(kuulid.index(kuul))
        
        keys = pg.key.get_pressed()
        
        eelmine_mk = mk
        maa_kõrgus(Tom.x,Tom.laius)
        
        if mk <= Tom.y + Tom.pikkus:
            Tom.y = mk-Tom.pikkus

        if Tom.kontr:
            # TOM PAREMALE JA VASAKULE      
            if keys [pg.K_d] and pole_sein_p(Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
                Tom.x += Tom.vel*dt
                Tom.vaatab = 1
            if keys [pg.K_a] and pole_sein_v(Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
                Tom.x -= Tom.vel*dt
                Tom.vaatab = -1
            
            # TOM HÜPPAMINE
            if not Tom.jump:
                if keys [pg.K_w]:
                    if randint(0,2):
                        hop.play()
                    else:
                        hop2.play()
                    Tom.jump = True
            if Tom.jump:
                #F = 1 / 2 * mass * velocity ^ 2
                if Tom.vh > 0:
                    F = (0.5*Tom.m*(Tom.vh**2)) #/2
                else:
                    F = -(0.5*Tom.m*(Tom.vh**2)) #/2
                
                Tom.y -= F*dt

                Tom.vh -= 1 
                
                if Tom.y+Tom.pikkus >= mk:
                    Tom.y = mk-Tom.pikkus
                    Tom.jump = False
                    Tom.vh = vh
        
        #tom kukkumine
        if mk > eelmine_mk and not Tom.jump:
            Tom.kukub = True
            Tom.vh = 0
        if Tom.kukub:
            F = 0.5*Tom.m*(Tom.vh**2) #/2
            Tom.y += F*dt
            Tom.vh -= 1
            if Tom.y+Tom.pikkus >= mk:
                Tom.y = mk-Tom.pikkus
                Tom.kukub = False
                Tom.vh = vh
        
        #TOM SAAB PIHTA
        for kuri in Vastane.instances:
            lükkaja_v = põrkub(kuri,Tom)
        #if lükkaja_v < 0:  #lükkaja mõte oli knockback teha vastavaks vastase velocytiga aga see läks segaseks ja ei töötand
        #    lükkaja_v = -lükkaja_v
        lükkaja_v = Tom.vh
        #knockback
        if Tom.kb != 0:
            Tom.värv = (255, 0, 0)
            if Tom.vh > 0:
                F = (0.5*Tom.m*(lükkaja_v**2)) #/2
                #if pole_sein_p(Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus) and pole_sein_v(Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus): ÜRITUS FIXIDA SEDA KINNI JÄÄMIST KNOCKBACKIS
                Tom.x -= (F*dt*Tom.kb)/3
            else:
                F = -(0.5*Tom.m*(Tom.vh**2)) #/2
                Tom.kontr = True
            
            Tom.y -= (F*dt)/2
            
            Tom.vh -= 1
            lükkaja_v -= 1
            if Tom.y+Tom.pikkus >= mk:
                Tom.y = mk-Tom.pikkus
                Tom.kb = 0
                Tom.vh = vh
                Tom.värv = (0, 255, 0)

        #TULISTAMINE
        if keys[pg.K_SPACE] and kuulide_cd == 0:
            shoot.play()
            if Tom.vaatab == 1:
                suund = 1
            else:
                suund = -1

            if len(kuulid) < kuulide_maxcount:  # This will make sure we cannot exceed 5 bullets on the screen at once
                kuulid.append(Kuul(round(Tom.x+Tom.laius//2+suund*Tom.laius/2), round(Tom.y + Tom.pikkus//2), suund))
            
            kuulide_cd = 1
        
        #RAHA
        for ir in raha.instances:
            if ir.kukkumas:
                raha_drop.play()
                ir.kukub()
            if Tom.x+Tom.laius >= ir.x and Tom.x <= ir.x and Tom.y+Tom.pikkus > ir.y-3:
                ir.instances.remove(ir)
                raha_pickup.play()
                raha.raha_maas -= 1
                Tom.raha += 1
        
        #vaheta screeni paremale
        if Tom.x+Tom.laius/2 > laius:
            #tom spawn
            Tom.x = 0-Tom.laius/2
            #kustuta eelmised
            for rii in põrand.instances:
                rii.instances.remove(rii)
            #kuhu poole
            screen += 1
            #uued platformide objektid
            põrand1 = põrand(0,laius,500)
            for o in range(len(screenid[screen])):
                exec("plat"+str(o)+" = "+screenid[screen][o])
            #vaenlased liigutada
            for vaenlane in Vastane.instances:
                vaenlane.x -= laius
            #uued vaenlased
            #veel implementimata
        #vaheta screeni vasakule
        if Tom.x+Tom.laius/2 < 0:
            #tom spawn
            Tom.x = laius-Tom.laius/2
            #kustuta eelmised platvormid
            for rii in põrand.instances:
                rii.instances.remove(rii)
            #kuhu poole
            screen -= 1
            #uued platformide objektid
            põrand1 = põrand(0,laius,500)
            for o in range(len(screenid[screen])):
                exec("plat"+str(o)+" = "+screenid[screen][o])
            #vaenlased liigutada
            for vaenlane in Vastane.instances:
                vaenlane.x += laius
            #uued vaenlased
            #veel implementimata


        #PAUSE MENU
        if keys[pg.K_p]:
            pause = True
            pos = pg.mixer.music.get_pos()
            pg.mixer.music.stop()
            pg.mixer.music.load(helidir+"\game_filt.mp3")
            start = start + pos/1000.0
            pg.mixer.music.play(-1, start)
            paused()
                
        võit()  
        redrawGameWindow()


while True:
    intro()
    main_loop()