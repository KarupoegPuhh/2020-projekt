import pygame as pg
import maailm
from abi import *
from player import *
from player_lisad import *

dirr = os.path.dirname(os.path.abspath(__file__))
piltdir = dirr+"/pildid"

pea = pg.image.load(piltdir+"/pea.png")
keha = pg.image.load(piltdir+"/keha.png")
jalad = pg.image.load(piltdir+"/jalad.png")
tossud = pg.image.load(piltdir+"/tossud.png")
pea1 = pg.image.load(piltdir+"/pea1.png")
keha1 = pg.image.load(piltdir+"/keha1.png")
jalad1 = pg.image.load(piltdir+"/jalad1.png")
tossud1 = pg.image.load(piltdir+"/tossud1.png")

#pood
def pood():
    global poes
    poes = True
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
        if maailm.Tom.health < maailm.Tom.max_health:
            nupp(aken, "Jõujooki! -1₽", 170, 200, 200, 100, (113,16,15), (163,66,65), jõujook_ost)
            if 170 < mouse[0] < 370 and 200 < mouse[1] < 300:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                JJ = smallText.render("Saad 1 hp juurde", True, (200,200,200))
                JJ_kord = JJ.get_rect()
                JJ_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(JJ, JJ_kord)
                
        if not maailm.hernepüss.unlocked:    
            nupp(aken, "Hernepüssi! -3₽", 540, 200, 200, 100, (112,130,56), (162,180,106), hernepüss_ost)
            if 540 < mouse[0] < 740 and 200 < mouse[1] < 300:   
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                hernepüss_txt = smallText.render("Püstolkuulipilduja", True, (200,200,200))
                hernepüss_txt_kord = hernepüss_txt.get_rect()
                hernepüss_txt_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(hernepüss_txt, hernepüss_txt_kord)
                
        if abs(maailm.Tom.vel) <= 20:
            nupp(aken, "Ritaliini! -1₽", 910 , 200, 200, 100, (80,5,94), (130,55,144), ritaliin_ost)
            if 910 < mouse[0] < 1110 and 200 < mouse[1] < 300:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                ritaliin_txt = smallText.render("Mmmm... maitsev", True, (200,200,200))
                ritaliin_txt_kord = ritaliin_txt.get_rect()
                ritaliin_txt_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(ritaliin_txt, ritaliin_txt_kord)
            
        if not maailm.kartulikahur.unlocked:
            nupp(aken, "kartul! -4₽", 540 , 400, 200, 100, (80,5,94), (130,55,144), kartulikahur_ost)
            if 540 < mouse[0] < 740 and 400 < mouse[1] < 500:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                potato_txt = smallText.render("SeE oN hIigLasLiK!", True, (200,200,200))
                potato_txt_kord = potato_txt.get_rect()
                potato_txt_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(potato_txt, potato_txt_kord)
        
        raha = veneText.render(str(maailm.Tom.raha)+" рубль", True, (255,215,0))
        aken.blit(raha, (laius-200, 20))
        
        pg.display.update()


