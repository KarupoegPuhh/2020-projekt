import maailm
from abi import *
from math import *

class Kuul:
    def __init__(self, x, y, suund, relv):
        self.x = x
        self.y = y
        self.raadius = relv.raadius
        self.värv = relv.värv
        self.vel = relv.vel * suund
        self.dmg = relv.dmg
        
    def draw(self):
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
        if self.y+5 >= self.mkr: #and pole_sein_p(self.v,self.x,self.y,3,3) and pole_sein_v(self.v,self.x,self.y,3,3): NAD SATUVAD SEINA SISSE VAHEST
            self.y = self.mkr-5
            self.kukkumas = False
    
    def draw(self):
        pg.draw.circle(aken, (255,215,0), (self.x , self.y), 5)
            
class Relvad:
    def __init__(self, dmg, cd, raadius, värv, vel, unlocked, nimi, nimi_data):
        self.dmg = dmg
        self.cd = cd
        self.raadius = raadius
        self.värv = värv
        self.vel = vel
        self.unlocked = unlocked
        self.nimi = nimi
        self.nimi_data = nimi_data
        
class Varustus:
    def __init__(self, speed, armor, equipped, unlocked, nimi):
        self.armor = armor
        self.speed = speed
        self.equipped = equipped
        self.unlocked = unlocked
        self.nimi = nimi
        
    def equip(self, Tom):
        if not self.equipped:
            self.equipped = True
            Tom.armor += self.armor
            if Tom.vel > 0:
                Tom.vel += self.speed
            else:
                Tom.vel -= self.speed
            
    def unequip(self, Tom):
        if self.equipped:
            self.equipped = False
            Tom.armor -= self.armor
            Tom.vel -= self.speed

class Item():
    def __init__(self, x, y, laius, kõrgus, asi, tekst, värv):
        self.x = x
        self.y = y - kõrgus
        self.laius = laius
        self.kõrgus = kõrgus
        self.asi = asi
        self.tekst = tekst
        self.collision = False
        self.aeg = 0
        self.värv = värv
    
    def draw(self):
        if not self.asi.unlocked:
            pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.kõrgus))
        if not self.asi.unlocked and self.collision:
            self.asi.unlocked = True
            self.aeg = pg.time.get_ticks()
        self.unlocked_sõnum()
        
    def unlocked_sõnum(self):
        aeg = pg.time.get_ticks()
        if self.asi.unlocked and self.aeg + 2000 >= aeg:
            TextSurf, TextRect = text_objects(self.tekst, largeText)
            TextRect.center = ((laius // 2), 170)
            aken.blit(TextSurf, TextRect)

nupp_all = False
class NPC():
    def __init__(self, x, y, laius, kõrgus, värv, tekst):
        self.x = x
        self.y = y - kõrgus
        self.laius = laius
        self.kõrgus = kõrgus
        self.värv = värv
        self.räägitud = False
        self.tekst = tekst
        self.page = 1
        self.i = 1

    def draw(self):
        pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.kõrgus))
        self.NPC_räägib()

    def NPC_räägib(self):
        pass


class NPC_inimene(NPC):
    def __init__(self, x, y, laius, kõrgus, värv, pic, tekst):
        NPC.__init__(self, x, y, laius, kõrgus, värv, tekst)
        self.pic = pic

    def NPC_räägib(self):
        global nupp_all
        if self.x + self.laius + 200 > (maailm.Tom.x + maailm.Tom.laius / 2) > self.x - 200 and self.y < maailm.Tom.y + maailm.Tom.pikkus / 2 < self.y + self.kõrgus:
            if self.page <= len(self.tekst) and self.räägitud == False:
                pg.draw.rect(aken, (50, 50, 50), (laius / 2 - 500, 0, 900, 220))
                TextSurf, TextRect = text_objects((self.tekst[self.page])[0:self.i], menu_head2Text,(255,255,255))
                TextRect.center = (laius / 2, 100)
                aken.blit(TextSurf, TextRect)
                self.i += 1
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    nupp_all = True
                if nupp_all == True and keys[pg.K_RETURN] == False:
                    self.page += 1
                    self.i = 1
                    nupp_all = False
                if self.page == len(self.tekst):
                    self.räägitud = True
            else:
                pg.draw.rect(aken, (50, 50, 50), (laius / 2 - 500, 0, 900, 220))
                TextSurf, TextRect = text_objects(self.tekst[0], menu_head2Text,(255,255,255))
                TextRect.center = (laius / 2, 100)
                aken.blit(TextSurf, TextRect)
            aken.blit(self.pic, (laius / 2 - 490, 10))
        if self.tekst[0] == "Kuidas ma saan kasulik olla?" and self.page == len(self.tekst):
            maailm.pood_unlocked.unlocked = True

