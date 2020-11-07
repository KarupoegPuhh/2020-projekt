import pygame as pg
import sys


def update():
    global jump
    global p_m
    global p_v
    global p_x
    global p_y
    global dt
    global p_speed
    #PLAYER
    #movement
    keys = pg.key.get_pressed()  
    if keys [pg.K_d] and p_vel < (aken_laius - p_x - p_laius) and (p_vel < (sein1[1][0] - p_x - p_laius) or p_y < sein1[2][1]-p_kõrgus):
        p_x += p_speed*dt
    if keys [pg.K_a] and p_vel < p_x:
        p_x -= p_speed*dt
    #hüppamine
    if not jump:
        if keys [pg.K_SPACE]:
            jump = True
    if jump: 
        #F = 1 / 2 * mass * velocity ^ 2
        if p_v > 0:
            F = (0.5*p_m*(p_v**2)) #/2
        else:
            F = -(0.5*p_m*(p_v**2)) #/2
        
        p_y -= F*dt

        p_v -= 1 
        
        if p_y >= 500:
            p_y = 500
            jump = False
            p_v = 10
    #seinad


def draw():
    #TAUST
    bg.fill(aken_taust)

    pg.draw.line(bg, (255, 0, 0), põrand[1],põrand[2])
    pg.draw.line(bg, (255, 0, 0), sein1[1],sein1[2])
    pg.draw.line(bg, (255, 0, 0), sein2[1],sein2[2])
    
    #PLAYER
    pg.draw.rect(bg, p_col, (p_x, p_y, p_laius, p_kõrgus))
    

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
p_y = 500
p_vel = 5
p_speed = 10

p_m = 1 #mass
p_v = 10 #velocity (hüppamisele)
jump = False

#SEINAD
põrand = {1:(0,500+p_kõrgus),2:(aken_laius,500+p_kõrgus)}
sein1 = {1:(600,500+p_kõrgus),2:(600,500)}
sein2 = {1:(605,500+p_kõrgus),2:(605,500)}

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