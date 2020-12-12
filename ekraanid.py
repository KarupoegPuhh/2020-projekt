from põrand import *
from vastased import *
from player_lisad import *
import maailm

def screenide_loomine():
    return {0:{#korrus
            1:[Põrand(-17,1296,500,738),Põrand(394,556,438,500),Põrand(-17,59,-18,360),Põrand(59,1280,-1,0)],
            2:[Põrand(-23,1296,500,740),Põrand(0,1280,-1,0)],
            3:[Põrand(0,1280,500,720),Põrand(820,1114,0,37),Põrand(194,1081,396,500),Põrand(341,991,303,396),Põrand(513,904,217,303),Põrand(618,818,136,217),Põrand(0,643,-1,0),Põrand(1112,1292,-1,0)],
            4:[Põrand(160,231,429,500),Põrand(506,576,424,500),Põrand(826,1213,427,500),Põrand(0,1280,500,720),Põrand(0,1280,-1,0)],
            5:[Põrand(81,168,423,500),Põrand(269,377,409,500),Põrand(933,1037,409,500),Põrand(933,1025,305,409),Põrand(0,1280,500,720),Põrand(1232,1280,0,500),Põrand(0,1280,0,1)],
            0:[Põrand(-18,1296,500,743),Põrand(1220,1296,-22,360)],
            -1:[Põrand(-18,1296,500,743),Põrand(0,1280,-49,-1),Põrand(0,47,174,500),Põrand(47,564,174,247),Põrand(564,614,174,374),Põrand(137,203,454,500),Põrand(-50,-1,0,174)]
        },
        1:{#korrus
            1337:[Põrand(0,36,0,500),Põrand(584,638,-16,344),Põrand(959,1148,305,360),Põrand(638,840,258,313),Põrand(1005,1148,137,192),Põrand(713,878,52,107),Põrand(1148,1280,-7,360),Põrand(36,713,-27,0),Põrand(1021,1280,-27,-1),Põrand(-23,1300,500,735),Põrand(638,713,-7,107)],
            5:[Põrand(0,1280,500,720),Põrand(1204,2280,360,500),Põrand(523,570,0,391),Põrand(290,327,290,360),Põrand(145,290,290,327),Põrand(129,145,290,500),Põrand(0,1280,0,1)],
            4:[Põrand(0,1280,500,720),Põrand(938,975,288,358),Põrand(975,1120,288,327),Põrand(1120,1136,288,500),Põrand(749,786,290,360),Põrand(604,749,290,327),Põrand(588,604,290,500),Põrand(191,228,288,358),Põrand(228,373,288,327),Põrand(373,389,288,500),Põrand(0,1280,0,1),Põrand(-106,40,96,163)],
            3:[Põrand(910,1280,500,720),Põrand(0,640,500,720),Põrand(226,799,300,320),Põrand(1134,1374,96,163),Põrand(0,1280,0,1),Põrand(0,15,-9,351),Põrand(820,1114,712,741)],
            2:[Põrand(-23,1300,500,735),Põrand(0,132,0,360),Põrand(1123,1280,-12,348)],
            1:[Põrand(0, 36, 0, 500), Põrand(584, 638, -16, 344), Trapdoor(853, 1148, 305, 360,maailm.delta_uksed, 200), Põrand(638, 840, 258, 313), Põrand(1005, 1148, 137, 192), Põrand(713, 878, 52, 107), Põrand(1148, 1280, -7, 360), Põrand(36, 713, -27, 0), Põrand(1021, 1280, -27, -1), Põrand(-23, 1300, 500, 735), Põrand(638, 713, -7, 107)],
            6:[Põrand(353,473,505,551),Põrand(1031,1151,505,551),Põrand(845,965,360,406),Põrand(487,607,360,406),Põrand(650,770,213,259),Põrand(-31,96,360,500),Põrand(0,1280,0,1)]
        },
        2:{
            1: [Põrand(1020, 1147, 665, 724), Põrand(0, 713, 501, 784), Põrand(1147, 1349, 501, 784),
                Põrand(714, 1003, 501, 534), Põrand(0, 36, -19, 501), Põrand(594, 714, 360, 501),
                Põrand(172, 363, 233, 273), Põrand(363, 400, 174, 273), Põrand(36, 154, 326, 370),
                Põrand(154, 172, 233, 370), Põrand(4, 1280, -33, -1), Põrand(1147, 1280, -163, 120)],
            2: [Põrand(-56, 133, 501, 784), Põrand(205, 352, 322, 398), Põrand(853, 949, 430, 501),
                Põrand(1125, 1335, 500, 801), Põrand(0, 133, -167, 116), Põrand(1125, 1295, -184, 116),
                Põrand(544, 640, 322, 393)],
            3: [Põrand(-968, 353, 500, 735), Põrand(696, 730, 201, 243), Põrand(565, 696, 219, 243),
                Põrand(550, 565, 115, 243), Põrand(353, 989, 400, 423), Põrand(353, 1326, 640, 720),
                Põrand(487, 1280, 500, 540), Põrand(431, 884, 317, 328), Põrand(884, 925, 115, 328),
                Põrand(317, 353, 93, 758), Põrand(1142, 1280, -14, 500), Põrand(353, 961, 93, 115),
                Põrand(187, 317, 360, 400), Põrand(187, 317, 198, 238), Põrand(0, 1144, -20, -1),
                Põrand(-18, 85, -13, 115)],
            4: [Põrand(223, 1546, 500, 735), Põrand(-107, 223, 640, 720), Põrand(-678, 115, 501, 541),
                Põrand(96, 1183, 298, 360), Põrand(0, 1280, 0, 1), Põrand(-80, 12, -13, 501)],
            5: [Põrand(-111, 1300, 500, 735), Põrand(1233, 1280, 0, 500), Põrand(810, 1233, 417, 500),
                Põrand(1081, 1233, 168, 251), Põrand(919, 1233, 334, 417), Põrand(1009, 1233, 251, 334),
                Põrand(1153, 1233, 85, 168), Põrand(96, 687, 298, 360), Põrand(371, 405, 0, 298), Põrand(0, 1058, 0, 1)],
        },
        3:{
            5:[Põrand(-23,906,500,735),Põrand(906,1054,667,720),Põrand(1233,1280,0,720),Põrand(288,653,338,400),Põrand(0,77,125,500),Põrand(653,720,0,400),Põrand(77,447,125,155),Põrand(447,499,80,155),Põrand(582,653,193,238),Põrand(236,288,293,400),Põrand(0,1280,0,1)],
            4:[Põrand(-980,343,500,735),Põrand(1126,1280,125,670),Põrand(266,343,125,500),Põrand(948,1025,0,175),Põrand(343,1025,300,350),Põrand(343,1280,670,720),Põrand(458,1126,500,551),Põrand(458,948,125,175),Põrand(0,1280,0,1),Põrand(0,13,-9,362),Põrand(119,266,315,360),Põrand(13,160,153,198)],
            3:[Põrand(-48,1300,500,735),Põrand(1048,1240,310,360),Põrand(999,1048,310,500),Põrand(-30,40,-9,385),Põrand(40,219,151,200),Põrand(192,820,101,151),Põrand(820,874,101,385),Põrand(141,695,335,385),Põrand(282,323,385,500),Põrand(499,540,233,335),Põrand(40,1280,-54,0),Põrand(1240,1280,1,360)],
            2:[Põrand(1125,1344,500,801),Põrand(-73,133,500,784),Põrand(566,713,180,256),Põrand(203,350,463,539),Põrand(350,434,0,325),Põrand(820,916,325,396),Põrand(566,713,604,680),Põrand(0,1280,-39,-1),Põrand(1259,1323,0,385)],
            1:[Põrand(-23,1329,500,735),Põrand(0,36,-25,500),Põrand(0,1280,-42,-1)]
        }
        }