class NPC_arvut(NPC):
    def __init__(self, x, y, laius, kõrgus, värv, tekst):
        NPC.__init__(self, x, y, laius, kõrgus, värv, tekst)
        self.kasutaja_parool = []
        self.tekst = "Sisestage parool!"
        self.aeg = 0
        self.access = maailm.delta_uksed
        self.vilgub = 0
        self.loading = 0

    def hacking(self):
        mouse = pg.mouse.get_pos()
        aeg = pg.time.get_ticks()
        parool = [pg.K_2, pg.K_0, pg.K_2, pg.K_0]
        if 255 < mouse[0] < 355 and 275 < mouse[1] < 315:
            if len(self.kasutaja_parool) > 4:
                self.kasutaja_parool = []
            if maailm.klahv != None and self.access.unlocked == False:
                self.kasutaja_parool.append(maailm.klahv)
                if len(self.kasutaja_parool) == len(parool):
                    if self.kasutaja_parool == parool:
                        self.tekst = "Juurdepääs lubatud!"
                        self.värv = (0,255,0)
                    else:
                        self.tekst = "Vale parool!"
                        self.värv = (255,0,0)
                        self.aeg = pg.time.get_ticks()
            if self.aeg != 0:
                if self.aeg + 2000 <= aeg:
                    self.kasutaja_parool = []
                    self.tekst = "Sisestage parool!"
                    self.aeg = 0
                    self.värv = (200,200,200)

    def NPC_räägib(self):
        if self.x + self.laius + 200 > (maailm.Tom.x + maailm.Tom.laius / 2) > self.x - 200 and self.y < maailm.Tom.y + maailm.Tom.pikkus / 2 < self.y + self.kõrgus:
            self.hacking()

            pg.draw.rect(aken, (0, 0, 0), (50, 50, 520, 300))
            pg.draw.rect(aken, (50, 50, 50), (52 , 52, 516, 296))
            pg.draw.rect(aken, self.värv, (255, 275, 100, 40))
            #Parooli display
            parool_ekraanil = "* " * len(self.kasutaja_parool)
            TextSurf, TextRect = text_objects(parool_ekraanil, menu_head2Text,(255,255,255))
            TextRect.center = (310, 300)
            aken.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects(self.tekst, menu_head2Text,(255,255,255))
            TextRect.center = (310, 100)
            aken.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("Lohistage kursor parooli aknale," , smallText,(255,255,255))
            TextRect.center = (310, 200)
            aken.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("et tuvastada klahve", smallText,(255,255,255))
            TextRect.center = (310, 225)
            aken.blit(TextSurf, TextRect)

            # Animatsioonid
            if self.värv == (0, 255, 0):
                self.animatsioonid()

    def animatsioonid(self):
        if self.värv == (0, 255, 0) and self.loading < 3:
            pg.draw.rect(aken, (50, 50, 50), (50, 50, 520, 300))
            if 0 <= self.vilgub < 10:
                TextSurf, TextRect = text_objects("LOADING", menu_head2Text,(255,255,255))
                TextRect.center = (310, 100)
                aken.blit(TextSurf, TextRect)
                self.vilgub += 1
            elif 10 <= self.vilgub < 20:
                TextSurf, TextRect = text_objects("LOADING.", menu_head2Text,(255,255,255))
                TextRect.center = (310, 100)
                aken.blit(TextSurf, TextRect)
                self.vilgub += 1
            elif 20 <= self.vilgub < 30:
                TextSurf, TextRect = text_objects("LOADING..", menu_head2Text,(255,255,255))
                TextRect.center = (310, 100)
                aken.blit(TextSurf, TextRect)
                self.vilgub += 1
            elif 30 <= self.vilgub <= 40:
                TextSurf, TextRect = text_objects("LOADING...", menu_head2Text,(255,255,255))
                TextRect.center = (310, 100)
                aken.blit(TextSurf, TextRect)
                self.vilgub += 1
                if self.vilgub > 40:
                    self.vilgub = 0
                    self.loading += 1

        if 20 > self.loading >= 3:
            pg.draw.rect(aken, (0, 0, 0), (50, 50, 520, 300))
            #XAXAXA naljakas
            inprogress = smallText.render("EI KÄPI, EI NÄPI, EI TOPI!", True, (0, 255, 0))
            aken.blit(inprogress, (190, 300))

            if 8 >= self.vilgub >= 5:
                inprogress = smallText.render("HACKING IN PROGRESS...", True, (0, 255, 0))
                aken.blit(inprogress, (190, 70))
                self.vilgub += 1
                if self.vilgub > 8:
                    self.vilgub = 0
                    self.loading += 1
            else:
                self.vilgub += 1
            pg.draw.rect(aken, (20, 20, 20), (80, 250, 460, 30))
            if self.loading <= 20:
                pg.draw.rect(aken, (0, 250, 0), (81, 251, 460 * (self.loading-2) / 18, 30))
        if self.loading == 20:
            pg.draw.rect(aken, (0, 0, 0), (50, 50, 520, 300))
            inprogress = menu_headText.render("ACCESS GRANTED", True, (0, 255, 0))
            aken.blit(inprogress, (90, 170))
            self.access.unlocked = True

