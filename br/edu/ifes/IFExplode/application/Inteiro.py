__author__ = 'Lucas'

#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Lucas"
__date__ = "$26/09/2015 16:52:42$"

import pygame, sys, os, time

from br.edu.ifes.IFExplode.cdp.color import *
from br.edu.ifes.IFExplode.cdp.Player import *
from br.edu.ifes.IFExplode.cdp.Block import *
from br.edu.ifes.IFExplode.cdp.Fase_1 import *
from br.edu.ifes.IFExplode.cgt.AplGerenciarPlayer import *
from br.edu.ifes.IFExplode.cgt.AplGerenciarFase import *
from br.edu.ifes.IFExplode.cih.JanelaPrincipal import *
from br.edu.ifes.IFExplode.cci.CrlFase import *

from pygame.locals import *

CrlFase()

if (__name__ == "__main__"):

    running = True # Variavel para o loop da janela principal

    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or \
            (event.type == pygame.KEYDOWN and \
            (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
                running = False

        #Funcoes de atualizacao

        player.update(fase_atual.lista_de_objetos, event)
        event = None #esvazia a variavel event
        fase_atual.update()


        #Testes de logica do jogo

        fase_atual.controla_camera()

        #Desenha e redesenha tudo

        fase_atual.draw(window)
        lista_objetos_ativos.draw(window)


        #Atrasa a Framerate

        clock.tick(frames_por_segundo)

        #Atualiza a tela

        pygame.display.update()


pygame.quit()

