__author__ = 'Lucas'

from br.edu.ifes.IFExplode.cdp.Player import *
from br.edu.ifes.IFExplode.cgt.AplGerenciarPlayer import *
from br.edu.ifes.IFExplode.cdp.Fase_1 import *


player = Player() #cria o player
lista_Fases = [] #uma lista para as fases
lista_Fases.append(Fase_1( player )) #adiciona a fase 1 a lista e passa o objeto player naquela fase

fase_atual_numero = 0 # um numero para identificar a fase atual
fase_atual = lista_Fases[fase_atual_numero] #guarda a posicao da fase atual da lista