#global eelm_lai
#global eelm_kõr
#eelm_lai = 0
#eelm_kõr = 0
class NPC_portaal(NPC):
    def __init__(self, x, y, laius, kõrgus, värv, tekst, siht_x, siht_y):
        NPC.__init__(self, x, y, laius, kõrgus, värv, tekst)
        self.siht_x = siht_x
        self.siht_y = siht_y
        self.aeg = 0
        self.raadius = 50 #min(self.laius,self.kõrgus)
        self.raadius_algne = 50

    global värvu
    global edasi
    värvu = 160
    edasi = True
    def draw(self):
        global värvu
        global edasi
        if värvu == 160:
            edasi = True
        if värvu == 255:
            edasi = False
        if edasi:
            värvu += 1
        else:
            värvu -= 1
        pg.draw.circle(aken, (värvu,värvu,värvu), (self.x+self.laius/2, self.y+self.kõrgus/2), self.raadius)
        self.NPC_räägib()

    def teleport(self):
        #global eelm_lai
        #global eelm_kõr
        aeg = pg.time.get_ticks()
        if self.x < (maailm.Tom.x + maailm.Tom.laius / 2) < self.x + self.laius and self.y < (maailm.Tom.y + maailm.Tom.pikkus/2) < self.y + self.kõrgus:
            if maailm.sandaalid.equipped and maailm.püksid.equipped and maailm.kasukas.equipped and maailm.kiiver.equipped:
                self.raadius += 4
                if self.aeg == 0:
                    self.aeg = aeg
                if self.aeg + 2000 <= aeg:
                    self.raadius = self.raadius_algne
                    #maailm.Tom.laius = 40
                    #maailm.Tom.pikkus = 60
                    maailm.Tom.x = self.siht_x
                    maailm.Tom.y = self.siht_y
            else:
                pg.draw.rect(aken, (50, 50, 50), (laius / 2 - 300, 0, 600, 200))
                TextSurf, TextRect = text_objects((self.tekst), menu_head2Text,(255,255,255))
                TextRect.center = (laius / 2, 100)
                aken.blit(TextSurf, TextRect)
        else:
            self.aeg = 0
            self.raadius = self.raadius_algne
            #for event in pg.event.get():
                #if event.type == pg.KEYDOWN:
            #maailm.Tom.laius = 40
            #maailm.Tom.pikkus = 60

    def NPC_räägib(self):
        self.teleport()

class Unlockable:
    def __init__(self, unlocked):
        self.unlocked = unlocked

class NPC_info(NPC):
    def __init__(self, x, y, laius, kõrgus, värv, suurus, tekst):
        NPC.__init__(self, x, y, laius, kõrgus, värv, tekst)
        self.akna_suurus = suurus
        self.tekst = tekst
        self.tekst_x = suurus[0] + 20
        self.tekst_y = suurus[1] + 100

    def NPC_räägib(self):
        if self.x + self.laius + 200 > (maailm.Tom.x + maailm.Tom.laius / 2) > self.x - 200:
            pg.draw.rect(aken, (50,50,50), (self.akna_suurus[0], self.akna_suurus[1],self.akna_suurus[2],self.akna_suurus[3]))
            #pealkiri
            TextSurf, TextRect = text_objects(self.tekst[0], menu_head2Text,(255,255,255))
            TextRect.center = (self.akna_suurus[2]/2 + self.akna_suurus[0], self.akna_suurus[1] + 30)
            aken.blit(TextSurf, TextRect)
            #Tekst
            self.tekst_y = self.akna_suurus[1] + 70
            for i in range(len(self.tekst)):
                if i == 0:
                    i += 1
                else:
                    inprogress = smallText.render(self.tekst[i], True, (0, 255, 0))
                    aken.blit(inprogress, (self.tekst_x, self.tekst_y))
                    self.tekst_y += 30
                    i += 1

