 #TEGELANE SAAB PIHTA
    #läheb main_loopi, kui vastane läheb sulle pihta saad knockback ja kaotad elud
        if Tom.hitbox[1] < paha.hitbox[1] + paha.hitbox[3] and Tom.hitbox[1] + Tom.hitbox[3] > paha.hitbox[1] and paha.elus == True:
            if Tom.hitbox[0] < paha.hitbox[0] + paha.hitbox[2] and Tom.hitbox[0] + Tom.hitbox[2] > paha.hitbox[0]:
                Tom.hit()
                
# läheb class Player alla                
def hit(self):
            if self.health > 1:
                self.health -= 1
                self.x -= 20
            else:
                self.elus = False
                surm()
                
 # Player muutujad               
            self.health = 10
            self.max_health = 10
            self.elus = True
            
            
#uus player def draw(self).   healtbari jaoks

def draw(self, aken):
            
            pygame.draw.rect(aken, (255,0,0),(self.x, self.y-15, self.laius, 10))
            pygame.draw.rect(aken, (0,255,0),(self.x, self.y-15, self.health * (self.laius / self.max_health) , 10))
            self.hitbox = (self.x-1, self.y-1, self.laius+2, self.pikkus+2)
            pg.draw.rect(aken, (255,0,0), self.hitbox, 1)
            pg.draw.rect(aken, self.värv, (self.x, self.y, self.laius, self.pikkus))
            
            
            
#algusesse, kus defineerime funktsioone, (kui tegelane saab surma) kutsutakse välja player.hit() sees
def surm():
        surm = True
        while surm:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            aken.fill((70,70,70))
            
            #Teksdi suurused
            largeText = pygame.font.Font("freesansbold.ttf", 70)
            smallText = pygame.font.Font("freesansbold.ttf", 20)
             
            TextSurf, TextRect = text_objects("Sa hukkusid oma rännakul...", largeText)
            TextRect.center = ((laius // 2), (170))
            aken.blit(TextSurf, TextRect)
            
            nupp("Annan alla", 400, 375, 200, 100, (100,0,0), (255,0,0), quit)
            nupp("Proovin uuesti", 400, 250, 200, 100, (0,100,0), (0,255,0), main_loop)
            
            pygame.display.update()
            
