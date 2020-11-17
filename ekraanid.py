from põrand import *
from vastased import *
from player_lisad import *
import maailm

def screenide_loomine():
    return {0:{#korrus
        -1:[Põrand(-18,1296,500,743)],
        0:[Põrand(-17,1296,500,738),Põrand(394,556,438,500),Põrand(0,59,0,360)],
        1:[Põrand(-23,1296,500,740)],
        2:[Põrand(0,1280,500,720),Põrand(818,1112,0,37),Põrand(194,1081,396,500),Põrand(341,991,303,396),Põrand(513,904,217,303),Põrand(618,818,136,217)],
        3:[Põrand(153,224,432,503),Põrand(506,576,424,500),Põrand(826,1213,427,500),Põrand(0,1280,500,720)],
        4:[Põrand(81,168,423,500),Põrand(353,461,409,500),Põrand(933,1037,409,500),Põrand(0,1280,500,720),Põrand(1232,1280,0,500)]
        },
        1:{#korrus
        1:[],
        2:[Põrand(23,50,100,240)]
        }
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