import pygame as pg
from põrand import *
from player import *
from vastased import *


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
    if len(vastased) == 0 and len(rahad) == 0:
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


def main_loop():
    global pood, seljakott, intro
    from algus import intro
    from pood_invnet import pood, seljakott
    
    #OBJEKTID
    global pole_sein_p, pole_sein_v
    global Tom
    global kuulid, vastased, põrandad, rahad
    global hernepüss, kartulikahur, ling, railgun
    global kasukas
    
    #vars
    kuulid = []
    kuulide_cd = 0
    kuulide_maxcount = 500
    vastased = []
    põrandad = []
    rahad = []
    
    #level layout
    põrand1 = Põrand(0,laius,500)#(0,600,500)
    põrandad.append(põrand1)
    global screen
    screen = 0
    global screenid
    screenid = {
    -1:[Põrand(750+400,800+400,250)],
    0:[Põrand(750+400,800+400,250),Põrand(100,200,400),Põrand(700,850,400)],
    1:[Põrand(10+400,800+400,250),Põrand(100,400,400),Põrand(700,720,600)]
    }
    #uued platformide objektid
    for o in range(len(screenid[screen])):
        põrandad.append(screenid[screen][o])
    
    #Pahad
    paha = Vastane(400, 0, 500, 5, 10,True)
    paha.y = põrand1.y-paha.pikkus
    paha1 = Vastane(900, 0, 1100, 15, 2,False)
    paha1.y = põrand1.y-paha1.pikkus
    vastased.append(paha)
    vastased.append(paha1)
    
    #Relvad
    ling = Relvad(2, 30, 5, (255,255,255), 15, 1, True,"ling", "Walter PPK")
    hernepüss = Relvad(1, 5, 3, (0,255,0), 20, 0, False,"hernepüss", "AK-47")
    kartulikahur = Relvad(20, 40, 10, (161,127,27), 13, 0, False,"kartulikaur", "Käsikahur")
    railgun = Relvad(0.2, 0, 20, (4,217,255),10 , 0, True,"midagi erakordset", "EMP gun")
    #Varustus
    kasukas = Varustus(0, 5, False, False, "vammus", 130, 325)
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
    
    def redrawGameWindow():
        aken.fill((21,85,83))

        for prr in põrandad:
            prr.draw(aken)

        Tom.draw(aken)
        for p1 in vastased:
            p1.draw(aken)
        
        for rah in rahad:
            rah.draw(aken)
        for kuul in kuulid:
            kuul.draw(aken)
            
        databar()
        kasukas.draw(aken)
        
        pg.display.update()
        dt = clock.tick(30)
        
    def maa_kõrgus(px,lai,obj=põrandad):
        global mk
        eelm_mk = mk
        y = []
        for i in obj:
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

    def pole_sein_v(dt,v,x,y,lai,pikk,umb=0,obj=põrandad):
        #absoluutväärtus vel
        if v < 0:
            v = -v
        #seinad vasakule minnes
        for i in obj:
            if x <= i.x2+(v*dt)+umb and x > i.x2 + 1-umb and not y < i.y - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                return False
        return True
        
    def pole_sein_p(dt,v,x,y,lai,pikk,umb=0,obj=põrandad):
        #seinad paremale minnes
        for i in obj:
            if x+lai+(v*dt) >= i.x1 and x+lai < i.x1 + 1 and not y < i.y - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                return False
        return True


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
                Tom.vh = Tom.initial_vh
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
        if kasukas.x < Tom.x < kasukas.x + kasukas.laius and kasukas.y < Tom.y < kasukas.y + kasukas.kõrgus:
            kasukas.collision = True
        
        #vaheta screeni paremale
        if Tom.x+Tom.laius/2 > laius:
            #tom spawn
            Tom.x = 0-Tom.laius/2
            #kustuta eelmised
            for rii in põrandad:
                põrandad.remove(rii)
            #kuhu poole
            screen += 1
            #uued platformide objektid
            põrand1 = Põrand(0,laius,500)
            põrandad.append(põrand1)
            for o in range(len(screenid[screen])):
                põrandad.append(screenid[screen][o])
            #vaenlased liigutada
            for vaenlane in vastased:
                vaenlane.x -= laius
                #vaenlane.
            #uued vaenlased
            #veel implementimata
        #vaheta screeni vasakule
        if Tom.x+Tom.laius/2 < 0:
            #tom spawn
            Tom.x = laius-Tom.laius/2
            #kustuta eelmised platvormid
            for rii in põrandad:
                põrandad.remove(rii)
            #kuhu poole
            screen -= 1
            #uued platformide objektid
            põrand1 = Põrand(0,laius,500)
            põrandad.append(põrand1)
            for o in range(len(screenid[screen])):
                põrandad.append(screenid[screen][o])
            #vaenlased liigutada
            for vaenlane in vastased:
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
        if not Tom.elus and Tom.kontr:
            surm()
        redrawGameWindow()