def vastaste_loomine():
    return {
        0:{#korrus
            -1: [],
            0: [Zombie(861, 500, 92, 73, 2, 1, 5, 400), Zombie(639, 500, 92, 73, 2, 1, 5, 300)],
            1: [],
            2: [Zombie(792, 500, 92, 73, 5, 1, 7, 400)],
            3: [Zombie(341, 303, 92, 73, 4, 2, 2, 170), Zombie(1081, 500, 92, 73, 5, 2, 2, 200)],
            4: [Zombie(826, 424, 92, 73, 5, 2, 6, 380), Zombie(231, 497, 92, 73, 5, 2, 6,250)],
            5: [Jälitaja(826, 500, 73, 73, 5, 2, 5), Zombie(939, 305, 29, 24, 3, 1, 12, 100)]
        },
        1:{
            1: [],
            2: [Lind(840, 188, 54, 40, 3, 2, 8, 400, 10, 300), Lind(350, 284, 54, 40, 3, 2, 8, 400, 10, 300)],
            3: [Zombie(226, 300, 92, 73, 5, 1, 5, 300), Zombie(180, 500, 92, 73, 5, 1, 7, 200)],
            4: [Jälitaja(255, 500, 92, 73, 5, 2, 5), Zombie(613, 500, 92, 73, 5, 3, 8, 400)],
            5: [Lind(951, 163, 54, 40, 3, 2, 8, 400, 10, 300), Zombie(839, 500, 92, 73, 5, 3, 8, 300), Zombie(414, 500, 92, 73, 5, 3, 5, 300)],
            6: []
        },
        2:{
            1: [Zombie(153, 233, 92, 73, 5, 3, 8, 200), Vampiir(39, 501, 56, 46, 8, 3, 8, 300, 1)],
            2: [Lind(874, 244, 54, 40, 3, 2, 8, 400, 10, 300), Lind(279, 156, 54, 40, 3, 2, 8, 400, 10, 300)],
            3: [Jälitaja(730, 640, 92, 73, 8, 4, 8), Preester(594, 219, 92, 73, 4, 1, 3, 2, 0.5), Vampiir(487, 500, 56, 46, 10, 3, 7, 300, 2), Vampiir(353,400, 56, 46, 10, 3, 7, 400, 2), Zombie(431, 317, 92, 73, 10, 4, 10, 300)],
            4: [Jälitaja(640, 496, 92, 73, 12, 3, 12), Vampiir(96, 298, 56, 46, 12, 4, 7, 300, 2), Vampiir(781, 298, 56, 46, 12, 4, 5, 300, 2), Vampiir(369,298,56,46, 12, 4, 12, 300, 2)],
            5: [Jälitaja(359, 500, 92, 73, 14, 4, 8), Zombie(405, 298, 92, 73, 14, 3, 5, 200), Zombie(96, 298, 92, 73, 14, 3, 7, 200)]
        },
        3:{
            1: [],
            2: [Lind(586, 483, 54, 40, 3, 2, 8, 400, 10, 300), Preester(30, 500, 92, 73, 4, 1, 3, 2, 0.5)],
            3: [Vampiir(195, 98, 56, 46, 15, 5, 15, 500, 2), Jälitaja(626, 500, 92, 73, 14, 4, 10), Vampiir(141, 333, 56, 46, 20, 5, 9, 300, 3), Vampiir(999,310, 56,46, 17, 5, 8, 200, 3)],
            4: [Jälitaja(611, 670, 92, 73, 10, 4, 8), Jälitaja(565, 300, 92, 73, 12, 4, 8), Jälitaja(657, 500, 92, 73, 15, 4, 8), Vampiir(458,125,56,46, 15, 5, 6, 400, 4), Vampiir(15, 153, 56, 46, 15, 5, 6, 100, 4), Vampiir(31, 500, 56, 46, 15, 5, 6, 200, 4)],
            5: [Preester(77, 125, 92, 73, 4, 1, 3, 2, 0.5), Vampiir(288, 339, 56, 46, 15, 5, 6, 300, 4), Jälitaja(407, 500, 92, 73, 15, 4, 8)]
        }
        }

