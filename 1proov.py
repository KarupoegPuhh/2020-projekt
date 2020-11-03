import pygame as pg
pg.init()

aken = pg.display.set_mode((900,600))
pg.display.set_caption("PRÖÖV")
x = 0
y = 500
speed = 1
jumping = False
airtime = 10
loop = True

while loop:
    pg.time.delay(100)

    keys = pg.key.get_pressed()
    if not jumping:
        if keys[pg.K_UP]:
            jumping = True
    else:
        if airtime >= -10:
            if airtime < 0:
                y += (airtime**2)*0.5
            else:
                y -= (airtime ** 2) * 0.5
            airtime -= 1
        else:
            jumping = False
            airtime = 10
    if keys[pg.K_RIGHT]:
        x += speed
    if keys[pg.K_LEFT]:
        x -= speed

    aken.fill((0,0,0))
    pg.draw.rect(aken,(0,200,0),(x,y,50,50))
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False

pg.quit()