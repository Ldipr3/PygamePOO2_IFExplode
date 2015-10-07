__author__ = 'Lucas'

import pygame

from br.edu.ifes.IFExplode.cdp.Fase import *
from br.edu.ifes.IFExplode.cdp.Block import *


class Fase_1(Fase):

    def __init__(self, objeto_player):

        super (Fase_1, self).__init__(objeto_player)

        #define um lugas especifico aonde o player vai iniciar naquela fase
        self.player_inicio = self.player_inicio_x, self.player_inicio_y = 600,0

        level = [
            # [ x, y, largura, altura, color ]
            [1, 1, 112, 848, black ],
            [92, 785, 1235, 63, black ],
            [1299, 786, 990, 62, black ],
            [2273, 786, 226, 62, black ],
            [2486, 0, 13, 847, black ],
            [2, 841, 1347, 33, black ],
            [1319, 834, 530, 40, black ],
            [1814, 827, 685, 47, black ],
            [106, 0, 428, 794, black ],
            [870, 723, 55, 66, black ],
            [984, 665, 55, 134, black ],
            [1097, 623, 46, 162, black ],
            [1025, 515, 48, 43, black ],
            [1112, 411, 48, 34, black ],
            [1218, 325, 250, 44, black ],
            [1194, 576, 42, 212, black ],
            [1536, 0, 71, 612, black ],
            [1388, 130, 147, 42, black ],
            [2422, 46, 63, 744, black ],
            [2364, 100, 70, 700, black ],
            [2316, 161, 49, 638, black ],
            [2264, 221, 56, 571, black ],
            [2215, 280, 53, 513, black ],
            [2156, 325, 65, 466, black ],
            [2108, 357, 49, 467, black ],
            [2068, 427, 46, 367, black ],
            [1993, 517, 33, 268, black ],
            [1942, 543, 28, 242, black ],
            [1876, 613, 34, 170, black ],
            [1804, 666, 43, 115, black ],
            [1729, 709, 54, 75, black ],
            [1806, 747, 41, 69, black ],
            [1878, 763, 33, 33, black ],
            [1946, 766, 23, 28, black ],
            [1995, 780, 30, 16, black ],
            [1730, 778, 52, 22, black ],

        ]

        for block in level:
            block = Block(block[0], block[1], block[2], block[3], block[4])
            self.lista_de_objetos.add(block)
