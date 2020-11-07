import pygame as pg
import sys

class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def update():
    global jump
    global jumpCount
    global p_x
    global p_y
    #PLAYER
    #movement
    keys = pg.key.get_pressed()  
    if keys [pg.K_d] and p_vel < (aken_laius - p_x - p_laius):
        p_x += 5
    if keys [pg.K_a] and p_vel < p_x:
        p_x -= 5
    if not jump:
        if keys [pg.K_SPACE]:
            jump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            p_y -= jumpCount ** 2 * 0.5 * neg
            jumpCount -= 1
        else:
            jump = False
            jumpCount = 10
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

dt = 1

#TEGELANE
p_laius = 40
p_kõrgus = 60
p_col = (0, 255, 0)
p_x = 200
p_y = 200
p_vel = 5

jumpCount = 10
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