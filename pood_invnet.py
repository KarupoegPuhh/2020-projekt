import pygame as pg
import maailm
from abi import *
from player import *
from player_lisad import *

#pood
def pood():
    global poes
    poes = True
    tere.play()

    while poes:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        aken.fill((42,45,67))
        pg.draw.rect(aken, (148, 82, 74), (446,0,388,104))
        pg.draw.rect(aken, (162, 126, 111), (450,0,380,100))
        TextSurf, TextRect = text_objects("Mida teile?", mediumText)
        TextRect.center = ((laius // 2), (50))
        aken.blit(TextSurf, TextRect)
        #Registreerime kus on kursor
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        #Joogid ja ained
        pg.draw.rect(aken, (148, 82, 74), (47,127,366,486))
        pg.draw.rect(aken, (162, 126, 111), (50,130,360,480))
        pg.draw.rect(aken, (148, 82, 74), (100,130,260,100))
        TextSurf, TextRect = text_objects("Mmm... maitsev", menu_head2Text)
        TextRect.center = (230, 180)
        aken.blit(TextSurf, TextRect)
        
        if not maailm.ritaliin:
            nupp(aken, "Ritaliini! -1₽", 130 , 250, 200, 70, (100,100,100), (15,113,115), ritaliin_ost)
            if 130 < mouse[0] < 330 and 250 < mouse[1] < 310:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                ritaliin_txt = smallText.render("Mmmm... maitsev", True, (200,200,200))
                ritaliin_txt_kord = ritaliin_txt.get_rect()
                ritaliin_txt_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(ritaliin_txt, ritaliin_txt_kord)
                
        if maailm.Tom.health < maailm.Tom.max_health:
            nupp(aken, "Jõujooki! -1₽", 130, 340, 200, 70, (100,100,100), (15,113,115), jõujook_ost)
            if 130 < mouse[0] < 330 and 340 < mouse[1] < 410:
                pg.draw.rect(aken, (100,100,100), (mouse[0], mouse[1], 200, 100))
                JJ = smallText.render("Saad 1 hp juurde", True, (200,200,200))
                JJ_kord = JJ.get_rect()
                JJ_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(JJ, JJ_kord)

            nupp(aken, "Viineripirukas! -10₽", 130, 440, 200, 70, (100, 100, 100), (15, 113, 115), viineripirukas_ost)
            if 130 < mouse[0] < 330 and 440 < mouse[1] < 510:
                pg.draw.rect(aken, (100, 100, 100), (mouse[0], mouse[1], 200, 100))
                JJ = smallText.render("Saad elud täis", True, (200, 200, 200))
                JJ_kord = JJ.get_rect()
                JJ_kord.center = (mouse[0] + 100, mouse[1] + 50)
                aken.blit(JJ, JJ_kord)
                
        #Relvade valik
        pg.draw.rect(aken, (148, 82, 74), (457,127,366,486))
        pg.draw.rect(aken, (162, 126, 111), (460,130,360,480))
        pg.draw.rect(aken, (148, 82, 74), (510,130,260,100))
        TextSurf, TextRect = text_objects("Põhh põhh...", menu_head2Text)
        TextRect.center = (640, 180)
        aken.blit(TextSurf, TextRect)
                
        if not maailm.hernepüss.unlocked:    
            nupp(aken, "Hernepüssi! -3₽", 540, 250, 200, 70, (100,100,100), (15,113,115), hernepüss_ost)   
            
        if not maailm.kartulikahur.unlocked:
            nupp(aken, "kartul! -4₽", 540 , 340, 200, 70, (100,100,100), (15,113,115), kartulikahur_ost)
                
        #Riiete valik
        pg.draw.rect(aken, (148, 82, 74), (867,127,366,486))
        pg.draw.rect(aken, (162, 126, 111), (870,130,360,480))
        pg.draw.rect(aken, (148, 82, 74), (920,130,260,100))
        TextSurf, TextRect = text_objects("Rõivad", menu_head2Text)
        TextRect.center = (1050, 180)
        aken.blit(TextSurf, TextRect)
        
        if not maailm.kiiver.unlocked:
            nupp(aken, "Näomask! -4₽", 950 , 340, 200, 70, (100,100,100), (15,113,115), kiiver_ost)
            
        
        #aken rahale ja raha
        pg.draw.rect(aken, (148, 82, 74), (1061,0,158,54))
        pg.draw.rect(aken, (162, 126, 111), (1065,0,150,50))
        raha = veneText.render(str(maailm.Tom.raha)+" рубль", True, (255,215,0))
        aken.blit(raha, (laius-200, 20))
        
        #Ostud tehtud
        nupp(aken, "Ostud tehtud!", 540, 630, 200, 70, (148, 82, 74), (168, 102, 94), pood_done)
        
        #Joonistame kastid dataga
        #relvad
        if maailm.hernepüss.unlocked == False:
            nupu_hover_txt(maailm.hernepüss, 540, 250, 200, 70, (200,200,200))
        if maailm.kartulikahur.unlocked == False:
            nupu_hover_txt(maailm.kartulikahur, 540 , 340, 200, 70, (21,244,238))
        #riided
        if maailm.kiiver.unlocked == False:
            rõiva_hover_txt(maailm.kiiver,950 , 340, 200, 70, (200,200,200))
        #söök
        if maailm.Tom.health < maailm.Tom.max_health:
            eat_hover_txt("Jõujook","Annab sulle", "ühe elupukti", 130, 340, 200, 70, (200,200,200))
            eat_hover_txt("Viineri pirukas", "Kõtu täis", "nämm!", 130, 440, 200, 70, (200, 200, 200))

        if not maailm.ritaliin:
            eat_hover_txt("Ritalin","KIIRUS!!!", "JÕUD!!!", 130 , 250, 200, 70, (21,244,238))
        
        pg.display.update()
    
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

def viineripirukas_ost():
    if maailm.Tom.raha >= 10 and maailm.Tom.health < maailm.Tom.max_health:
        maailm.Tom.raha -= 10
        maailm.Tom.health = maailm.Tom.max_health
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
        maailm.ritaliin = True
        maailm.Tom.vel += 7
        maailm.Tom.vh += 1
        maailm.Tom.initial_vh += 1
        maailm.Tom.raha -= 1
        ost.play()
        
def kiiver_ost():
    maailm.kiiver.unlocked = True
        
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
        TextSurf, TextRect = text_objects("Rõivad", menu_headText)
        TextRect.center = (250, 180)
        aken.blit(TextSurf, TextRect)
        ##Riided nupud
        if maailm.kiiver.unlocked:
            if not maailm.kiiver.equipped:
                nupp(aken, maailm.kiiver.nimi, 70, 250, 200, 70, (100,0,0), (200,0,0), kiiver_equip_fun)
                aken.blit(pea, (325,250))
            if maailm.kiiver.equipped:
                nupp(aken, maailm.kiiver.nimi, 70, 250, 200, 70, (0,100,0), (0,200,0), kiiver_unequip_fun)
                aken.blit(pea1, (325,250))
        else:
            aken.blit(pea, (325,250))
            
        if maailm.kasukas.unlocked:
            if not maailm.kasukas.equipped:
                nupp(aken, maailm.kasukas.nimi, 70, 340, 200, 70, (100,0,0), (200,0,0), kasukas_equip_fun)
                aken.blit(keha, (325,340))
            if maailm.kasukas.equipped:
                nupp(aken, maailm.kasukas.nimi, 70, 340, 200, 70, (0,100,0), (0,200,0), kasukas_unequip_fun)
                aken.blit(keha1, (325,340))
        else:
            aken.blit(keha, (325,340))
            
        if maailm.püksid.unlocked:
            if not maailm.püksid.equipped:
                nupp(aken, maailm.püksid.nimi, 70, 430, 200, 70, (100,0,0), (200,0,0), püksid_equip_fun)
                aken.blit(jalad, (325,430))
            if maailm.püksid.equipped:
                nupp(aken, maailm.püksid.nimi, 70, 430, 200, 70, (0,100,0), (0,200,0), püksid_unequip_fun)
                aken.blit(jalad1, (325,430))
        else:
            aken.blit(jalad, (325,430))
            
        if maailm.sandaalid.unlocked:
            if not maailm.sandaalid.equipped:
                nupp(aken, maailm.sandaalid.nimi, 70, 520, 200, 70, (100,0,0), (200,0,0), sandaalid_equip_fun)
                aken.blit(tossud, (325,520))
            if maailm.sandaalid.equipped:
                nupp(aken, maailm.sandaalid.nimi, 70, 520, 200, 70, (0,100,0), (0,200,0), sandaalid_unequip_fun)
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
        #Relvad
        if maailm.ling.unlocked == True:
            nupu_hover_txt(maailm.ling, 555, 250, 200, 70, (200,200,200))
        if maailm.hernepüss.unlocked == True:
            nupu_hover_txt(maailm.hernepüss, 780, 250, 200, 70, (200,200,200))
        if maailm.kartulikahur.unlocked == True:
            nupu_hover_txt(maailm.kartulikahur, 70, 430, 200, 70, (21,244,238))
        if maailm.railgun.unlocked == True:
            nupu_hover_txt(maailm.railgun, 1005, 430, 200, 70, (191,0,255))
        #Riided
        if maailm.kiiver.unlocked == True:
            rõiva_hover_txt(maailm.kiiver, 70, 250, 200, 70, (200,200,200))
        if maailm.kasukas.unlocked == True:
            rõiva_hover_txt(maailm.kasukas, 70, 340, 200, 70, (200,200,200))
        if maailm.püksid.unlocked == True:
            rõiva_hover_txt(maailm.püksid, 70, 430, 200, 70, (200,200,200))
        if maailm.sandaalid.unlocked == True:
            rõiva_hover_txt(maailm.sandaalid, 70, 520, 200, 70, (200,200,200))
        
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