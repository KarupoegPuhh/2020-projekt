import maailm
import pygame as pg
from pygame_init import *
from abi import *
from player import *
from random import randint

mitmes_kord = 0
tegelane_pilt_menüüs = jeesus1

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
        
        nupp(aken, "Minek!",laius/2-100, 300, 200, 100, (155,114,98), (185,144,128), maailm.main_loop)
        nupp(aken, "Vali oma sõdalane!", laius/2-100, 425, 200, 100, (72,58,78), (102,88,108), vali_sõdalane)
        nupp(aken, "Annan alla...", laius/2-100, 550, 200, 100, (42,42,50), (72,72,89), quit)
        
        pg.display.update()
        
def vali_sõdalane():
    global a
    global valin_sõdalane
    valin_sõdalane = True
    while valin_sõdalane:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        aken.fill((42,45,67))
            
        #Currently selected sõdalane 200x200 pilt
        aken.blit(tegelane_pilt_menüüs,(540,10))
        aken.blit(border, (530,0))
        
        #Valisõdalane tekst
        TextSurf, TextRect = text_objects("Vali oma sõdalane!", mediumText)
        TextRect.center = ((laius // 2), (270))
        aken.blit(TextSurf, TextRect)
    
        
        nupp(aken, "Valik tehtud!", laius/2-100 , 600, 200, 100, (148, 82, 74), (168, 102, 94), sõdalane_valitud)
        #Tegelase valik
        nupp(aken, "Kalkulaator!", 96, 330, 200, 100, (44,86,150), (64,106,170), zolk_sõdalane)
        nupp(aken, "V klub", 392, 330, 200, 100, (255,154,19), (255,174,39), oleg_sõdalane)
        nupp(aken, "3rd Reich", 688 , 330, 200, 100, (254,184,198), (255,204,218), ott_sõdalane)
        nupp(aken, "Nnnnnnoh!", 984, 330, 200, 100, (205,3,0), (235,3,0), hennoste_sõdalane)
        nupp(aken, "Deus Vult!", 96, 460, 200, 100, (150,150,150), (250,250,250), esimene_sõdalane)
        nupp(aken, "Tahan olla camo!", 392, 460, 200, 100, (112,130,56), (162,180,106), teine_sõdalane)
        nupp(aken, "Vidi vini vici", 688, 460, 200, 100, (80,5,94), (130,55,144), kolmas_sõdalane)
        a1 = randint(0,255)
        a2 = randint(0,255)
        a3 = randint(0,255)
        nupp(aken, "krdi lõng, aja juuksed maha", 984, 460, 200, 100, (a1, a2, a3), (250,250,250), lõngus_sõdalane)
        
        pg.display.update()
        

def sõdalane_valitud():
    global valin_sõdalane
    valin_sõdalane = False
    
def esimene_sõdalane():
    global tegelane_pilt_menüüs
    Player.kangelane_värv = (255,255,255)
    Player.kangelane_nimi = "Jeesus Kristus"
    Player.kangelane_pilt = jeesus
    tegelane_pilt_menüüs = jeesus1
        
def teine_sõdalane():
    global tegelane_pilt_menüüs
    Player.kangelane_värv = (112,130,56)
    Player.kangelane_nimi = "al-Assad"
    Player.kangelane_pilt = al_assad
    tegelane_pilt_menüüs = al_assad1

def kolmas_sõdalane():
    global tegelane_pilt_menüüs
    Player.kangelane_värv = (80,5,94)
    Player.kangelane_nimi = "Julius Caesar"
    Player.kangelane_pilt = Julius
    tegelane_pilt_menüüs = Julius1
    
def zolk_sõdalane():
    global tegelane_pilt_menüüs
    Player.kangelane_värv = (44,86,150)
    Player.kangelane_nimi = "Indrek Zolk"
    Player.kangelane_pilt = zolk
    tegelane_pilt_menüüs = zolk1
    
def oleg_sõdalane():
    global tegelane_pilt_menüüs
    Player.kangelane_värv = (255,154,19)
    Player.kangelane_nimi = "Oleg Košik"
    Player.kangelane_pilt = oleg
    tegelane_pilt_menüüs = oleg1
    
def ott_sõdalane():
    global tegelane_pilt_menüüs
    Player.kangelane_värv = (254,184,198)
    Player.kangelane_nimi = "Ott-Kaarel"
    Player.kangelane_pilt = ott
    tegelane_pilt_menüüs = ott1
    
def hennoste_sõdalane():
    global tegelane_pilt_menüüs
    Player.kangelane_värv = (205,3,0)
    Player.kangelane_nimi = "Hennoste"
    Player.kangelane_pilt = hennoste
    tegelane_pilt_menüüs = hennoste1

def lõngus_sõdalane():
    global tegelane_pilt_menüüs
    Player.kangelane_värv = (255, 0, 128)
    Player.kangelane_nimi = "lõngus"
    Player.kangelane_pilt = lõngus
    tegelane_pilt_menüüs = lõngus1