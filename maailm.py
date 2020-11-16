import pygame as pg
from põrand import *
from player import *
from vastased import *
from ekraanid import *


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
    if len(vastased_ekraanis[1]) == 0 and len(rahad) == 0:
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
    global pause
    pause = True
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        aken.fill((42,45,67))
        TextSurf, TextRect = text_objects("Tõmban hinge!", largeText)
        TextRect.center = ((520), (100))
        aken.blit(TextSurf, TextRect)
        
    
        nupp(aken, "Jätkan!", 1050, 150, 200, 100, (100,100,100), (15,113,115), unpause)
        nupp(aken, "Varustuse juurde", 1050, 300, 200, 100, (100,100,100), (15,113,115), seljakott)
        nupp(aken, "Konsum", 1050, 450, 200, 100, (100,100,100), (15,113,115), pood)
        nupp(aken, "Annan alla", 1050, 600, 200, 100, (100,100,100), (15,113,115), intro)
        
        aken.blit(sleep, (100,225))
        
        pg.display.update()
        
def rgb():
    global red 
    global green
    global blue
    global redc
    global greenc 
    global bluec 
    if redc:
        red -= 25
        green += 25
        if red <= 0:
            red = 0
            green = 250
            greenc = True
            redc = False
    elif greenc:
        green -= 25
        blue += 25
        if green <= 0:
            green = 0
            blue = 250
            bluec = True
            greenc = False
    elif bluec:
        blue -= 25
        red += 25
        if blue <= 0:
            blue = 0
            red = 250
            redc = True
            bluec = False
            red = 250    
    return (red, green, blue)


