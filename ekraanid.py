from põrand import *
from vastased import *
from player_lisad import *
import maailm

def screenide_loomine():
    return {
        -1:[],
        0:[Põrand(100,200,400),Põrand(700,850,400),Põrand(750+400,800+400,250)],
        1:[Põrand(10+400,800+400,250),Põrand(100,400,400),Põrand(700,720,600)],
        2:[],
        3:[Põrand(0,1280,720),Põrand(938,975,288),Põrand(975,1136,288),Põrand(1120,1136,327),Põrand(749,786,290),Põrand(588,749,290),Põrand(588,604,327),Põrand(191,228,288),Põrand(228,389,288),Põrand(373,389,327)],
        4:[Põrand(0,1280,500),Põrand(194,1081,396),Põrand(341,991,303),Põrand(513,904,217),Põrand(618,818,136)]


        }

def vastaste_loomine():
    return {
        -1:[Vampiir(200, 500, 75, 50, 5, 8, 3, (200,0,0), 300, 0.1), Preester(100, 500, 50, 50, 4, 2, 1, (50,50,50), 2, 3, 0.5)],
        0:[Jälitaja(400, 500, 40, 40, 5, 10, 1,(0,0,200)), Zombie(860, 500, 60, 40, 3, 10, 5, (0,150,0), 280)],
        1:[Jälitaja(900, 250, 40, 40, 6, 20, 1,(0,0,200))],
        2:[Lind(700, 100, 50, 50, 6, 10, 1, (200,200,200), 400, 5, 200)]
        }

def itemite_loomine():
    return {0:[Item(120, 395, 20, 20, maailm.kasukas, "Sa leidsid rõivaid!", (200,200,0))],
            1:[Item(410, 245, 30, 50, maailm.railgun, "Sa leidsid relva!", (191,0,255))]
            }