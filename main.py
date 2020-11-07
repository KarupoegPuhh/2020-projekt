import pygame as pg
import sys


def update():
    global jump
    global p_m
    global p_v
    global p_x
    global p_y
    global dt
    global p_nägu
    global k_exists
    global k_x
    global k_vel
    #PLAYER
    #movement
    keys = pg.key.get_pressed()  
    if keys [pg.K_d] and p_vel < (aken_laius - p_x - p_laius):
        p_x += 1*dt
        p_nägu = True
    if keys [pg.K_a] and p_vel < p_x:
        p_x -= 1*dt
        p_nägu = False
    if not jump:
        if keys [pg.K_SPACE]:
            jump = True
    #hüppamine
    if not jump:
        if keys [pg.K_SPACE]:
            jump = True
    if jump: 
        #F = 1 / 2 * mass * velocity ^ 2. source: https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
        p_y -= (((1 / 2)*p_m*(p_v**2))/2)*dt
           
        #decreasing velocity while going up and become negative while coming down 
        p_v = p_v-1
           
        #max kõrgus
        if p_v < 0: 
               
            #negative sign is added to counter negative velocity 
            p_m =-1
        if p_v == -6:
            jump = False
            p_v = 5
            p_m = 1

    #kuul
    if keys [pg.K_m]:
        k_exists = True
        if p_nägu == True:
            k_x += k_vel
        else:
            k_x -= k_vel
        if k_x == p_x + 200 or k_x == p_x -200:
            k_exists = False



def draw():
    #TAUST
    bg.fill(aken_taust)
    #PLAYER
    pg.draw.rect(bg, p_col, (p_x, p_y, p_laius, p_kõrgus))
    #KUUL
    while k_exists == True:
        pg.draw.circle(bg, k_col, (k_x, k_y), k_raadius)

    #UPDATE
    pg.display.flip()
    #fps
    dt = clock.tick(60)
    

aken_laius = 1280
aken_pikkus = 720
aken_taust = (0,0,0)

bg = pg.display.set_mode((aken_laius, aken_pikkus))
pg.display.set_caption('D-day')

clock = pg.time.Clock()
dt = 1


#TEGELANE
p_laius = 40
p_kõrgus = 60
p_col = (0, 255, 0)
p_x = 200
p_y = 200
p_vel = 5
p_nägu = True

p_m = 1 #mass
p_v = 5 #velocity (hüppamisele)
jump = False

#KUUL
k_raadius = 10
k_col = (255, 0, 0)
k_x = p_x + (0.5 * p_laius)
k_y = p_y - (0.5 * p_kõrgus)
k_vel = 15
k_exists = False







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