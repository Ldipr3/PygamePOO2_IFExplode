__author__ = 'Lucas'

import pygame
from br.edu.ifes.IFExplode.cdp.color import *


if(__name__ == "__main__"):

    pygame.init()
    tamanho_tela = largura, altura = 2000, 768
    Janela = pygame.display.set_mode(tamanho_tela)

    clock = pygame.time.Clock()
    fps = 60

    Janela.fill(white)
    pygame.display.update( )
    '''
    alguns exemplos de desenhos de estruturas
    rect = pygame.Rect((20, 50), (100, 200))
    #pygame.draw.rect(Janela, red, rect, 3)

    lista_pontos = [(20, 50), (3, 120), (100, 120)]
    pygame.draw.polygon(Janela, green, lista_pontos)


                      (superficie, cor, (x, y), raio, stroke)
    pygame.draw.circle(Janela, silver, (largura/2, altura/2), 100, 5)

    pygame.draw.line(Janela, gray, (100, 100), (1024,768), 3 )
    '''
    para_desenhar = [ ]

    desenhe_block_box = False



    rodando = True
    while (rodando):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or \
            (event.type == pygame.KEYDOWN and \
            (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
                rodando = False

            if(event.type == pygame.MOUSEMOTION):
                mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()

            if(event.type == pygame.MOUSEBUTTONDOWN):
                pos = mouse_pos
                desenhe_block_box = True
            if(event.type == pygame.MOUSEBUTTONUP):
                final_pos = mouse_pos
                desenhe_block_box = False

                rect = pygame.Rect(pos, (final_pos[0] - pos[0], final_pos[1] - pos[1]))
                rect.normalize()

                para_desenhar += [rect]# para pegar a altura e a largura

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RETURN):
                    for plataforma in para_desenhar:
                        print "[" + str(plataforma).split("(")[1].split(")")[0] + ", black ],"

                if(event.key == pygame.K_BACKSPACE):
                    para_desenhar.pop()

        Janela.fill(white)

        if(desenhe_block_box):
            pygame.draw.rect(Janela, red, pygame.Rect(pos, (mouse_pos[0] - pos[0], mouse_pos[1]- pos[1])))

        for item in para_desenhar:
            pygame.draw.rect(Janela, black, item)

        pygame.display.update()

        clock.tick(fps)





    pygame.quit()