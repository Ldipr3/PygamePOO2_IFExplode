__author__ = 'Lucas'

from br.edu.ifes.IFExplode.cdp.Player import *
from br.edu.ifes.IFExplode.cgt.AplGerenciarFase import *
from br.edu.ifes.IFExplode.cdp.Fase_1 import *



player.set_image(os.path.join("Images", "PlayerV1.png"))
player.set_position(40, 40) #define uma posicao para o player
player.set_fase(fase_atual)

lista_objetos_ativos = pygame.sprite.Group() #cria lista de objetos ativo
lista_objetos_ativos.add(player) #adiciona player na lista de objetos ativos
