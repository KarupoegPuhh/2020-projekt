from põrand import *
from vastased import *
from player_lisad import *
import maailm

def screenide_loomine():
    return {
        -1:[],
        0:[Põrand(100,200,400),Põrand(700,850,400),Põrand(750+400,800+400,250)],
        1:[Põrand(10+400,800+400,250),Põrand(100,400,400),Põrand(700,720,600)],
        2:[]
        }

def vastaste_loomine():
    return {
        -1:[Vampiir(200, 500, 75, 50, 5, 8, 3, (200,0,0), 300, 0.1), Preester(100, 500, 50, 50, 4, 2, 1, (50,50,50), 2, 3, 0.5)],
        0:[Jälitaja(400, 500, 40, 40, 5, 10, 1,(0,0,200)), Zombie(860, 500, 60, 40, 3, 10, 5, (0,150,0), 280)],
        1:[Jälitaja(900, 250, 40, 40, 6, 20, 1,(0,0,200))],
        2:[Lind(700, 100, 50, 50, 6, 10, 1, (200,200,200), 400, 5, 200)]
        }

def itemite_loomine():
    print("LÕIN")
    return {0:[Item(120, 350, 50, 50, maailm.kasukas, "Sa leidsid rõivaid!")]}