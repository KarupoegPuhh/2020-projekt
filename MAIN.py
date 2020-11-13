import pygame as pg
import sys
from random import randint
import os
from Player_class import *
from Player_class_lisad import *
from abi import *
from pygame_init import *
from vastased import *


mitmes_kord = 0

    

def intro():
    global mitmes_kord
    mitmes_kord += 1
    if mitmes_kord == 1:
        global intromus
        #intromus = pg.mixer.Sound(helidir+"/delta.mp3")
        #intromus.play()

    

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

        #kontrollid
        kontrollid = smallText.render("liigu: wasd", True, (0,0,0))
        aken.blit(kontrollid, (laius-300, 20))
        kontrollid = smallText.render("tulista: space", True, (0,0,0))
        aken.blit(kontrollid, (laius-300, 40))
        kontrollid = smallText.render("menüü: p", True, (0,0,0))
        aken.blit(kontrollid, (laius-300, 60))
        kontrollid = smallText.render("KONTROLLID:", True, (0,0,0))
        aken.blit(kontrollid, (laius-300, 0))
        
        nupp(aken, "Minek!",laius/2-100, 300, 200, 100, (155,114,98), (185,144,128), main_loop)
        nupp(aken, "Vali oma sõdalane!", laius/2-100, 425, 200, 100, (72,58,78), (102,88,108), vali_sõdalane)
        nupp(aken, "Annan alla...", laius/2-100, 550, 200, 100, (42,42,50), (72,72,89), quit)
        
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
    
        
        nupp(aken, "Valik tehtud!", laius/2-100 , 600, 200, 100, (100,100,0), (255,255,0), sõdalane_valitud)
        #Relva valik
        nupp(aken, "Deus Vult!", 170, 300, 200, 100, (150,150,150), (250,250,250), esimene_sõdalane)
        nupp(aken, "Tahan olla camo!", 540, 300, 200, 100, (112,130,56), (162,180,106), teine_sõdalane)
        nupp(aken, "Vidi vini vici", 910 , 300, 200, 100, (80,5,94), (130,55,144), kolmas_sõdalane)
        
        pg.display.update()
        

def sõdalane_valitud():
    global valin_sõdalane
    valin_sõdalane = False
    
def esimene_sõdalane():
    Player.kangelane_värv = (255,255,255)
    Player.kangelane_nimi = "Jeesus Kristus"
    Player.kangelane_pilt = pg.image.load("jesus.png")
        
def teine_sõdalane():
    Player.kangelane_värv = (112,130,56)
    Player.kangelane_nimi = "al-Assad"
    Player.kangelane_pilt = pg.image.load("bashar.png")

def kolmas_sõdalane():
    Player.kangelane_värv = (80,5,94)
    Player.kangelane_nimi = "Julius Caesar"
    Player.kangelane_pilt = pg.image.load("JC_120x120.png")
    
