
#Bibliotecas utilizadas para a criação do game

import pygame 
from sys import exit
from pygame.locals import*
from random import randint
import time

#inicialização do game
pygame.init()

#dimensões da janela
largura = 600
altura = 400

#Variáveis para controlar a origem do objeto
x = largura/2
y = altura/2
x_purple = randint(15,570)
y_purple = randint(15,370)


#Inicialização e configuração da janela
window = pygame.display.set_mode((largura, altura))   #criação
window.fill((255,255,255))     #cor de fundo
pygame.display.set_caption('Jogo de comer o cu de quem ta lendo')   #nome da janela
clock = pygame.time.Clock() #criação da variável de frame rate


#Inicializando uma fonte parar criar um texto
font = pygame.font.SysFont('sans-serif', 20, bold=True, italic=False)


#Inicializando som do game
music = pygame.mixer.music.load('BoxCat Games - Passing Time.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
colision_noise = pygame.mixer.Sound('smw_kick.wav')


#Criando variáveis da dinâmica do game
points = 0

start = time.time()
while True: #gameloop

    window.fill((255,255,255)) #aualização da cor de fundo da tela
    clock.tick(120)  #setando o frame rate


    #Texto que aparecerá na tela
    message = f"PONTOS: {points}"
    final_message = "Parabéns, seu CU foi comido com sucesso!"
    #Renderizando a fonte
    formated_text = font.render(message, True, (100,100,100))
    final_text = font.render(final_message, True, (0,0,0))

    for event in pygame.event.get():    #definindo os eventos externos(inputs)
        if event.type == QUIT:
            pygame.quit()  
            exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    
    if points >= 50:
        
        end = time.time()
        result_time = end - start
        time_text = f'Tempo = {round(result_time,2)} segundos'
        formated_time_text = font.render(time_text, False,(0,0,0))

        while(1):
            pygame.draw.rect(window,(255, 102, 204), (100,153,400,50))
            window.blit(final_text, (130,170))
            window.blit(formated_time_text,(150,210))
        
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                         
                if event.type == KEYDOWN:
                    if event.key ==K_ESCAPE:
                        exit()
                        


    #eventos de tecla pressionada
    if pygame.key.get_pressed()[K_DOWN]:
        y += 5
    if pygame.key.get_pressed()[K_UP]:
        y -= 5
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 5
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 5

    #exemplos de formas de objetos para se criar
    '''pygame.draw.rect(window,(180,0,0), (200,150,200,100), 5)
    pygame.draw.circle(window,(179,218,255), (300,200), 40, 5)
    pygame.draw.line(window,(255,204,0), (50,50),(550,50), 10)'''


    #objetos que criei para o game(2 circulos)
    green_circle = pygame.draw.circle(window, (0, 102, 102), (x,y), 30)
    purple_circle = pygame.draw.circle(window, (102,0,51), (x_purple,y_purple), 30)

    #Tratando a colisão
    if green_circle.colliderect(purple_circle):
        x_purple = randint(15,570)
        y_purple = randint(15,370)
        points += 1
        colision_noise.play()

    #Imprimindo o texto na tela
    window.blit(formated_text, (480,20))

    #Atualizando o display
    pygame.display.update()    


