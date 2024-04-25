import pygame
from pygame.locals import *
from sys import exit
import pygame.locals 
from random import randint

largura_obj = 100
altura_obj = 100
largura = 1280
altura = 960
x = largura/2 - largura_obj/2
y = altura/2 - altura_obj/2
x_azul = randint(20, 1200)
y_azul = randint(30,860)
pygame.font.init()
pontos = 0
fonte = pygame.font.SysFont('Arial', 60, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo')
clock = pygame.time.Clock()

while True: 
    clock.tick(30)
    tela.fill((255,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(
                exit()
            )
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
               x = x - 40
            if event.key == K_d:
                x = x + 40
            if event.key == K_w:
                y = y - 40
            if event.key == K_s:
                y = y + 40'''
    if pygame.key.get_pressed()[K_a]:
        x = x - 20   
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20      
    ret_vermelho = pygame.draw.rect(tela, (255,0,0),(x, y, largura_obj, altura_obj))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul, y_azul, largura_obj,))
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40,600)
        y_azul =randint(50,430)
        pontos = pontos + 1
        
    tela.blit(texto_formatado, (900, 80))
    pygame.display.update()   
    if y >= altura:
        y = 0
    if y < 0:
        y = altura
    if x >= largura:
        x = 0
    if x < 0:
        x = largura