def pood():
    global Tom
    global hernepüss
    global kartulikahur
    global ka
    global poes
    poes = True
    global ost
    ost = pg.mixer.Sound(helidir+"/cash.mp3")
    tere = pg.mixer.Sound(helidir+"/shop_e.mp3")
    tere.play()

    while poes:
        mouse = pg.mouse.get_pos()
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
                    
        nupp(aken, "Ostud tehtud!", laius/2-100 , 600, 200, 100, (100,100,0), (255,255,0), pood_done)
        #Relva valik
        if Tom.health < Tom.max_health:
            nupp(aken, "Jõujooki! -1₽", 170, 200, 200, 100, (113,16,15), (163,66,65), jõujook_ost)
            if 170 < mouse[0] < 370 and 200 < mouse[1] < 300:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                JJ = smallText.render("Saad 1 hp juurde", True, (200,200,200))
                JJ_kord = JJ.get_rect()
                JJ_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(JJ, JJ_kord)
                
        if not hernepüss.unlocked:    
            nupp(aken, "Hernepüssi! -3₽", 540, 200, 200, 100, (112,130,56), (162,180,106), hernepüss_ost)
            if 540 < mouse[0] < 740 and 200 < mouse[1] < 300:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                hernepüss_txt = smallText.render("Püstolkuulipilduja", True, (200,200,200))
                hernepüss_txt_kord = hernepüss_txt.get_rect()
                hernepüss_txt_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(hernepüss_txt, hernepüss_txt_kord)
                
        if Tom.vel <= 20:
            nupp(aken, "Ritaliini! -1₽", 910 , 200, 200, 100, (80,5,94), (130,55,144), ritaliin_ost)
            if 910 < mouse[0] < 1110 and 200 < mouse[1] < 300:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                ritaliin_txt = smallText.render("Mmmm... maitsev", True, (200,200,200))
                ritaliin_txt_kord = ritaliin_txt.get_rect()
                ritaliin_txt_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(ritaliin_txt, ritaliin_txt_kord)
            
        if not kartulikahur.unlocked:
            nupp(aken, "kartul! -4₽", 540 , 400, 200, 100, (80,5,94), (130,55,144), kartulikahur_ost)
            if 540 < mouse[0] < 740 and 400 < mouse[1] < 500:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                potato_txt = smallText.render("SeE oN hIigLasLiK!", True, (200,200,200))
                potato_txt_kord = potato_txt.get_rect()
                potato_txt_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(potato_txt, potato_txt_kord)
        
        raha = veneText.render(str(Tom.raha)+" рубль", True, (255,215,0))
        aken.blit(raha, (laius-200, 20))
        
        pg.display.update()

def pood_done():
    global poes
    poes = False
    headaega = pg.mixer.Sound(helidir+"/shop_l.mp3")
    headaega.play()
    
def jõujook_ost():
    if Tom.raha >= 1:
        Tom.raha -= 1
        if Tom.max_health - Tom.health >= 1:
            Tom.health += 1
        else:
            Tom.health += Tom.max_health - Tom.health
        ost.play()
        
def hernepüss_ost():
    if Tom.raha >= 3:
        hernepüss.unlocked = True
        Tom.raha -= 3
        ost.play()

def kartulikahur_ost():
    if Tom.raha >= 4:
        kartulikahur.unlocked = True
        Tom.raha -= 4
        ost.play()
        
def ritaliin_ost():
    global vh
    if Tom.raha >= 1:
        Tom.vel *= 1.5
        Tom.vh += 1
        vh += 1
        Tom.raha -= 1
        ost.play()

