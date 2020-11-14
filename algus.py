import maailm
import pygame as pg
from pygame_init import *
from abi import *
from player import *

mitmes_kord = 0

dirr = os.path.dirname(os.path.abspath(__file__))
piltdir = dirr+"/pildid"

def intro():
    global mitmes_kord
    mitmes_kord += 1
    if mitmes_kord == 1:
        global intromus

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
        
        nupp(aken, "Minek!",laius/2-100, 300, 200, 100, (155,114,98), (185,144,128), maailm.main_loop)
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
    global piltdir
    Player.kangelane_värv = (255,255,255)
    Player.kangelane_nimi = "Jeesus Kristus"
    Player.kangelane_pilt = pg.image.load(piltdir+"/jesus.png")
        
def teine_sõdalane():
    Player.kangelane_värv = (112,130,56)
    Player.kangelane_nimi = "al-Assad"
    Player.kangelane_pilt = pg.image.load(piltdir+"/bashar.png")

def kolmas_sõdalane():
    Player.kangelane_värv = (80,5,94)
    Player.kangelane_nimi = "Julius Caesar"
    Player.kangelane_pilt = pg.image.load(piltdir+"/JC_120x120.png")