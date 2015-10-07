__author__ = 'Lucas'

import pygame

pygame.init()

# Definicoes da Janela
window_tamanho = window_largura, window_altura = 1200, 768
window = pygame.display.set_mode(window_tamanho, pygame.RESIZABLE)
pygame.display.set_caption('IFExplode!!!')
clock = pygame.time.Clock()#funcao clock controla o tempo dentro da janela
frames_por_segundo = 60
