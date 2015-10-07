__author__ = 'Lucas'

from br.edu.ifes.IFExplode.cdp.Player import *
from br.edu.ifes.IFExplode.cgt.AplGerenciarFase import *
from br.edu.ifes.IFExplode.cdp.Fase_1 import *

lista_objetos_ativos = pygame.sprite.Group() #cria lista de objetos ativo

class AplGerenciarPlayer(Player):

    def define_propriedades(self, Player):
        player.set_image(os.path.join("Images", "Player_V3.png"))
        player.set_position(40, 40) #define uma posicao para o player
        player.set_fase(fase_atual)


    def ativa_player(self, Player):
        lista_objetos_ativos.add(player) #adiciona player na lista de objetos ativos
