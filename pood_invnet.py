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
                
        if maailm.Tom.vel <= 20:
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
        
        if maailm.kasukas.unlocked:
            if not maailm.kasukas.equipped:
                nupp(aken, "Abramovi kasukas", 170, 300, 200, 100, (100,0,0), (200,0,0), kasukas_equip_fun)
            if maailm.kasukas.equipped:
                nupp(aken, "Abramovi kasukas", 170, 300, 200, 100, (0,100,0), (0,200,0), kasukas_unequip_fun)
            
        pg.display.update()
        
def riided_done():
    global riided_m
    riided_m = False
    
def kasukas_equip_fun():
    maailm.kasukas.equip(maailm.Tom)
    
def kasukas_unequip_fun():
    maailm.kasukas.unequip(maailm.Tom)