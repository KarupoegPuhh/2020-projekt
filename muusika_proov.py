import pygame as pg
pg.init()

pg.display.set_mode((200,100))

pg.mixer.music.load("1304215180.mp3")
pg.mixer.music.play(-1)
pause = False
pos = 0
start = 0

while True:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    keys = pg.key.get_pressed()

    if not pause:
        if keys[pg.K_p]:
            pause = True
            pos = pg.mixer.music.get_pos()
            pg.mixer.music.stop()
            pg.mixer.music.load("filt.mp3")
            start = start + pos/1000.0
            pg.mixer.music.play(-1, start)
    else:
        if keys[pg.K_p]:
            pause = False
            pos = pg.mixer.music.get_pos()
            pg.mixer.music.stop()
            pg.mixer.music.load("1304215180.mp3")
            start = start + pos/1000.0
            pg.mixer.music.play(-1, start)

