import maailm
from abi import *

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
            Tom.vel += self.speed
            
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
                TextSurf, TextRect = text_objects((self.tekst[self.page])[0:self.i], menu_head2Text)
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
                TextSurf, TextRect = text_objects(self.tekst[0], menu_head2Text)
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
            TextSurf, TextRect = text_objects(parool_ekraanil, menu_head2Text)
            TextRect.center = (310, 300)
            aken.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects(self.tekst, menu_head2Text)
            TextRect.center = (310, 100)
            aken.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("Lohistage kursor parooli aknale," , smallText)
            TextRect.center = (310, 200)
            aken.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("et tuvastada klahve", smallText)
            TextRect.center = (310, 225)
            aken.blit(TextSurf, TextRect)

            # Animatsioonid
            if self.värv == (0, 255, 0):
                self.animatsioonid()

    def animatsioonid(self):
        if self.värv == (0, 255, 0) and self.loading < 3:
            pg.draw.rect(aken, (50, 50, 50), (50, 50, 520, 300))
            if 0 <= self.vilgub < 10:
                TextSurf, TextRect = text_objects("LOADING", menu_head2Text)
                TextRect.center = (310, 100)
                aken.blit(TextSurf, TextRect)
                self.vilgub += 1
            elif 10 <= self.vilgub < 20:
                TextSurf, TextRect = text_objects("LOADING.", menu_head2Text)
                TextRect.center = (310, 100)
                aken.blit(TextSurf, TextRect)
                self.vilgub += 1
            elif 20 <= self.vilgub < 30:
                TextSurf, TextRect = text_objects("LOADING..", menu_head2Text)
                TextRect.center = (310, 100)
                aken.blit(TextSurf, TextRect)
                self.vilgub += 1
            elif 30 <= self.vilgub <= 40:
                TextSurf, TextRect = text_objects("LOADING...", menu_head2Text)
                TextRect.center = (310, 100)
                aken.blit(TextSurf, TextRect)
                self.vilgub += 1
                if self.vilgub > 40:
                    self.vilgub = 0
                    self.loading += 1

        if 20 > self.loading >= 3:
            pg.draw.rect(aken, (0, 0, 0), (50, 50, 520, 300))
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

class NPC_portaal(NPC):
    def __init__(self, x, y, laius, kõrgus, värv, tekst, siht_x, siht_y):
        NPC.__init__(self, x, y, laius, kõrgus, värv, tekst)
        self.siht_x = siht_x
        self.siht_y = siht_y
        self.aeg = 0

    def teleport(self):
        aeg = pg.time.get_ticks()
        if self.x < (maailm.Tom.x + maailm.Tom.laius / 2) < self.x + self.laius and self.y < (maailm.Tom.y + maailm.Tom.pikkus/2) < self.y + self.kõrgus:
            if maailm.sandaalid.equipped:
                if self.aeg == 0:
                    self.aeg = aeg
                if self.aeg + 2000 <= aeg:
                    maailm.Tom.x = self.siht_x
                    maailm.Tom.y = self.siht_y
            else:
                pg.draw.rect(aken, (50, 50, 50), (laius / 2 - 300, 0, 600, 200))
                TextSurf, TextRect = text_objects((self.tekst), menu_head2Text)
                TextRect.center = (laius / 2, 100)
                aken.blit(TextSurf, TextRect)
        else:
            self.aeg = 0

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
        if self.x + self.laius + 200 > (maailm.Tom.x + maailm.Tom.laius / 2) > self.x - 200 and self.y - 200 < maailm.Tom.y + maailm.Tom.pikkus / 2 < self.y + self.kõrgus:
            pg.draw.rect(aken, (50,50,50), (self.akna_suurus[0], self.akna_suurus[1],self.akna_suurus[2],self.akna_suurus[3]))
            #pealkiri
            TextSurf, TextRect = text_objects(self.tekst[0], menu_head2Text)
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


