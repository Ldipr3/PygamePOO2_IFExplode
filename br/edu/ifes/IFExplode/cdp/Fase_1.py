__author__ = 'Lucas'

import pygame

from br.edu.ifes.IFExplode.cdp.Fase import *
from br.edu.ifes.IFExplode.cdp.Block import *


class Fase_1(Fase):

    def __init__(self, objeto_player):

        super (Fase_1, self).__init__(objeto_player)

        #define um lugas especifico aonde o player vai iniciar naquela fase
        self.player_inicio = self.player_inicio_x, self.player_inicio_y = 300,0

        level = [
            # [ x, y, largura, altura, color ]

            [3, 829, 1774, 36, black ],
            [1636, 876, 0, 0, black ],
            [1764, 715, 735, 180, black ],
            [1798, 891, 14, 3, black ],
            [0, 0, 54, 830, black ],
            [49, 63, 54, 74, black ],
            [91, 102, 49, 99, black ],
            [119, 149, 61, 121, black ],
            [163, 191, 37, 166, black ],
            [191, 314, 32, 110, black ],
            [214, 356, 34, 183, black ],
            [248, 397, 54, 214, black ],
            [295, 432, 49, 258, black ],
            [329, 483, 29, 257, black ],
            [346, 538, 42, 166, black ],
            [372, 589, 44, 147, black ],
            [409, 653, 40, 157, black ],
            [439, 720, 37, 117, black ],
            [466, 767, 49, 95, black ],
            [514, 540, 167, 58, black ],
            [572, 594, 126, 65, black ],
            [628, 645, 67, 96, black ],
            [671, 697, 117, 39, black ],
            [749, 672, 70, 59, black ],
            [880, 788, 79, 39, black ],
            [929, 742, 64, 62, black ],
            [964, 682, 92, 74, black ],
            [1005, 638, 112, 60, black ],
            [937, 490, 50, 1, black ],
            [1071, 326, 136, 333, black ],
            [787, 372, 308, 97, black ],
            [691, 604, 61, 92, black ],
            [516, 0, 18, 551, black ],
            [533, 474, 100, 80, black ],
            [533, 386, 64, 104, black ],
            [738, 310, 84, 106, black ],
            [677, 311, 81, 54, black ],
            [531, 195, 69, 84, black ],
            [710, 119, 68, 4, black ],
            [729, 221, 113, 124, black ],
            [743, 97, 91, 175, black ],
            [672, 116, 90, 23, black ],
            [587, 234, 43, 35, black ],
            [916, 1, 27, 233, black ],
            [1057, 120, 81, 301, black ],
            [991, 302, 84, 30, black ],
            [939, 190, 54, 23, black ],
            [1038, 283, 0, 0, black ],
            [1028, 282, 38, 28, black ],
            [668, 685, 89, 28, black ],
            [1052, 420, 74, 55, black ],
            [1110, 413, 37, 56, black ],
            [1135, 397, 21, 91, black ],
            [1140, 418, 18, 71, black ],



        ]

        for block in level:
            block = Block(block[0], block[1], block[2], block[3], block[4])
            self.lista_de_objetos.add(block)