def itemite_loomine():
    return {0:{#korrus
        -1: [NPC_inimene(100, 500, 30, 60, (200,200,0), konsum,["Kuidas ma saan kasulik olla?", "Tere, mina olen klienditeenindaja...", "Minu käest saab osta asju...", "Relvi, rõivaid ja midagi hamba alla..."])],
        1:[Item(120, 395, 20, 20, maailm.kasukas, "Sa leidsid rõivaid!", (200,200,0)), NPC_info(394, 500, 162, 62, (200,200,200), [100, 50, 800, 300], ["Tere tulemast Deltasse!", "Liikumiseks vajuta  'A'  ja  'D'   või   '<-'  ja  '->'  klahve", "Hüppamiseks vajuta 'W' või 'Z' klahvi", "Tulistamiseks vajuta 'SPACE' või 'X' klahvi", "Vajuta 'P' ,et hinge tõmmata", "Vajuta 'ENTER' ,kui sa kellegagi räägid ", "---------------------", "Keegi on kohvikus . . ."])],
        2:[Item(410, 245, 30, 50, maailm.railgun, "Sa leidsid relva!", (191,0,255))],
        5:[NPC_inimene(1050, 500, 30, 60, (200,200,0), söökla, ["Parool on '2020'", "Kes seal on?...", "Ohh, see oled sina...", "Hummid on terve maja üle võtnud...", "Sa pead maja neist vabastama...", "teistel korrustel on neid rohkem...", "Nad blokeerisid 3. korruse...", "Sa saad selle arvutiga avada...", "Mine teisile korrusele, ruumi 2037..."])]
        },
        1:{1:[NPC_arvut(100, 500, 100, 100, (200,200,200),None)]

        },
        3:{3:[NPC_portaal(1050, 500, 100, 140, (0,0,255), "Sa ei saa siseneda", 50, 5), NPC_portaal(40, 150, 100, 150, (0,0,255), "Sa ei saa siseneda", 1100, 365)]

        }
        }