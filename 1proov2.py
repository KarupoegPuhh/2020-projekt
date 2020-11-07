import pygame as py
import sys


width = 800
height = 400
bg = pg.image.load("/Users/anetteandresoo/Documents/Proge/Kodutööd/Mängud/Projekt/Pildid/bg.jpg")
bg = pg.transform.scale(bg, (width, height))
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Platformer")
clock = pg.time.Clock()
pg.init()

#tegelane
char_width = 40
char_height = 60
char_col = (255, 0, 0)
char_x = 200
char_y = 200
vel = 5
char = pg.image.load("/Users/anetteandresoo/Documents/Proge/Kodutööd/Mängud/Projekt/Pildid/char.png")
char = pg.transform.scale(char, (64, 64))

jumpCount = 10
jump = False
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    keys = pg.key.get_pressed()
    
    if keys [pg.K_d] and vel < (width - char_x - char_width):
        char_x += 5
    if keys [pg.K_a] and vel < char_x:
        char_x -= 5
    if not jump:
        if keys [pg.K_SPACE]:
                jump = True
    else:
        if jumpCount >= -10:
            neg = 1
        if jumpCount < 0:
            neg = -1
            char_y -= jumpCount ** 2 * 0.5 * neg
            jumpCount -= 1
        else:
            jump = False
            jumpCount = 10
            
screen.fill((0, 0, 0))
screen.blit(bg, (0, 0))
screen.blit(char,(char_x, char_y))
#pg.draw.rect(screen, char_col, (char_x, char_y, char_width, char_height))
pg.display.update()
clock.tick(60)
    
    
quit()