#inventory   
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

        TextSurf, TextRect = text_objects("(Sul on käes "+str(maailm.Tom.relv.nimi)+")", mediumText)
        TextRect.center = ((laius // 2), (230))
        aken.blit(TextSurf, TextRect)
        
        nupp(aken, "Olen valmis naasma!", laius/2-100 , 600, 200, 100, (100,100,0), (255,255,0), invent_stop)
        #Relva valik
        if maailm.ling.unlocked:
            nupp(aken, "lingu viskama!", 170, 300, 200, 100, (100,100,100), (200,200,200), ling_equip)
                    
        if maailm.hernepüss.unlocked:
            nupp(aken, "Ma sain hernepüssi!", 540, 300, 200, 100, (100,100,100), (200,200,200), hernepüss_equip)
                
        if maailm.kartulikahur.unlocked:
            nupp(aken, "Ohh kartulikahur!", 910 , 300, 200, 100, (100,100,100), (200,200,200), kartulikahur_equip)
                
        if maailm.railgun.unlocked:
            nupp(aken, "Tulevik in nüüd, vanamees!", 490, 450, 300, 100, (100,100,100), (200,200,200), railgun_equip)
            
            
        #joonistame kasti, et infot lugeda
        nupu_hover_txt(maailm.ling, 170, 300, 200, 100, (200,200,200))
        nupu_hover_txt(maailm.hernepüss, 540, 300, 200, 100, (200,200,200))
        nupu_hover_txt(maailm.kartulikahur, 910, 300, 200, 100, (21,244,238))
        nupu_hover_txt(maailm.railgun, 490, 450, 300, 100, (191,0,255))

        pg.display.update()
        
def invent_stop():
    global inventory_tab
    inventory_tab = False
    
def ling_equip():
    if maailm.ling.unlocked:
        maailm.Tom.relv = maailm.ling      
def hernepüss_equip():
    if maailm.hernepüss.unlocked:
        maailm.Tom.relv = maailm.hernepüss
def kartulikahur_equip():
    if maailm.kartulikahur.unlocked:
        maailm.Tom.relv = maailm.kartulikahur
def railgun_equip():
    if maailm.railgun.unlocked:
        maailm.Tom.relv = maailm.railgun
                
def pood_done():
    global poes
    poes = False
    headaega = pg.mixer.Sound(helidir+"/shop_l.mp3")
    headaega.play()
    
def jõujook_ost():
    if maailm.Tom.raha >= 1:
        maailm.Tom.raha -= 1
        if maailm.Tom.max_health - maailm.Tom.health >= 1:
            maailm.Tom.health += 1
        else:
            maailm.Tom.health += maailm.Tom.max_health - maailm.Tom.health
        ost.play()
        
def hernepüss_ost():
    if maailm.Tom.raha >= 3:
        maailm.hernepüss.unlocked = True
        maailm.Tom.raha -= 3
        ost.play()

def kartulikahur_ost():
    if maailm.Tom.raha >= 4:
        maailm.kartulikahur.unlocked = True
        maailm.Tom.raha -= 4
        ost.play()
        
def ritaliin_ost():
    global vh
    if maailm.Tom.raha >= 1:
        maailm.Tom.vel *= 1.5
        maailm.Tom.vh += 1
        maailm.Tom.initial_vh += 1
        maailm.Tom.raha -= 1
        ost.play()
        
#Seljakott
def seljakott():
    global sk
    sk = True
    while sk:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        aken.fill((42,45,67))
        pg.draw.rect(aken, (148, 82, 74), (466,0,348,104))
        pg.draw.rect(aken, (162, 126, 111), (470,0,340,100))
        TextSurf, TextRect = text_objects("Seljakott", mediumText)
        TextRect.center = ((laius // 2), (50))
        aken.blit(TextSurf, TextRect)
        #Riided ja relvad eraldi
        #riided
        pg.draw.rect(aken, (148, 82, 74), (47,127,406,486))
        pg.draw.rect(aken, (162, 126, 111), (50,130,400,480))
        pg.draw.rect(aken, (148, 82, 74), (150,130,200,100))
        #pg.draw.rect(aken, (238, 244, 212), (155,135,190,90)) veel üks kast nimele
        TextSurf, TextRect = text_objects("Rõivad", menu_headText)
        TextRect.center = (250, 180)
        aken.blit(TextSurf, TextRect)
        ##Riided nupud
        if maailm.kiiver.unlocked:
            if not maailm.kiiver.equipped:
                nupp(aken, "Aero kiiver", 70, 250, 200, 70, (100,0,0), (200,0,0), kiiver_equip_fun)
                aken.blit(pea, (325,250))
            if maailm.kiiver.equipped:
                nupp(aken, "Aero kiiver", 70, 250, 200, 70, (0,100,0), (0,200,0), kiiver_unequip_fun)
                aken.blit(pea1, (325,250))
        else:
            aken.blit(pea, (325,250))
            
        if maailm.kasukas.unlocked:
            if not maailm.kasukas.equipped:
                nupp(aken, "Abramovi kasukas", 70, 340, 200, 70, (100,0,0), (200,0,0), kasukas_equip_fun)
                aken.blit(keha, (325,340))
            if maailm.kasukas.equipped:
                nupp(aken, "Abramovi kasukas", 70, 340, 200, 70, (0,100,0), (0,200,0), kasukas_unequip_fun)
                aken.blit(keha1, (325,340))
        else:
            aken.blit(keha, (325,340))
            
        if maailm.püksid.unlocked:
            if not maailm.püksid.equipped:
                nupp(aken, "Viigipüksid", 70, 430, 200, 70, (100,0,0), (200,0,0), püksid_equip_fun)
                aken.blit(jalad, (325,430))
            if maailm.püksid.equipped:
                nupp(aken, "Viigipüksid", 70, 430, 200, 70, (0,100,0), (0,200,0), püksid_unequip_fun)
                aken.blit(jalad1, (325,430))
        else:
            aken.blit(jalad, (325,430))
            
        if maailm.sandaalid.unlocked:
            if not maailm.sandaalid.equipped:
                nupp(aken, "Sandaalid", 70, 520, 200, 70, (100,0,0), (200,0,0), sandaalid_equip_fun)
                aken.blit(tossud, (325,520))
            if maailm.sandaalid.equipped:
                nupp(aken, "Sandaalid", 70, 520, 200, 70, (0,100,0), (0,200,0), sandaalid_unequip_fun)
                aken.blit(tossud1, (325,520))
        else:
            aken.blit(tossud, (325,520))
           
        #relvad
        pg.draw.rect(aken, (148, 82, 74), (527,127,706,486))
        pg.draw.rect(aken, (162, 126, 111), (530,130,700,480))
        pg.draw.rect(aken, (148, 82, 74), (780,130,200,100))
        TextSurf, TextRect = text_objects("Relvad", menu_headText)
        TextRect.center = (880, 180)
        aken.blit(TextSurf, TextRect)
        ##Relvad nupp
        if maailm.ling.unlocked:
            nupp(aken, "Ling", 555, 250, 200, 70, (100,100,100), (15,113,115), ling_equip)
                    
        if maailm.hernepüss.unlocked:
            nupp(aken, "Hernepüss", 780, 250, 200, 70, (100,100,100), (15,113,115), hernepüss_equip)
                
        if maailm.kartulikahur.unlocked:
            nupp(aken, "Kartulikahur", 1005, 250, 200, 70, (100,100,100), (15,113,115), kartulikahur_equip)
                
        if maailm.railgun.unlocked:
            nupp(aken, "EMP gun", 1005, 430, 200, 70, (100,100,100), (15,113,115), railgun_equip)
               
        ###joonistame kasti, et infot lugeda
        nupu_hover_txt(maailm.ling, 555, 250, 200, 70, (200,200,200))
        nupu_hover_txt(maailm.hernepüss, 780, 250, 200, 70, (200,200,200))
        nupu_hover_txt(maailm.kartulikahur, 1005, 250, 200, 70, (21,244,238))
        nupu_hover_txt(maailm.railgun, 1005, 430, 200, 70, (191,0,255))
        
        TextSurf, TextRect = text_objects("(Sul on käes "+str(maailm.Tom.relv.nimi)+")", smallText)
        TextRect.center = (880, 570)
        aken.blit(TextSurf, TextRect)
        
        
        #Järtkan/tagasi nupp
        nupp(aken, "Jätkan!", 590, 630, 100, 70, (148, 82, 74), (168, 102, 94), sk_done)
        
        pg.display.update()
        
def sk_done():
    global sk
    sk = False
    
def kasukas_equip_fun():
    maailm.kasukas.equip(maailm.Tom)
    
def kasukas_unequip_fun():
    maailm.kasukas.unequip(maailm.Tom)
    
def kiiver_equip_fun():
    maailm.kiiver.equip(maailm.Tom)
    
def kiiver_unequip_fun():
    maailm.kiiver.unequip(maailm.Tom)
    
def püksid_equip_fun():
    maailm.püksid.equip(maailm.Tom)
    
def püksid_unequip_fun():
    maailm.püksid.unequip(maailm.Tom)
    
def sandaalid_equip_fun():
    maailm.sandaalid.equip(maailm.Tom)
    
def sandaalid_unequip_fun():
    maailm.sandaalid.unequip(maailm.Tom)