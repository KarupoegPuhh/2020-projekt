import pygame
import sys
pygame.init()


laius = 1000
kõrgus = 500
aken = pygame.display.set_mode((laius, kõrgus))
pygame.display.set_caption('D-day')
pygame.display.flip()

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
        
def nupp(text, x, y, laius, kõrgus, värv_tuhm, värv_hele, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    largeText = pygame.font.Font("freesansbold.ttf", 70)
    smallText = pygame.font.Font("freesansbold.ttf", 20)
        
    
    
    if x + laius > mouse[0] > x and y + kõrgus > mouse[1] > y:
        pygame.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
        pygame.draw.rect(aken, värv_hele, (x-5, y-5, laius, kõrgus))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x+x+laius)//2, (y+y+kõrgus)//2)
    aken.blit(textSurf, textRect)
    

        
def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        aken.fill((70,70,70))
        
        #Teksdi suurused
        largeText = pygame.font.Font("freesansbold.ttf", 155)
        smallText = pygame.font.Font("freesansbold.ttf", 20)
         
        TextSurf, TextRect = text_objects("D-day", largeText)
        TextRect.center = ((laius // 2), (170))
        aken.blit(TextSurf, TextRect)
        
       
        
        def nupp(text, x, y, laius, kõrgus, värv_tuhm, värv_hele, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            
            
            if x + laius > mouse[0] > x and y + kõrgus > mouse[1] > y:
                pygame.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
                pygame.draw.rect(aken, värv_hele, (x-5, y-5, laius, kõrgus))
                if click[0] == 1 and action != None:
                    action()
            else:
                pygame.draw.rect(aken, värv_tuhm, (x, y, laius, kõrgus))
            textSurf, textRect = text_objects(text, smallText)
            textRect.center = ((x+x+laius)//2, (y+y+kõrgus)//2)
            aken.blit(textSurf, textRect)
        
        nupp("minek", 100, 300, 200, 100, (0,100,0), (0,255,0), main_loop)
        nupp("Vali oma sõdalane", 400, 300, 200, 100, (100,100,0), (255,255,0))
        nupp("annan alla", 700, 300, 200, 100, (100,0,0), (255,0,0), quit)
        
        
        
        pygame.display.update()
        
def main_loop():
    global pause
    
    def unpause():
        global pause
        pause = False
    
    def paused():
        
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            aken.fill((70,70,70))
            largeText = pygame.font.Font("freesansbold.ttf", 70)
            TextSurf, TextRect = text_objects("Tõmban hinge", largeText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            
        
            nupp("Jätkan!", 100, 300, 200, 100, (0,100,0), (0,255,0), unpause)
            nupp("Annan alla", 400, 300, 200, 100, (100,100,0), (255,255,0), quit)
            
            pygame.display.update()
    
    def redrawGameWindow():
        aken.fill((0,0,0))
        Tom.draw(aken)
        paha.draw(aken)
        paha1.draw(aken)
        for kuul in kuulid:
            kuul.draw(aken)
        pygame.display.update()
        

        

    class Player:
        def __init__(self, x, y, laius, kõrgus):
            self.x = x
            self.y = y
            self.laius = laius
            self.kõrgus = kõrgus
            self.vel = 20
            self.värv = (0, 255, 0)
            self.vaatab = 0
            self.hitbox = (self.x-1, self.y-1, 27, 27)
            self.jump = False
            self.m = 1
            self.v = 8
            self.dt = 1
            
        def draw(self, aken):
            self.hitbox = (self.x-1, self.y-1, 27, 27)
            pygame.draw.rect(aken, (255,0,0), self.hitbox, 2)
            pygame.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.kõrgus))

    class Kuul:
        def __init__(self, x, y, suund):
            self.x = x
            self.y = y
            self.raadius = 5
            self.värv = (255, 0, 0)
            self.vel = 30 * suund
            
        def draw(self, aken):
            pygame.draw.circle(aken, self.värv, (self.x , self.y), self.raadius)

    class Vastane:
        def __init__(self, x, y, lõpp, vel, health):
            self.x = x
            self.y = y
            self.lõpp = lõpp
            self.path = [self.x, self.lõpp]
            self.vel = vel
            self.laius = 20
            self.kõrgus = 20
            self.värv = (0, 255, 255)
            self.hitbox = (self.x -1, self.y -1, 22, 22)
            self.health = health
            self.max_health = health
            self.elus = True
            
        def move(self):
            if self.vel > 0:
                if self.vel + self.x < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    
        def draw(self, aken):
            if self.elus:
                self.move()
                pygame.draw.rect(aken, (255,0,0),(self.x, self.y-15, self.laius, 10))
                pygame.draw.rect(aken, (0,255,0),(self.x, self.y-15, self.health * (self.laius // self.max_health), 10))
                self.hitbox = (self.x -1, self.y -1, 22, 22)
                pygame.draw.rect(aken, (255,0,0), self.hitbox, 1)
                pygame.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.kõrgus))

        def hit(self):
            if self.health > 1:
                self.health -= 1
            else:
                self.elus = False
            print("hit!")
            
    Tom = Player(10, 200, 25, 25)
    kuul = Kuul(laius + Tom.x // 2, kõrgus + Tom.y // 2, Tom.vaatab)
    paha = Vastane(400, 200, 500, 5, 10)
    paha1 = Vastane(100, 200, 400, 15, 2)

    pause = False   
    kuulid = []
    kuulide_cd = 0
    running = True
    kuulide_cd_const = 10
    kuulide_maxcount = 5
    while running:
        pygame.time.delay(15)
        
        #KUULID
        if kuulide_cd > 0:
            kuulide_cd += 1
        if kuulide_cd > kuulide_cd_const:
            kuulide_cd = 0
        for kuul in kuulid:
            #Paha tulistamine
            if kuul.y - kuul.raadius < paha.hitbox[1] + paha.hitbox[3] and kuul.y + kuul.raadius > paha.hitbox[1] and paha.elus == True:
                if kuul.x - kuul.raadius < paha.hitbox[0] + paha.hitbox[2] and kuul.x + kuul.raadius > paha.hitbox[0]:
                    kuulid.pop(kuulid.index(kuul))
                    paha.hit()
            #Paha1 tulistamine
            if kuul.y - kuul.raadius < paha1.hitbox[1] + paha1.hitbox[3] and kuul.y + kuul.raadius > paha1.hitbox[1] and paha1.elus == True:
                if kuul.x - kuul.raadius < paha1.hitbox[0] + paha1.hitbox[2] and kuul.x + kuul.raadius > paha1.hitbox[0]:
                    kuulid.pop(kuulid.index(kuul))
                    paha1.hit()
            if kuul.x < Tom.x + 500 and kuul.x > Tom.x - 500:
                kuul.x += kuul.vel  # Moves the kuul by its vel
            else:
                kuulid.pop(kuulid.index(kuul))
                
                
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        
        keys = pygame.key.get_pressed()
        
        #PAREMALE JA VASAKULE      
        if keys [pygame.K_d] and Tom.vel < (laius - Tom.x - Tom.laius):
            Tom.x += Tom.vel
            Tom.vaatab = 1
        if keys [pygame.K_a] and Tom.vel < Tom.x:
            Tom.x -= Tom.vel
            Tom.vaatab = -1
            
        #HÜPPAMINE
        if not Tom.jump:
            if keys [pygame.K_w]:
                Tom.jump = True
                v_vaheväärtus = Tom.v
        if Tom.jump: 
            #F = 1 / 2 * mass * velocity ^ 2
            Tom.y -= ((1 / 2)*Tom.m*(Tom.v**2))*Tom.dt
 
            Tom.v = Tom.v-1
            if Tom.v < 0: 
 
                Tom.m =-1
            if Tom.v == - (v_vaheväärtus + 1):
                Tom.jump = False
                Tom.m = 1
                Tom.v = -(Tom.v + 1)
            
        
        #TULISTAMINE
        
        if keys[pygame.K_SPACE] and kuulide_cd == 0:
            if Tom.vaatab == 1:
                suund = 1
            else:
                suund = -1

            if len(kuulid) < kuulide_maxcount:  # This will make sure we cannot exceed 5 bullets on the screen at once
                kuulid.append(Kuul(round(Tom.x+Tom.laius//2), round(Tom.y + Tom.kõrgus//2), suund))
            
            kuulide_cd = 1
        
        #PAUSE MENU
        if keys[pygame.K_p]:
            pause = True
            paused()
           
       # This will create a bullet starting at the middle of the character
                
            
        redrawGameWindow()

while True:
    intro()
    main_loop()
