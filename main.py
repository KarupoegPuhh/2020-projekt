import pygame as pg
import sys
from blocks import *
import os

#PLATFORM
#https://opensource.com/article/18/7/put-platforms-python-game

class Platform(pg.sprite.Sprite):
    def __init__(self, plat_x, plat_y, img_w, img_h, img):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.y = plat_y
        self.rect.x = plat_x


def update():
    global jump
    global p_m
    global p_v
    global F
    global p_x
    global p_y
    global dt
    #PLAYER
    #movement
    keys = pg.key.get_pressed()  
    if keys [pg.K_d] and p_vel < (aken_laius - p_x - p_laius):
        p_x += 5*dt
    if keys [pg.K_a] and p_vel < p_x:
        p_x -= 5*dt
    if not jump:
        if keys [pg.K_SPACE]:
            jump = True
    if jump: 
        # F = 1 / 2 * mass * velocity ^ 2
        p_y -= (1 / 2)*m*(v**2)
           
        # decreasing velocity while going up and become negative while coming down 
        v = v-1
           
        # object reached its maximum height 
        if v < 0: 
               
            # negative sign is added to counter negative velocity 
            m =-1
    #fps
    dt = clock.tick(60)


def draw():
    #TAUST
    bg.fill(aken_taust)
    #PLAYER
    p = pg.draw.rect(bg, p_col, (p_x, p_y, p_laius, p_kõrgus))

    #UPDATE
    pg.display.flip()
    #pg.display.update()

aken_laius = 1280
aken_pikkus = 720
aken_taust = (0,0,0)

bg = pg.display.set_mode((aken_laius, aken_pikkus))
pg.display.set_caption('D-day')

clock = pg.time.Clock()
dt = 1

esimene_korrus = Platform(0, 660, 500, 60, "./esimene_korrus.png")

#TEGELANE
p_laius = 40
p_kõrgus = 60
p_col = (0, 255, 0)
p_x = 200
p_y = 200
p_vel = 5

p_m = 1 #mass
p_v = 5 #velocity (hüppamisele)
jump = False

#KUUL
k_raadius = 10
k_col = (255, 0, 0)
#_x =
#k_y = 
k_vel = 15







loop = True
while loop:
    #AKNA SULGEMINE
    for event in pg.event.get():
        if event.type == pg.QUIT: #or esc
            loop = False
    #MAIN LOOP
    update()
    #DRAW LOOP
    draw()
    #clock
pg.quit()