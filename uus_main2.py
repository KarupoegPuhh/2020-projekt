import pygame as pg
import sys
pg.init()


laius = 1280
kõrgus = 720
aken = pg.display.set_mode((laius, kõrgus))
pg.display.set_caption('D-day')
pg.display.flip()

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
        
def nupp(text, x, y, laius, kõrgus, värv_tuhm, värv_hele, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    
    largeText = pg.font.Font("freesansbold.ttf", 70)
    smallText = pg.font.Font("freesansbold.ttf", 20)
        
    
    
    if x + laius > mouse[0] > x and y + kõrgus > mouse[1] > y:
        pg.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
        pg.draw.rect(aken, värv_hele, (x-5, y-5, laius, kõrgus))
        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x+x+laius)//2, (y+y+kõrgus)//2)
    aken.blit(textSurf, textRect)

def intro():
    intro = True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        aken.fill((70,70,70))
        
        #Teksdi suurused
        largeText = pg.font.Font("freesansbold.ttf", 155)
        smallText = pg.font.Font("freesansbold.ttf", 20)
         
        TextSurf, TextRect = text_objects("D-day", largeText)
        TextRect.center = ((laius // 2), (170))
        aken.blit(TextSurf, TextRect)
        
       
        
        def nupp(text, x, y, laius, kõrgus, värv_tuhm, värv_hele, action=None):
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            
            
            
            if x + laius > mouse[0] > x and y + kõrgus > mouse[1] > y:
                pg.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
                pg.draw.rect(aken, värv_hele, (x-5, y-5, laius, kõrgus))
                if click[0] == 1 and action != None:
                    action()
            else:
                pg.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
            textSurf, textRect = text_objects(text, smallText)
            textRect.center = ((x+x+laius)//2, (y+y+kõrgus)//2)
            aken.blit(textSurf, textRect)
        
        nupp("minek",laius/3-100, 300, 200, 100, (0,100,0), (0,255,0), main_loop)
        nupp("Vali oma sõdalane", laius/2-100, 300, 200, 100, (100,100,0), (255,255,0))
        nupp("annan alla", laius-laius/3-100, 300, 200, 100, (100,0,0), (255,0,0), quit)
        
        
        
        pg.display.update()

def main_loop():
    global pause
    
    class Player:
        def __init__(self, x, y, laius, pikkus):
            self.x = x
            self.y = y
            self.laius = laius
            self.pikkus = pikkus
            self.värv = (0, 255, 0)
            self.vaatab = 1
            self.hitbox = (self.x-1, self.y-1, self.laius+2, self.pikkus+2)
            self.jump = False
            self.kukub = True
            self.m = 1
            self.vel = 10
            self.vh = 10 #hüppe vel
            #self.dt = 1
            
        def draw(self, aken):
            self.hitbox = (self.x-1, self.y-1, self.laius+2, self.pikkus+2)
            pg.draw.rect(aken, (255,0,0), self.hitbox, 1)
            pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.pikkus))

    class Kuul:
        def __init__(self, x, y, suund):
            self.x = x
            self.y = y
            self.raadius = 5
            self.värv = (255, 0, 0)
            self.vel = 30*suund
            
        def draw(self, aken):
            pg.draw.circle(aken, self.värv, (self.x , self.y), self.raadius)

    class Vastane:
        def __init__(self, x, y, lõpp, vel, health):
            self.x = x
            self.y = y
            self.lõpp = lõpp
            self.path = [self.x, self.lõpp]
            self.vel = vel
            self.laius = 20
            self.pikkus = 60
            self.värv = (0, 255, 255)
            self.hitbox = (self.x -1, self.y -1, self.laius+2, self.pikkus+2)
            self.health = health
            self.max_health = health
            self.elus = True
            
        def move(self):
            if self.vel > 0:
                if self.vel + self.x < self.path[1]:
                    self.x += self.vel*dt
                else:
                    self.vel = -self.vel*dt
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel*dt
                else:
                    self.vel = -self.vel*dt
                    
        def draw(self, aken):
            if self.elus:
                self.move()
                pg.draw.rect(aken, (255,0,0),(self.x, self.y-15, self.laius, 10))
                pg.draw.rect(aken, (0,255,0),(self.x, self.y-15, self.health * (self.laius // self.max_health), 10))
                self.hitbox = (self.x -1, self.y -1, self.laius+2, self.pikkus+2)             
                pg.draw.rect(aken, (255,0,0), self.hitbox, 1)
                pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.pikkus))

        def hit(self):
            if self.health > 1:
                self.health -= 1
            else:
                self.elus = False
            print("hit!")

    class põrand:
        instances = []
        
        def __init__(self,x1,x2,y):
            self.__class__.instances.append(self)

            self.y = y
            self.x1 = x1
            self.x2 = x2
        
        def draw(self, aken):
            pg.draw.line(aken, (255, 0, 0), (self.x1,self.y),(self.x2,self.y))
            #seinad
            pg.draw.line(aken, (255, 0, 0), (self.x1,self.y),(self.x1,kõrgus))
            pg.draw.line(aken, (255, 0, 0), (self.x2,self.y),(self.x2,kõrgus))


    def unpause():
        global pause
        pause = False
    
    def paused():
        
        while pause:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                    
            aken.fill((70,70,70))
            largeText = pg.font.Font("freesansbold.ttf", 70)
            TextSurf, TextRect = text_objects("Tõmban hinge", largeText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            
        
            nupp("Jätkan!", 100, 300, 200, 100, (0,100,0), (0,255,0), unpause)
            nupp("Annan alla", 400, 300, 200, 100, (100,100,0), (255,255,0), quit)
            
            pg.display.update()
    
    def redrawGameWindow():
        aken.fill((0,0,0))
        
        põrand1.draw(aken)
        #põrand2.draw(aken)
        plat.draw(aken)

        Tom.draw(aken)
        paha.draw(aken)
        paha1.draw(aken)
        for kuul in kuulid:
            kuul.draw(aken)
        
        pg.display.update()
        dt = clock.tick(30)
    
    def pole_sein_v(v,x,y,lai,pikk,umb=0,obj=põrand):
        #pole window vasak äär
        if v < 0:
            v = -v
        if v*dt < x:
            #seinad vasakule minnes
            for i in obj.instances:
                if x <= i.x2+(v*dt)+umb and x > i.x2 + 1-umb and not y < i.y - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                    return False
            return True
        return False

    def pole_sein_p(v,x,y,lai,pikk,umb=0,obj=põrand):
        #pole window parem äär
        if v*dt < (laius - x - lai):
            #seinad paremale minnes
            for i in obj.instances:
                if x+lai+(v*dt) >= i.x1 and x+lai < i.x1 + 1 and not y < i.y - pikk: #not v*dt < (i.x1 - x - lai) or y < i.y - pikk:
                    return False
            return True
        return False

    def maa_kõrgus(px,lai,obj=põrand):
        global mk
        eelm_mk = mk
        y = []
        for i in obj.instances:
            if px >= i.x1-lai and px <= i.x2:
                #print(i.x1)
                #print(px+lai)
                #print(px)
                #print(i.x2)
                y.append(i.y)

        if not y:
            mk = eelm_mk
        else:
            mk = (min(y))
    
    #VARS
    if True: #et saaks collapsida

        põrand1 = põrand(0,laius,500)#(0,600,500)
        #põrand2 = põrand(700,laius,500)
        plat = põrand(600,700,400)

        Tom = Player(900, 100, 40, 60)
        #Tom.y = põrand1.y-Tom.pikkus
        vh = Tom.vh
        Tom.vh = 0
        kuul = Kuul(laius + Tom.x // 2, kõrgus + Tom.y // 2, Tom.vaatab)
        paha = Vastane(400, 0, 500, 5, 10)
        paha.y = põrand1.y-paha.pikkus
        paha1 = Vastane(100, 0, 400, 15, 2)
        paha1.y = põrand1.y-paha1.pikkus

        kuulid = []
        kuulide_cd = 0
        kuulide_cd_const = 10
        kuulide_maxcount = 5

        pause = False
        running = True
        clock = pg.time.Clock()
        global dt
        dt = 1
        global mk #maa kõrgus (suurem arv = madalam kõrgus)
        mk = 500
        global eelmine_mk
        eelmine_mk = 500
    
    while running:
        #exit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        #KUULID
        if True: #lihtsalt et saaks collapsida seda
            if kuulide_cd > 0:
                kuulide_cd += 1
            if kuulide_cd > kuulide_cd_const:
                kuulide_cd = 0
            for kuul in kuulid:
                #Paha tulistamine
                if kuul.y - kuul.raadius < paha.hitbox[1] + paha.hitbox[3] and kuul.y + kuul.raadius > paha.hitbox[1] and paha.elus:
                    if kuul.x - kuul.raadius < paha.hitbox[0] + paha.hitbox[2] and kuul.x + kuul.raadius > paha.hitbox[0]:
                        kuulid.pop(kuulid.index(kuul))
                        paha.hit()
                #Paha1 tulistamine
                if kuul.y - kuul.raadius < paha1.hitbox[1] + paha1.hitbox[3] and kuul.y + kuul.raadius > paha1.hitbox[1] and paha1.elus:
                    if kuul.x - kuul.raadius < paha1.hitbox[0] + paha1.hitbox[2] and kuul.x + kuul.raadius > paha1.hitbox[0]:
                        kuulid.pop(kuulid.index(kuul))
                        paha1.hit()
                #sein
                if not pole_sein_v(kuul.vel,kuul.x,kuul.y,0,0,5):
                    if kuul in kuulid:
                        kuulid.pop(kuulid.index(kuul))
                if not pole_sein_p(kuul.vel,kuul.x,kuul.y,0,0,5):
                    if kuul in kuulid:
                        kuulid.pop(kuulid.index(kuul))
                #liikumine
                if kuul.x < Tom.x + 500 and kuul.x > Tom.x - 500:
                    kuul.x += kuul.vel*dt  # Moves the kuul by its vel
                else:
                    if kuul in kuulid:
                        kuulid.pop(kuulid.index(kuul))
        
        keys = pg.key.get_pressed()
        
        eelmine_mk = mk
        maa_kõrgus(Tom.x,Tom.laius)
        # TOM PAREMALE JA VASAKULE      
        if keys [pg.K_d] and pole_sein_p(Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
            Tom.x += Tom.vel*dt
            Tom.vaatab = 1
        if keys [pg.K_a] and pole_sein_v(Tom.vel,Tom.x,Tom.y,Tom.laius,Tom.pikkus):
            Tom.x -= Tom.vel*dt
            Tom.vaatab = -1
        
        # TOM HÜPPAMINE
        if not Tom.jump:
            if keys [pg.K_w]:
                Tom.jump = True
        if Tom.jump:
            #F = 1 / 2 * mass * velocity ^ 2
            if Tom.vh > 0:
                F = (0.5*Tom.m*(Tom.vh**2)) #/2
            else:
                F = -(0.5*Tom.m*(Tom.vh**2)) #/2
            
            Tom.y -= F*dt

            Tom.vh -= 1 
            
            if Tom.y+Tom.pikkus >= mk:
                Tom.y = mk-Tom.pikkus
                Tom.jump = False
                Tom.vh = vh
        
        #tom kukkumine
        if mk > eelmine_mk and not Tom.jump:
            Tom.kukub = True
            Tom.vh = 0
        if Tom.kukub:
            F = -(0.5*Tom.m*(Tom.vh**2)) #/2
            Tom.y -= F*dt
            Tom.vh -= 1
            if Tom.y+Tom.pikkus >= mk:
                Tom.y = mk-Tom.pikkus
                Tom.kukub = False
                Tom.vh = vh

            
        
        #TULISTAMINE
        
        if keys[pg.K_SPACE] and kuulide_cd == 0:
            if Tom.vaatab == 1:
                suund = 1
            else:
                suund = -1

            if len(kuulid) < kuulide_maxcount:  # This will make sure we cannot exceed 5 bullets on the screen at once
                kuulid.append(Kuul(round(Tom.x+Tom.laius//2+suund*Tom.laius/2), round(Tom.y + Tom.pikkus//2), suund))
            
            kuulide_cd = 1
        
        #PAUSE MENU
        if keys[pg.K_p]:
            pause = True
            paused()
                
            
        redrawGameWindow()

while True:
    intro()
    main_loop()