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
            [1, 0, 90, 767, black ],
            [2, 624, 1115, 100, black ],
            [56, 86, 407, 41, black ],
            [718, 45, 68, 435, black ],
            [249, 234, 468, 15, black ],
            [89, 353, 498, 34, black ],
            [600, 530, 48, 85, black ],
            [605, 590, 45, 55, black ],
            [534, 564, 81, 91, black ],
            [474, 598, 70, 50, black ],
            [401, 611, 82, 23, black ],
            [978, 326, 40, 330, black ],
            [900, 574, 93, 56, black ],
            [959, 522, 26, 2, black ],
            [961, 511, 20, 23, black ],
            [966, 445, 17, 36, black ],
            [892, 464, 41, 31, black ],
            [933, 495, 0, 0, black ],
            [1117, 0, 404, 765, black ],

        ]

        for block in level:
            block = Block(block[0], block[1], block[2], block[3], block[4])
            self.lista_de_objetos.add(block)
