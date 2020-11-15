import os
import pygame as pg
from pygame_init import *


dirr = os.path.dirname(os.path.abspath(__file__))
helidir = dirr+"/helid"
fontdir = dirr+"/fontid"
#piltdir = dirr+"/pildid"

#helid
nupp_hover = pg.mixer.Sound(helidir+"/click_h.wav")
nupp_klikk = pg.mixer.Sound(helidir+"/click.wav")
vastane_valu = pg.mixer.Sound(helidir+"/Zhurt.mp3")
vastane_valu2 = pg.mixer.Sound(helidir+"/Zhurt1.mp3")
vastane_surm = pg.mixer.Sound(helidir+"/Zdeath.mp3")
valu = pg.mixer.Sound(helidir+"/hurt.mp3")
psurm = pg.mixer.Sound(helidir+"/death.mp3")
shoot = pg.mixer.Sound(helidir+"/shoot.mp3")
whit = pg.mixer.Sound(helidir+"/hit.mp3")
hop = pg.mixer.Sound(helidir+"/hop.mp3")
hop2 = pg.mixer.Sound(helidir+"/hop1.mp3")
pg.mixer.Sound.set_volume(shoot,0.4)
pg.mixer.Sound.set_volume(whit,0.4)
raha_pickup = pg.mixer.Sound(helidir+"/gold_pickup.mp3")
raha_drop = pg.mixer.Sound(helidir+"/gold_drop.mp3")
pg.mixer.Sound.set_volume(raha_drop,0.4)
pg.mixer.Sound.set_volume(raha_pickup,0.4)
ost = pg.mixer.Sound(helidir+"/cash.mp3")
tere = pg.mixer.Sound(helidir+"/shop_e.mp3")

#Teksdid
largeText = pg.font.Font(fontdir+"/RL.ttf", 150)
mediumText = pg.font.Font(fontdir+"/RM.ttf", 70)
smallText = pg.font.Font(fontdir+"/RM.ttf", 22)
veneText = pg.font.SysFont(fontdir+"/MIROSLN.ttf", 36)
databarText = pg.font.Font(fontdir+"/RM.ttf", 15)
menu_headText = pg.font.Font(fontdir+"/RM.ttf", 50)



def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

hiir_all = False
#hoverib = False
#vana_hover = False
def nupp(aken, text, x, y, laius, kõrgus, värv_tuhm, värv_hele, action=None):
    global hiir_all
    #global hoverib
    #global vana_hover
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    #if vana_hover != hoverib:
    #    nupp_hover.play()  
    if x + laius > mouse[0] > x and y + kõrgus > mouse[1] > y:
        #hoverib = True
        pg.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
        pg.draw.rect(aken, värv_hele, (x-2, y-2, laius, kõrgus))
        hiir_vabastatud = False
        if hiir_all and not click[0]:
            hiir_vabastatud = True
        hiir_all = click[0]
        if hiir_vabastatud:
            nupp_klikk.play()
            action()

    else:
        pg.draw.rect(aken, (0,0,0), (x-2, y-1, laius+4, kõrgus+2))
        pg.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
        #hoverib = False
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x+x+laius)//2, (y+y+kõrgus)//2)
    aken.blit(textSurf, textRect)

    #vana_hover = hoverib
    
def nupu_hover_txt(item, x,y,laius,kõrgus, txt_värv):
    mouse = pg.mouse.get_pos()
    if x < mouse[0] < x + laius and y < mouse[1] < y + kõrgus and item.unlocked:
        #infoleht
        pg.draw.rect(aken, (10,10,10), (mouse[0], mouse[1], 200, 135))
        #nimi
        nupp_hover_tekst = smallText.render("Nimi : " + str(item.nimi_data), True, txt_värv)
        nupp_hover_tekst_kord = nupp_hover_tekst.get_rect()
        nupp_hover_tekst_kord.center = (mouse[0] + 100, mouse[1] + 15)
        aken.blit(nupp_hover_tekst, nupp_hover_tekst_kord)
        #dmg
        relv_dmg_txt = smallText.render("võimsus : " + str(item.dmg), True, txt_värv)
        relv_dmg_txt_kord = relv_dmg_txt.get_rect()
        relv_dmg_txt_kord.center = (mouse[0] + 100, mouse[1] + 45)
        aken.blit(relv_dmg_txt, relv_dmg_txt_kord)
        #kiirus
        relv_dmg_txt = smallText.render("kiirus : " + str(item.vel), True, txt_värv)
        relv_dmg_txt_kord = relv_dmg_txt.get_rect()
        relv_dmg_txt_kord.center = (mouse[0] + 100, mouse[1] + 75)
        aken.blit(relv_dmg_txt, relv_dmg_txt_kord)
        #cd
        relv_dmg_txt = smallText.render("laadimisaeg : " + str(item.cd), True, txt_värv)
        relv_dmg_txt_kord = relv_dmg_txt.get_rect()
        relv_dmg_txt_kord.center = (mouse[0] + 100, mouse[1] + 105)
        aken.blit(relv_dmg_txt, relv_dmg_txt_kord)