def main_loop():
    global Tom
    global Relvad
    global hernepüss
    global kartulikahur
    global pause
    
    #intromus.stop()
    
    def unpause():
        global pause
        global start
        pause = False
        pos = pg.mixer.music.get_pos()
        pg.mixer.music.stop()
        pg.mixer.music.load(helidir+"/game.mp3")
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
            
        
            nupp(aken, "Jätkan!", 170, 300, 200, 100, (0,100,0), (0,255,0), unpause)
            nupp(aken, "Annan alla", 540, 300, 200, 100, (100,100,0), (255,255,0), intro)
            nupp(aken, "Varustuse juurde", 910, 300, 200, 100, (0,100,0), (0,255,0), seljakott)
            nupp(aken, "Konsum", 540, 450, 200, 100, (0,100,0), (0,255,0), pood)
            
            pg.display.update()
            
    def seljakott():
        global sk
        sk = True
        while sk:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                    
            aken.fill((70,70,70))
            TextSurf, TextRect = text_objects("Seljakott", largeText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            
            keys = pg.key.get_pressed()
      
            if keys [pg.K_i]:
                inventory()
            
        
            nupp(aken, "Jätkan!", 170, 300, 200, 100, (0,100,0), (0,255,0), sk_done)
            nupp(aken, "Riided", 540, 300, 200, 100, (100,100,0), (255,255,0), riided)
            nupp(aken, "Relvad", 910, 300, 200, 100, (0,100,0), (0,255,0), inventory)
            
            pg.display.update()
            
    def sk_done():
        global sk
        sk = False
        
    def riided():
        global riided_m
        riided_m = True
        while riided_m:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                    
            aken.fill((70,70,70))
            TextSurf, TextRect = text_objects("Riided", largeText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            
            keys = pg.key.get_pressed()
      
            if keys [pg.K_i]:
                inventory()
            
        
            nupp(aken, "Jätkan!", 540, 600, 200, 100, (0,100,0), (0,255,0), riided_done)
            
            if kasukas.unlocked:
                if not kasukas.equipped:
                    nupp(aken, "Abramovi kasukas", 170, 300, 200, 100, (100,0,0), (200,0,0), kasukas_equip_fun)
                if kasukas.equipped:
                    nupp(aken, "Abramovi kasukas", 170, 300, 200, 100, (0,100,0), (0,200,0), kasukas_unequip_fun)
                
            pg.display.update()
            
    def riided_done():
        global riided_m
        riided_m = False
        
    def kasukas_equip_fun():
        kasukas.equip(Tom)
        
    def kasukas_unequip_fun():
        kasukas.unequip(Tom)
        
    
    
    def redrawGameWindow():
        aken.fill((21,85,83))

        for prr in põrand.instances:
            prr.draw(aken)

        Tom.draw(aken)
        for p1 in Vastane.instances:
            p1.draw(aken)
        
        for rah in raha.instances:
            rah.draw(aken)
        for kuul in kuulid:
            kuul.draw(aken)
            
        databar()
        kasukas.draw(aken)
        
        pg.display.update()
        dt = clock.tick(30)
    
    

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
        #Väike paus ja ütleb, et surid
        TextSurf, TextRect = text_objects("Sa said surma...lol", mediumText)
        TextRect.center = ((laius // 2), (170))
        aken.blit(TextSurf, TextRect)
        pg.display.update()
        pg.time.wait(3000)
    
        surm = True
        while surm:   
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            aken.fill((70,70,70))
            
            TextSurf, TextRect = text_objects("Hummid tampisid su ära...", mediumText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            
            nupp(aken, "Annan alla", 400, 375, 200, 100, (100,0,0), (255,0,0), intro)
            nupp(aken, "Proovin uuesti", 400, 250, 200, 100, (0,100,0), (0,255,0), main_loop)
            
            pg.display.update()

    def võit():
        if len(Vastane.instances) == 0 and raha.raha_maas == 0:
            TextSurf, TextRect = text_objects("VÕIT!", largeText)
            TextRect.center = ((laius // 2), (100))
            aken.blit(TextSurf, TextRect)
                
            pg.display.update()
            pg.time.wait(2000)
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                        
                aken.fill((70,70,70))
                TextSurf, TextRect = text_objects("Sa said hakkama!", largeText)
                TextRect.center = ((laius // 2), (170))
                aken.blit(TextSurf, TextRect)
                
            
                
                nupp(aken, "Aitab kah...", laius/2-100 , 500 , 200, 100, (100,100,0), (255,255,0), intro)
                
                pg.display.update()

    #inventory
    if True:    
        def inventory():
            global inventory_tab
            inventory_tab = True
            while inventory_tab:
                mouse = pg.mouse.get_pos()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                        
                aken.fill((70,70,70))
                TextSurf, TextRect = text_objects("Vali oma varustus", largeText)
                TextRect.center = ((laius // 2), (100))
                aken.blit(TextSurf, TextRect)

                TextSurf, TextRect = text_objects("(Sul on käes "+str(Relvad.instance.nimi)+")", mediumText)
                TextRect.center = ((laius // 2), (230))
                aken.blit(TextSurf, TextRect)
                
                nupp(aken, "Olen valmis naasma!", laius/2-100 , 600, 200, 100, (100,100,0), (255,255,0), invent_stop)
                #Relva valik
                if ling.unlocked:
                    nupp(aken, "lingu viskama!", 170, 300, 200, 100, (100,100,100), (200,200,200), ling_equip)
                            
                if hernepüss.unlocked:
                    nupp(aken, "Ma sain hernepüssi!", 540, 300, 200, 100, (100,100,100), (200,200,200), hernepüss_equip)
                        
                if kartulikahur.unlocked:
                    nupp(aken, "Ohh kartulikahur!", 910 , 300, 200, 100, (100,100,100), (200,200,200), kartulikahur_equip)
                        
                if railgun.unlocked:
                    nupp(aken, "Tulevik in nüüd, vanamees!", 490, 450, 300, 100, (100,100,100), (200,200,200), railgun_equip)
                    
                    
                #joonistame kasti, et infot lugeda
                nupu_hover_txt(ling, 170, 300, 200, 100, (200,200,200))
                nupu_hover_txt(hernepüss, 540, 300, 200, 100, (200,200,200))
                nupu_hover_txt(kartulikahur, 910, 300, 200, 100, (21,244,238))
                nupu_hover_txt(railgun, 490, 450, 300, 100, (191,0,255))
        
                pg.display.update()
                
        def invent_stop():
            global inventory_tab
            inventory_tab = False
            
        def ling_equip():
            if ling.unlocked:
                Relvad.instance = ling      
        def hernepüss_equip():
            if hernepüss.unlocked:
                Relvad.instance = hernepüss
        def kartulikahur_equip():
            if kartulikahur.unlocked:
                Relvad.instance = kartulikahur
        def railgun_equip():
            if railgun.unlocked:
                Relvad.instance = railgun
            
    def databar():
        pg.draw.rect(aken, (25,25,25), (238, 598, 804, 124))
        pg.draw.rect(aken, (50,50,50), (240, 600, 800, 120))
        #healthbar
        pg.draw.rect(aken, (100,0,0), (340, 625, 600, 20))
        pg.draw.rect(aken, (200,0,0), (342, 627, 596 * (Tom.health / Tom.max_health), 16))
        TextSurf, TextRect = text_objects(str(round(Tom.health, 2)) + " / " + str(Tom.max_health), databarText)
        TextRect.center = ((laius // 2), (635))
        aken.blit(TextSurf, TextRect)
        
        #Pilt tegelase jaoks
        pg.draw.rect(aken, (25,25,25), (0, 570, 124, 200))
        pg.draw.rect(aken, (50,50,50), (2, 600, 120, 120))
        aken.blit(Player.kangelane_pilt, (2,600))
        ##Tegelase nimi
        nimi = databarText.render(Player.kangelane_nimi, True, (200,200,200))
        nimi_kord = nimi.get_rect()
        nimi_kord.center = (60, 585)
        aken.blit(nimi, nimi_kord)
        
        #Üleminek pildilt healtbarile
        #pilt joonistatakse paraboolide abil
        a = -2
        x_laius = 123
        y_kõrgus = 600
        while -2 <= a <= 2:
            while -2 <= a <= 0:
                pg.draw.rect(aken, (25, 25, 25), (x_laius, y_kõrgus, 2, 125))
                a += 0.035
                x_laius -= a
                y_kõrgus += 0.5 * a**2
            while 0 <= a <= 2:
                pg.draw.rect(aken, (25, 25, 25), (x_laius, y_kõrgus, 2, 125))
                a += 0.035
                x_laius += a
                y_kõrgus -= 0.5 * a**2 
            
        
        #Displayb tegelase suurused
        #Kiirus
        TextSurf, TextRect = text_objects("Kiirus : " + str(Tom.vel), databarText)
        TextRect.center = ((laius // 2), (660))
        aken.blit(TextSurf, TextRect)
        #Relv
        TextSurf, TextRect = text_objects("Relv : " + str(Relvad.instance.nimi), databarText)
        TextRect.center = ((laius // 2), (680))
        aken.blit(TextSurf, TextRect)
        #Raha
        raha = databarText.render(str(Tom.raha)+" рубль", True, (255,215,0))
        aken.blit(raha, (915, 650))
        nupp(aken, "Konsumisse", 875, 675, 150, 25, (100,100,100), (200,200,200), pood)
        #Turvis
        TextSurf, TextRect = text_objects("Turvis : " + str(Tom.armor), databarText)
        TextRect.center = ((laius // 2), (700))
        aken.blit(TextSurf, TextRect)
        #Nupp inventoryle
        nupp(aken, "Seljakott", 260, 675, 150, 25, (100,100,100), (200,200,200), seljakott)
        

    #Maailmas olevad tegelased ja objektid
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
        global vh
        vh = Tom.vh
        Tom.vh = 0
        #Pahad
        paha = Vastane(400, 0, 500, 5, 10,True)
        paha.y = põrand1.y-paha.pikkus
        paha1 = Vastane(900, 0, 1100, 15, 2,False)
        paha1.y = põrand1.y-paha1.pikkus
        #Relvad
        ling = Relvad(2, 30, 5, (255,255,255), 15, 1, True,"ling", "Walter PPK")
        hernepüss = Relvad(1, 5, 3, (0,255,0), 20, 0, False,"hernepüss", "AK-47")
        kartulikahur = Relvad(20, 40, 10, (161,127,27), 13, 0, False,"kartulikaur", "Käsikahur")
        railgun = Relvad(0.2, 0, 20, (4,217,255),10 , 0, True,"midagi erakordset", "EMP gun")
        #Varustus
        kasukas = Varustus(0, 5, False, False, "vammus", 130, 325)
        #Et mängjal oleks alguses relv
        ling_equip()

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
    
        #taustamuusika
        pg.mixer.music.load(helidir+"/game.mp3")
        pg.mixer.music.play(-1)
        pos = 0
        global start
        start = 0

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
                if not pole_sein_v(dt, kuul.vel,kuul.x,kuul.y,3,3,9):
                    if kuul in kuulid:
                        kuulid.pop(kuulid.index(kuul))
                        whit.play()
                if not pole_sein_p(dt, kuul.vel,kuul.x,kuul.y,3,3,9):
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
            if keys [pg.K_d] and pole_sein_p(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
                Tom.x += Tom.vel*dt
                Tom.vaatab = 1
            if keys [pg.K_a] and pole_sein_v(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
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
        else:
            Tom.jump = False
            #Tom.vh = vh

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
            #if Tom.kukub:
            #    Tom.kukub = False
            #    Tom.vh = vh
            Tom.värv = (255, 0, 0)
            if Tom.vh > 0:
                F = -(0.5*Tom.m*(lükkaja_v**2)) #/2
                if F < 0 and pole_sein_p(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
                    Tom.x += (F*dt*Tom.kb)/3
                if F > 0 and pole_sein_v(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
                    Tom.x += (F*dt*Tom.kb)/3
            else:
                F = (0.5*Tom.m*(Tom.vh**2)) #/2
                Tom.kontr = True
            
            Tom.y += (F*dt)/2
            
            Tom.vh -= 1
            lükkaja_v -= 1
            if Tom.y+Tom.pikkus >= mk:
                Tom.y = mk-Tom.pikkus
                Tom.kb = 0
                Tom.vh = vh
                Tom.värv = värvike
        else:
            värvike = Tom.värv

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
                ir.kukub(dt)
            if Tom.x+Tom.laius >= ir.x and Tom.x <= ir.x and Tom.y+Tom.pikkus > ir.y-3:
                ir.instances.remove(ir)
                raha_pickup.play()
                raha.raha_maas -= 1
                Tom.raha += 1
                
        #Vastase liikumine
        for vastane in Vastane.instances:
            if vastane.elus:
                vastane.move(dt, Tom)
                
        #Collision varustusega
        if kasukas.x < Tom.x < kasukas.x + kasukas.laius and kasukas.y < Tom.y < kasukas.y + kasukas.kõrgus:
            kasukas.collision = True
        
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
                #vaenlane.
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
            pg.mixer.music.load(helidir+"/game_filt.mp3")
            start = start + pos/1000.0
            pg.mixer.music.play(-1, start)
            paused()
                
        võit()  
        redrawGameWindow()


while True:
    intro()
    main_loop()