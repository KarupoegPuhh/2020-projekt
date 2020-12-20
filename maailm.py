import pygame as pg
from põrand import *
from player import *
from vastased import *
from ekraanid import *
from player_lisad import *
global pole_sein_p, pole_sein_v
global Tom
global kuulid, vastased, põrandad, rahad, itemid
global hernepüss, kartulikahur, ling, railgun, scar, sau
global kasukas, kiiver, püksid, sandaalid
global ritaliin, ritaliin_cd
global esimene_kord
esimene_kord = True

def surm():
    global esimene_kord
    psurm.play()
    pg.mixer.music.stop()
    #Väike paus ja ütleb, et surid
    TextSurf, TextRect = text_objects("Sa said surma...lol", mediumText)
    TextRect.center = ((laius // 2), 170)
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
        esimene_kord = False
        nupp(aken, "tee kunstlikku hingamist", 400, 250, 200, 100, (0,100,0), (0,255,0), main_loop)
        
        pg.display.update()

def võit():
    if True:
        pg.mixer.music.stop()
        võith.play()

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
            TextSurf, TextRect = text_objects("Sa said hakkama! Kõik hummid on surnd.", mediumText)
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
        
        #ET SAAKS PAUSIST NUPUGA KA ÄRA MINNA AGA SEE EI TÖÖTAND MILLEGIPÄRST
        #for event in pg.event.get():
        #    if event.type == pg.KEYDOWN:
        #        if event.key == pg.K_ESCAPE or event.key == pg.K_p:
        #            unpause()

        nupp(aken, "Jätkan!", 1050, 150, 200, 100, (100,100,100), (15,113,115), unpause)
        nupp(aken, "Varustuse juurde", 1050, 300, 200, 100, (100,100,100), (15,113,115), seljakott)
        if maailm.pood_unlocked.unlocked:
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
    if True: #collapsimiseks
        global pood, seljakott, intro
        from algus import intro
        from pood_invnet import pood, seljakott
        
        #OBJEKTID
        global pole_sein_p, pole_sein_v
        global Tom
        global kuulid, vastased, põrandad, rahad, itemid
        global hernepüss, kartulikahur, ling, railgun, scar, sau
        global kasukas, kiiver, püksid, sandaalid, lifti_kaart
        global ritaliin, ritaliin_cd
        global delta_uksed, pood_unlocked
        global esimene_kord

        #level layout
        global screen
        global screen_y
        global screenid
        global vastased_ekraanis
        global itemid_ekraanis
        global liftis
        
        if esimene_kord:
            #vars
            vastased = []
            rahad = []
            itemid = None
            
            #Relvad
            ling = Relvad(1, 30, 5, (255,255,255), 15, True,"ling", "Walter PPK")
            hernepüss = Relvad(3, 5, 3, (0,255,0), 20, False,"hernepüss", "AK-47")
            kartulikahur = Relvad(15, 40, 10, (161,127,27), 13, False,"kartulikaur", "Käsikahur")
            railgun = Relvad(0.5, 0, 20, (4,217,255), 10, False,"midagi erakordset", "EMP gun")
            scar = Relvad(5, 10, 4, (0,0,0), 30, False, "FN SCAR", "FN SCAR")
            sau = Relvad(100, 300, 100, (0,0,255), 100, False, "Gandalgi sau", "Gandalfi sau")
            #Varustus
            kasukas = Varustus(0, 5, False, False, "Abramovi vammus")
            kiiver = Varustus(1, 2, False, False, "Näomask")
            püksid = Varustus(2, 1, False, False, "Viigipüksid")
            sandaalid = Varustus(5, 0, False, False, "Sandaalid")
            lifti_kaart = Varustus(0,0,True,False, "Magnetkiip")
            #UnlockedCheck
            delta_uksed = Unlockable(False)
            pood_unlocked = Unlockable(False)

            vastased_ekraanis = vastaste_loomine()
            itemid_ekraanis = itemite_loomine()

            #Et mängjal oleks alguses relv
            Tom = Player(580, 100, 40, 60, ling)
        
        screen = 1
        screen_y = 0
        eelmine_screen_y = 0
        liftis = False
        screenid = screenide_loomine()
        
        kuulid = []
        kuulide_cd = 0
        kuulide_maxcount = 500
        põrandad = None

        Tom.x = 580
        Tom.y = 100
        Tom.m = 1
        Tom.vel = 10
        Tom.velx = 0
        Tom.vely = 0
        Tom.põrandal = False
        Tom.laes = False
        Tom.initial_vh = 10.5
        Tom.vh = 0 #hüppe vel
        Tom.health = 10
        Tom.kb = 0 #knockback 1-paremale -1-vasakule 0-false
        Tom.kontr = True #kas saab kontrollida
        Tom.elus = True
        Tom.relv = ling
        Tom.vel_debuff = 0
        Tom.värv = Player.kangelane_värv

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
        
        vastaste_arv = 0
        for y in vastased_ekraanis:
            for x in vastased_ekraanis[y]:
                vastaste_arv += len(vastased_ekraanis[y][x])
        print("VASTASTE ARV: " + str(vastaste_arv))

        
        
        def hangi_y(plat):
            return plat.y1
        for y in screenid:
            for x in screenid[y]:
                screenid[y][x].sort(reverse=True, key=hangi_y)
        

        clock = pg.time.Clock()
        global dt
        dt = 1
        #global mk #maa kõrgus (suurem arv = madalam kõrgus)
        #mk = 500
        #global eelmine_mk
        #eelmine_mk = 500

        #taustamuusika
        pg.mixer.music.load(helidir+"/game.mp3")
        pg.mixer.music.play(-1)
        pos = 0
        global start
        start = 0
        ritaliin_music = False
        
        #taustad
        nobg = pg.image.load(os.path.dirname(os.path.abspath(__file__))+"/pildid"+"/nobg.png")
        global bg
        bg = {}
        for i in range(1):
            bg[i] = {}
            for j in range(6):
                print(os.path.dirname(os.path.abspath(__file__))+"/pildid"+"/bg"+str(i)+str(j)+".png")
                bg[i][j] = pg.image.load(os.path.dirname(os.path.abspath(__file__))+"/pildid"+"/bg"+str(i)+str(j)+".png")

    def redrawGameWindow():
        aken.fill((21,85,83))
        #try:
        #    aken.blit(bg[screen_y][screen],(0,0))
        #except:
        #    aken.blit(nobg,(0,0))
        textSurf, textRect = text_objects("KORRUS: "+str(screen_y+1),mediumText,(100,100,100))
        textRect.center = (laius/2,kõrgus/2)
        aken.blit(textSurf, textRect)

        for prr in põrandad:
            prr.draw()
        
        for p1 in vastased:
            p1.draw()
        
        for item in itemid:
            item.draw()
        
        Tom.draw()
        
        for raha in rahad:
            raha.draw()
        
        for kuul in kuulid:
            kuul.draw()
            
        databar()
        
        pg.display.update()
        dt = clock.tick(30)

    def pole_sein_v(dt,v,x,y,lai,pikk,umb=0):
        #absoluutväärtus vel
        if v < 0:
            v = -v
        #seinad vasakule minnes
        for i in põrandad:
            if x <= i.x2+(v*dt)+umb and x > i.x2 + 1-umb and y + pikk >= i.y1 and y <= i.y2: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                return False
        return True
        
    def pole_sein_p(dt,v,x,y,lai,pikk,umb=0):
        #seinad paremale minnes
        for i in põrandad:
            if x+lai+(v*dt) >= i.x1 and x+lai < i.x1 + 1 and not y < i.y1 - pikk and y <= i.y2: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                return False
        return True
    
    #global esimene_col
    #esimene_col = True
    def collision(ent):
        ent.põrandal = False
        ent.laes = False
        for plat in põrandad:
            # Collidib?
            if ent.x + ent.laius > plat.x1 and ent.x < plat.x2 and ent.y + ent.pikkus > plat.y1 and ent.y < plat.y2:
                targetx = 0
                targety = 0
                
                if ent.velx > 0:
                    targetx = plat.x1 - ent.laius
                elif ent.velx < 0:
                    targetx = plat.x2
                
                if ent.vely > 0:
                    targety = plat.y1 - ent.pikkus
                elif ent.vely < 0:
                    targety = plat.y2
                
                if abs(targety - ent.y) <= abs(ent.vely) + 0.01:
                    ent.y = targety
                    if ent.vely > 0:
                        ent.põrandal = True
                    elif ent.vely < 0:
                        ent.laes = True
                elif abs(targetx - ent.x) <= abs(ent.velx) + 0.01:
                    ent.x = targetx
                        
    def databar():
        databar_nihe = 0
        pildi_nihe = 0
        parabooli_nihe = 0
        if Tom.y > kõrgus/2 + 200:
            databar_nihe = 600
            pildi_nihe = 450
            parabooli_nihe = 640
        pg.draw.rect(aken, (25,25,25), (238, 598 - databar_nihe, 804, 124))
        pg.draw.rect(aken, (50,50,50), (240, 600 - databar_nihe, 800, 120))
        #healthbar
        pg.draw.rect(aken, (100,0,0), (340, 605 - databar_nihe, 600, 20))
        if Tom.health >= 0:
            pg.draw.rect(aken, (200,0,0), (342, 607 - databar_nihe, 596 * (Tom.health / Tom.max_health), 16))
            TextSurf, TextRect = text_objects(str(round(Tom.health, 2)) + " / " + str(Tom.max_health), databarText)
            TextRect.center = ((laius // 2), (615 - databar_nihe))
            aken.blit(TextSurf, TextRect)
        else:
            TextSurf, TextRect = text_objects("0" + " / " + str(Tom.max_health), databarText)
            TextRect.center = ((laius // 2), (615 - databar_nihe))
            aken.blit(TextSurf, TextRect)
        #ritaliinbar
        pg.draw.rect(aken, (30,30,30), (340, 630 - databar_nihe, 600, 20))
        if ritaliin:
            pg.draw.rect(aken, (rgb()), (342, 632 - databar_nihe, 596 * ((900 - ritaliin_cd) / 900 ), 16))
            TextSurf, TextRect = text_objects(("Ritaliin"), databarText,(0,0,0))
        else:
            TextSurf, TextRect = text_objects(("Ritaliin"), databarText,(100,100,100))
        TextRect.center = ((laius // 2), (640 - databar_nihe))
        aken.blit(TextSurf, TextRect)
        
        #Pilt tegelase jaoks
        ##raha cheat nupp
        def motherlode():
            Tom.raha += 1000
            maailm.pood_unlocked.unlocked = True
            hernepüss.unlocked = True
            kartulikahur.unlocked = True
            sau.unlocked = True
            railgun.unlocked = True
            scar.unlocked = True
            lifti_kaart.unlocked = True
            aeg = pg.time.get_ticks()
            if aeg + 2000 >= pg.time.get_ticks():
                TextSurf, TextRect = text_objects("MOTHERLODE", largeText)
                TextRect.center = ((laius // 2), 170)
                aken.blit(TextSurf, TextRect)
        nupp(aken, "Motherlode", 0, 695 - databar_nihe, 25, 25, (100, 100, 100), (15, 113, 115), motherlode)

        pg.draw.rect(aken, (25,25,25), (0, 570 - databar_nihe, 124, 180))
        pg.draw.rect(aken, (50,50,50), (2, 600 - databar_nihe, 120, 120))
        aken.blit(Player.kangelane_pilt, (2,600 - databar_nihe))
        ##Tegelase nimi
        nimi = databarText.render(Player.kangelane_nimi, True, (200,200,200))
        nimi_kord = nimi.get_rect()
        nimi_kord.center = (60, 585 - pildi_nihe)
        aken.blit(nimi, nimi_kord)
        
        #Üleminek pildilt healtbarile
        #pilt joonistatakse paraboolide abil
        a = -2
        x_laius = 123
        y_kõrgus = 600 - parabooli_nihe
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
        
    
        #Displayb tegelase statid
        #Kiirus
        TextSurf, TextRect = text_objects("Kiirus : " + str(abs(Tom.vel)), databarText,(200,200,200))
        TextRect.center = ((laius // 2), (660 - databar_nihe))
        aken.blit(TextSurf, TextRect)
        #Relv
        TextSurf, TextRect = text_objects("Relv : " + str(Tom.relv.nimi), databarText,(200,200,200))
        TextRect.center = ((laius // 2), (680 - databar_nihe))
        aken.blit(TextSurf, TextRect)
        #Raha
        raha = databarText.render(str(Tom.raha)+" рубль", True, (255,215,0))
        aken.blit(raha, (915, 650 - databar_nihe))
        #Turvis
        TextSurf, TextRect = text_objects("Turvis : " + str(Tom.armor), databarText,(200,200,200))
        TextRect.center = ((laius // 2), (700 - databar_nihe))
        aken.blit(TextSurf, TextRect)
        #Debuff
        if maailm.Tom.vel_debuff != 0:
            TextSurf, TextRect = text_objects("OLED NÕIUTUD!", databarText,rgb()) #(230,0,230)
            TextRect.center = ((laius // 2 + 120), (680 - databar_nihe))
            aken.blit(TextSurf, TextRect)
        if maailm.pood_unlocked.unlocked:
            nupp(aken, "Konsumisse", 875, 675 - databar_nihe, 150, 25, (100,100,100), (200,200,200), pood)
        #Nupp inventoryle
        nupp(aken, "Seljakott", 260, 675 - databar_nihe, 150, 25, (100,100,100), (200,200,200), seljakott)

    global vaheta_ekraani
    def vaheta_ekraani():
        global põrandad
        global vastased
        global itemid
        
        #tapa kõik kuulid
        for kulu in kuulid:
            if kulu in kuulid:
                kuulid.pop(kuulid.index(kulu))

        for i in vastased:
            i.player_väljub(Tom)
        
        #uued platformide objektid
        põrandad = screenid.get(screen_y, {}).get(screen, []) #screenid[screen_y][screen]
        vastased = vastased_ekraanis.get(screen_y,{}).get(screen, [])
        itemid = itemid_ekraanis.get(screen_y,{}).get(screen, [])
        
        for i in vastased:
            i.player_siseneb(Tom)
            
        
    vaheta_ekraani()

    global klahv

    #main loop
    while True:       
        #exit
        klahv = None
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                klahv = event.key

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
                            if kuul in kuulid:
                                kuulid.pop(kuulid.index(kuul))
                            p.hit(kuul) 
                            if randint(0,2):
                                vastane_valu.play()
                            else:
                                vastane_valu2.play()
                            break

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
        
        Tom.velx = 0
        Tom.vely = 0
        
        if Tom.kontr:
            # TOM PAREMALE JA VASAKULE
            if keys [pg.K_d] or keys [pg.K_RIGHT]: #and pole_sein_p(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
                Tom.velx += Tom.vel*dt
                Tom.vaatab = 1
            if keys [pg.K_a] or keys [pg.K_LEFT]: #and pole_sein_v(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
                Tom.velx -= Tom.vel*dt
                Tom.vaatab = -1
            
            if Tom.kb == 0:
                Tom.vh -= 1
                
                # TOM HÜPPAMINE
                if Tom.põrandal:
                    if keys [pg.K_w] or keys [pg.K_z]:
                        Tom.vh = Tom.initial_vh
                        if randint(0,2):
                            hop.play()
                        else:
                            hop2.play()
                
                #F = 1 / 2 * mass * velocity ^ 2
                if Tom.vh > 0:
                    F = (0.5*Tom.m*(Tom.vh**2)) #/2
                else:
                    F = -(0.5*Tom.m*(Tom.vh**2)) #/2
                
                Tom.vely -= F*dt

        
        #if lükkaja_v < 0:  #lükkaja mõte oli knockback teha vastavaks vastase velocytiga aga see läks segaseks ja ei töötand
        #    lükkaja_v = -lükkaja_v
        #knockback

        #if pole_sein_p(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus) and pole_sein_v(dt, Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
        #    lükkab_seina = False KB FIX PROOV
        #else:
        #    lükkab_seina = True
        if Tom.kb != 0:
            #if Tom.kukub:
            #    Tom.kukub = False
            #    Tom.vh = vh
            if Tom.vh > 0:
                F = -(0.5*Tom.m*(Tom.vh**2)) #/2
                if F < 0:
                    Tom.velx += (F*dt*Tom.kb)/3
                if F > 0:
                    Tom.velx += (F*dt*Tom.kb)/3
            else:
                F = (0.5*Tom.m*(Tom.vh**2)) #/2
                Tom.kontr = True
            
            Tom.vely += (F*dt)/2
            
            Tom.vh -= 1
            
            if Tom.vely >= 0 and Tom.põrandal:
                Tom.kb = 0
                Tom.värv = Player.kangelane_värv

        #TULISTAMINE
        if (keys[pg.K_SPACE] or keys[pg.K_x]) and kuulide_cd == 0:
            shoot.play()
            if Tom.vaatab == 1:
                if Tom.vel_debuff == 0:
                    suund = 1
                else:
                    suund = -1
            else:
                if Tom.vel_debuff == 0:
                    suund = -1
                else:
                    suund = 1

            if len(kuulid) < kuulide_maxcount:  # This will make sure we cannot exceed 5 bullets on the screen at once
                kuulid.append(Kuul(round(Tom.x+Tom.laius//2+suund*Tom.laius/2), round(Tom.y + Tom.pikkus//2), suund, Tom.relv))
            
            kuulide_cd = 1
        
        #RAHA
        for ir in rahad:
            if ir.kukkumas:
                raha_drop.play()
                ir.kukub(dt)
            if Tom.x+Tom.laius >= ir.x and Tom.x <= ir.x and Tom.y+Tom.pikkus > ir.y-3 and Tom.y < ir.y:
                rahad.remove(ir)
                raha_pickup.play()
                Tom.raha += 1
                
        #Vastase liikumine
        for vastane in vastased:
            if vastane.elus:
                vastane.move(dt, Tom)

                
        #Collision varustusega
        for item in itemid:
            if Tom.x < (item.x + item.laius / 2) < Tom.x + Tom.laius and Tom.y < item.y + item.kõrgus/2 <= Tom.y + Tom.pikkus:
                item.collision = True
        
        # COLLISION HANDLING
        Tom.x += Tom.velx
        Tom.y += Tom.vely
        collision(Tom)
        if Tom.põrandal or Tom.laes:
            Tom.vh = 0
        
        #print(Tom.vh, Tom.põrandal, Tom.laes, Tom.kb, Tom.kontr, Tom.velx, Tom.vely, Tom.x)
        
        #TOM SAAB PIHTA
        for kuri in vastased:
            Tom.põrkub(kuri, dt)
        
        #vaheta screeni paremale
        if Tom.x+(Tom.laius/2) > laius:
            #tom spawn
            Tom.x = 0-(Tom.laius/2)
            #raha
            for raha in rahad:
                raha.x -= laius
            #kuhu poole
            screen += 1
            vaheta_ekraani()
            
        #vaheta screeni vasakule
        if Tom.x+(Tom.laius/2) < 0:
            #tom spawn
            Tom.x = laius-(Tom.laius/2)
            #raha
            for raha in rahad:
                raha.x += laius
            #kuhu poole
            screen -= 1
            vaheta_ekraani()

        #vaheta screeni üles
        if Tom.y+(Tom.pikkus/2) < 0:
            #tom spawn
            Tom.y = kõrgus-(Tom.pikkus/2)
            #raha
            for raha in rahad:
                raha.y -= kõrgus
            #kuhu poole
            screen_y += 1
            vaheta_ekraani()
            
        #vaheta screeni alla
        if Tom.y+(Tom.pikkus/2) > kõrgus:
            #tom spawn
            Tom.y = 0-(Tom.pikkus/2)
            #raha
            for raha in rahad:
                raha.y += kõrgus
            #kuhu poole
            screen_y -= 1
            vaheta_ekraani()

        #PAUSE MENU
        if keys[pg.K_p]: #or keys[pg.K_ESCAPE]:
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
                Tom.vh -= 1
                Tom.initial_vh -= 1
                Tom.värv = algne_värv
                if Tom.vel > 0:
                    Tom.vel -= 7
                else:
                    Tom.vel += 7

                
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

        #preester kiiruse debuff
        if Tom.vel < 0:
            Tom.vel_debuff -= 1
            if Tom.vel_debuff == 0:
                Tom.vel *= -1
        else:
            Tom.vel_debuff = 0

        if not Tom.elus and Tom.kontr or screen_y < 0:
            surm()

        if screen_y != eelmine_screen_y and liftis:
            print("maailm")
            liftis = False
            lift_animatsioon()
        eelmine_screen_y = screen_y


        redrawGameWindow()