class Lift(NPC):
    def __init__(self, x, y, laius, kõrgus, värv, tekst):
        NPC.__init__(self, x, y, laius, kõrgus, värv, tekst)
        self.pilet = True

    def NPC_räägib(self):
        pg.draw.rect(aken, (30, 30, 30), (self.x - 2, self.y - 32, self.laius + 4, self.kõrgus  + 32))
        if maailm.liftis == False:
            pg.draw.rect(aken, (70, 70, 70), (self.x , self.y, self.laius, self.kõrgus))
            pg.draw.rect(aken, (10, 10, 10), (self.x + self.laius / 2, self.y, 1, self.kõrgus))
        else:
            pg.draw.rect(aken, (130, 130, 130), (self.x, self.y, self.laius, self.kõrgus))
        pg.draw.rect(aken, (100, 100, 100), (self.x, self.y - 30, self.laius, 30))
        TextSurf, TextRect = text_objects("LIFT", smallText, (255, 255, 255))
        TextRect.center = (self.x + self.laius / 2, self.y - 15)
        aken.blit(TextSurf, TextRect)
        if self.x + self.laius > (maailm.Tom.x + maailm.Tom.laius / 2) > self.x and self.y < maailm.Tom.y + maailm.Tom.pikkus / 2 < self.y + self.kõrgus:
            if not maailm.lifti_kaart.unlocked:
                pg.draw.rect(aken, (50, 50, 50), (laius / 2 - 300, 0, 600, 220))
                TextSurf, TextRect = text_objects("Sul ei ole magnetkaarti!", menu_head2Text, (255, 255, 255))
                TextRect.center = (laius / 2, 100)
                aken.blit(TextSurf, TextRect)
            else:
                pg.draw.rect(aken, (50, 50, 50), (laius / 2 - 300, 0, 600, 220))
                TextSurf, TextRect = text_objects("Mis korrusele tahad minna?", menu_head2Text, (255, 255, 255))
                TextRect.center = (laius / 2, 50)
                aken.blit(TextSurf, TextRect)
                nupp(aken, "1. Korrus", 365, 130, 100, 70, (148, 82, 74), (168, 102, 94), esimesele)
                nupp(aken, "2. Korrus", 515, 130, 100, 70, (148, 82, 74), (168, 102, 94), teisele)
                nupp(aken, "3. Korrus", 665, 130, 100, 70, (148, 82, 74), (168, 102, 94), kolmandale)
                nupp(aken, "4. Korrus", 815, 130, 100, 70, (148, 82, 74), (168, 102, 94), neljandale)

global lift_animatsioon

def lift_animatsioon():
    print("jookseb")
    siseneb = True
    väljub = False
    uksed = 0
    def lift():
        põrand_laius = 800
        põrand_y = 600
        lagi_y = 100
        põrand_x = laius / 2 - 400
        sein_y = 100
        sein_kõrgus = 502
        vasak_x = laius / 2 - 400
        parem_x = laius / 2 + 400
        for i in range(150):
            pg.draw.rect(aken,(123, 144, 149), (põrand_x, põrand_y, põrand_laius, 2))
            pg.draw.rect(aken, (123, 144, 149), (põrand_x, lagi_y, põrand_laius, 2))
            põrand_y += 2
            põrand_x -= 2
            põrand_laius += 4
            lagi_y -= 2
        for i in range(300):
            pg.draw.rect(aken,(123, 127, 128), (vasak_x, sein_y, 2, sein_kõrgus))
            pg.draw.rect(aken, (123, 127, 128), (parem_x, sein_y, 2, sein_kõrgus))
            sein_kõrgus += 4
            sein_y -= 2
            parem_x += 2
            vasak_x -= 2
    lift()
    while siseneb:
        pg.draw.rect(aken, (50, 50, 50), (laius/2 - 400, 100, uksed, 500))
        pg.draw.rect(aken, (50, 50, 50), (laius/2 + 400 - uksed, 100, uksed, 500))
        pg.display.update()
        uksed += 0.35
        if uksed >= 405:
            pg.time.wait(1400)
            siseneb = False
            väljub = True
    maailm.vaheta_ekraani()
    while väljub:
        aken.fill((21, 85, 83))
        for prr in maailm.põrandad:
            prr.draw()
        for p1 in maailm.vastased:
            p1.draw()
        for item in maailm.itemid:
            item.draw()
        lift()
        uksed -= 0.35
        pg.draw.rect(aken, (50, 50, 50), (laius/2 - 400, 100, uksed, 500))
        pg.draw.rect(aken, (50, 50, 50), (laius/2 + 400 - uksed, 100, uksed, 500))
        pg.display.update()
        if uksed <= 0:
            väljub = False
def esimesele():
    maailm.screen_y = 0
    maailm.liftis = True
def teisele():
    maailm.screen_y = 1
    maailm.liftis = True
def kolmandale():
    maailm.screen_y = 2
    maailm.liftis = True
def neljandale():
    maailm.screen_y = 3
    maailm.liftis = True

class Võit():
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.collision = False
        self.r = 40
        self.punktid = []
        self.kõrgus = self.r
        self.laius = self.r
        nurk = 0
        for i in range(8):
            x = self.x + self.r * cos(nurk)
            y = self.y + self.r * sin(nurk)
            self.punktid.append((x,y))
            nurk += pi/4

    def draw(self):
        pg.draw.polygon(aken, maailm.rgb(), self.punktid)
        if self.collision:
            maailm.võit()