def main_loop():
    global pood, seljakott, intro
    from algus import intro
    from pood_invnet import pood, seljakott
    
    #OBJEKTID
    global pole_sein_p, pole_sein_v
    global Tom
    global kuulid, vastased, põrandad, rahad, itemid
    global hernepüss, kartulikahur, ling, railgun
    global kasukas, kiiver, püksid, sandaalid
    global ritaliin, ritaliin_cd
    
    #vars
    kuulid = []
    kuulide_cd = 0
    kuulide_maxcount = 500
    vastased = []
    põrandad = None
    rahad = []
    itemid = None
    
    #Relvad
    ling = Relvad(2, 30, 5, (255,255,255), 15, 1, True,"ling", "Walter PPK")
    hernepüss = Relvad(1, 5, 3, (0,255,0), 20, 0, False,"hernepüss", "AK-47")
    kartulikahur = Relvad(20, 40, 10, (161,127,27), 13, 0, False,"kartulikaur", "Käsikahur")
    railgun = Relvad(0.2, 0, 20, (4,217,255),10 , 0, False,"midagi erakordset", "EMP gun")
    #Varustus
    kasukas = Varustus(0, 5, False, False, "vammus")
    kiiver = Varustus(1, 2, False, False, "rattakiiver")
    püksid = Varustus(2, 1, False, True, "viigipüksid")
    sandaalid = Varustus(5, 0, False, True, "sandaalid")
    
    #Ritaliin buff
    ritaliin = False
    ritaliin_cd = 0
    global red, green, blue, redc, greenc, bluec
    red = 250
    green = 0
    blue = 0
    redc = True
    greenc = False
    bluec = False
    
    #level layout
    global screen
    global screenid
    global vastased_ekraanis
    screenid = screenide_loomine()
    screen = 0
    vastased_ekraanis = vastaste_loomine()
    itemid_ekraanis = itemite_loomine()
    
    for scr in screenid:
        põrand1 = Põrand(0,laius,500,kõrgus)
        screenid[scr].append(põrand1)
    
    
    #Et mängjal oleks alguses relv
    Tom = Player(580, 100, 40, 60, ling)

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
    ritaliin_music = False
    
    def redrawGameWindow():
        aken.fill((21,85,83))

        for prr in põrandad:
            prr.draw()

        Tom.draw()
        for p1 in vastased:
            p1.draw()
        
        for raha in rahad:
            raha.draw()
        for kuul in kuulid:
            kuul.draw()
            
        databar()
        for item in itemid:
            item.draw()
        
        pg.display.update()
        dt = clock.tick(30)
        
    def maa_kõrgus(px,lai):
        global mk
        eelm_mk = mk
        y = []
        for i in põrandad:
            if px >= i.x1-lai and px <= i.x2:
                #print(i.x1)
                #print(px+lai)
                #print(px)
                #print(i.x2)
                y.append(i.y1)

        if not y:
            mk = eelm_mk
        else:
            mk = (min(y))

    def pole_sein_v(dt,v,x,y,lai,pikk,umb=0):
        #absoluutväärtus vel
        if v < 0:
            v = -v
        #seinad vasakule minnes
        for i in põrandad:
            if x <= i.x2+(v*dt)+umb and x > i.x2 + 1-umb and not y < i.y1 - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                return False
        return True
        
    def pole_sein_p(dt,v,x,y,lai,pikk,umb=0):
        #seinad paremale minnes
        for i in põrandad:
            if x+lai+(v*dt) >= i.x1 and x+lai < i.x1 + 1 and not y < i.y1 - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                return False
        return True

    def collision(x,y,vel,plat):
        pass


    def databar():
        
        ##
        
        ##

        pg.draw.rect(aken, (25,25,25), (238, 598, 804, 124))
        pg.draw.rect(aken, (50,50,50), (240, 600, 800, 120))
        #healthbar
        pg.draw.rect(aken, (100,0,0), (340, 605, 600, 20))
        if Tom.health >= 0:
            pg.draw.rect(aken, (200,0,0), (342, 607, 596 * (Tom.health / Tom.max_health), 16))
            TextSurf, TextRect = text_objects(str(round(Tom.health, 2)) + " / " + str(Tom.max_health), databarText)
            TextRect.center = ((laius // 2), (615))
            aken.blit(TextSurf, TextRect)
        else:
            TextSurf, TextRect = text_objects("0" + " / " + str(Tom.max_health), databarText)
            TextRect.center = ((laius // 2), (615))
            aken.blit(TextSurf, TextRect)
        #ritaliinbar
        pg.draw.rect(aken, (30,30,30), (340, 630, 600, 20))
        if ritaliin:
            pg.draw.rect(aken, (rgb()), (342, 632, 596 * ((900 - ritaliin_cd) / 900 ), 16))
        TextSurf, TextRect = text_objects(("Ritaliin"), databarText)
        TextRect.center = ((laius // 2), (640))
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
        TextSurf, TextRect = text_objects("Relv : " + str(Tom.relv.nimi), databarText)
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
    
    def vaheta_ekraani():
        global põrandad
        global vastased
        global itemid
        #RAHA?
        for i in vastased:
            i.player_väljub(Tom)
        #uued platformide objektid
        põrandad = screenid.get(screen, [])
        vastased = vastased_ekraanis.get(screen,[])
        itemid = itemid_ekraanis.get(screen,[])
        for i in vastased:
            i.player_siseneb(Tom)
            
        
    vaheta_ekraani()
    #main loop
    while True:       
        #exit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        #KUULID
        if True: #lihtsalt et saaks collapsida seda
            if kuulide_cd > 0:
                kuulide_cd += 1
            if kuulide_cd > Tom.relv.cd:
                kuulide_cd = 0
            for kuul in kuulid:
                #Pahade tulistamine
                for p in vastased:
                    if kuul.y - kuul.raadius < p.hitbox[1] + p.hitbox[3] and kuul.y + kuul.raadius > p.hitbox[1] and p.elus:
                        if kuul.x - kuul.raadius < p.hitbox[0] + p.hitbox[2] and kuul.x + kuul.raadius > p.hitbox[0]:
                            kuulid.pop(kuulid.index(kuul))
                            p.hit(kuul) 
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
        
        #eelmine_mk = mk
        #maa_kõrgus(Tom.x,Tom.laius)
        
        if mk <= Tom.y + Tom.pikkus:
            Tom.y = mk-Tom.pikkus

        if Tom.kontr:
            # TOM PAREMALE JA VASAKULE      
            if keys [pg.K_d]: #and pole_sein_p(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
                Tom.x += Tom.vel*dt
                Tom.vaatab = 1
            if keys [pg.K_a]: #and pole_sein_v(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
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
                    Tom.vh = Tom.initial_vh
        else:
            Tom.jump = False
            #Tom.vh = Tom.initial_vh

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
                Tom.vh = Tom.initial_vh
        
        #TOM SAAB PIHTA
        for kuri in vastased:
            lükkaja_v = Tom.põrkub(kuri, dt)
        #if lükkaja_v < 0:  #lükkaja mõte oli knockback teha vastavaks vastase velocytiga aga see läks segaseks ja ei töötand
        #    lükkaja_v = -lükkaja_v
        lükkaja_v = Tom.vh
        #knockback

        #if pole_sein_p(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus) and pole_sein_v(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
        #    lükkab_seina = False KB FIX PROOV
        #else:
        #    lükkab_seina = True

        if Tom.kb != 0:
            #if Tom.kukub:
            #    Tom.kukub = False
            #    Tom.vh = vh
            Tom.värv = (255, 0, 0)
            if Tom.vh > 0:
                F = -(0.5*Tom.m*(lükkaja_v**2)) #/2
                if F < 0 and pole_sein_p(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus,3):
                    Tom.x += (F*dt*Tom.kb)/3
                if F > 0 and pole_sein_v(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus,3):
                #if not lükkab_seina: KB FIX PROOV
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
                Tom.vh = Tom.initial_vh
                Tom.värv = värvike
        else:
            värvike = Tom.värv
            eelmine_mk = mk
            maa_kõrgus(Tom.x,Tom.laius) #POSSIBLE KB PLATFORMI OTSA FIX AGA VÕIBOLLA TEEB MINGEID BUGE (muidu need kaks rida jooksid iga frame)

        #TULISTAMINE
        if keys[pg.K_SPACE] and kuulide_cd == 0:
            shoot.play()
            if Tom.vaatab == 1:
                suund = 1
            else:
                suund = -1

            if len(kuulid) < kuulide_maxcount:  # This will make sure we cannot exceed 5 bullets on the screen at once
                kuulid.append(Kuul(round(Tom.x+Tom.laius//2+suund*Tom.laius/2), round(Tom.y + Tom.pikkus//2), suund, Tom.relv))
            
            kuulide_cd = 1
        
        #RAHA
        for ir in rahad:
            if ir.kukkumas:
                raha_drop.play()
                ir.kukub(dt)
            if Tom.x+Tom.laius >= ir.x and Tom.x <= ir.x and Tom.y+Tom.pikkus > ir.y-3:
                rahad.remove(ir)
                raha_pickup.play()
                Tom.raha += 1
                
        #Vastase liikumine
        for vastane in vastased:
            if vastane.elus:
                vastane.move(dt, Tom)
                
        #Collision varustusega
        for item in itemid:
            if item.x < Tom.x + Tom.laius / 2 < item.x + item.laius and item.y < Tom.y + Tom.pikkus <= item.y + item.kõrgus*2:
                item.collision = True
        
        #vaheta screeni paremale
        if Tom.x+Tom.laius/2 > laius:
            #tom spawn
            Tom.x = 0-Tom.laius/2
            #kuhu poole
            screen += 1
            vaheta_ekraani()
            
        #vaheta screeni vasakule
        if Tom.x+Tom.laius/2 < 0:
            #tom spawn
            Tom.x = laius-Tom.laius/2
            #kuhu poole
            screen -= 1
            vaheta_ekraani()

        #PAUSE MENU
        if keys[pg.K_p]:
            pause = True
            pos = pg.mixer.music.get_pos()
            pg.mixer.music.stop()
            pg.mixer.music.load(helidir+"/game_filt.mp3")
            start = start + pos/1000.0
            pg.mixer.music.play(-1, start)
            paused()
        
        #Ritaliin
        if ritaliin:
            ritaliin_cd += 1
            if ritaliin_cd == 1:
                laul = randint(1, 2)
                algne_värv = Tom.värv
            if 1 < ritaliin_cd < 900:
                Tom.värv = (rgb())
            if ritaliin_cd >= 900:
                ritaliin = False
                ritaliin_cd = 0
                Tom.vel -= 7
                Tom.vh -= 1
                Tom.initial_vh -= 1
                Tom.värv = algne_värv
                
        if ritaliin and not ritaliin_music:
            ritaliin_music = True
            pg.mixer.music.stop()
            if laul == 1:
                pg.mixer.music.load(helidir+"/ritaliin.mp3")
                pg.mixer.music.play(-1, start, 2000)
            if laul == 2:
                pg.mixer.music.load(helidir+"/ritaliin1.mp3")
                pg.mixer.music.play(-1, start, 2000)     
        if not ritaliin and ritaliin_music:
            ritaliin_music = False
            pg.mixer.music.stop()
            pg.mixer.music.load(helidir+"/game.mp3")
            pg.mixer.music.play(-1, start, 1000)
            
                
        võit()
        if not Tom.elus and Tom.kontr:
            surm()
        redrawGameWindow()