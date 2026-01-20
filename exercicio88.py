#########################################################
#                                                       #
#                   EXERCICIO 88                        #
#                                                       #
#########################################################

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# o programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta

# jogo 1 (numeros de 1 a 60 sem repetições)
# jogo 2 (numeros de 1 a 60 sem repetições)
# jogo 3 (numeros de 1 a 60 sem repetições)
# jogo 4 (numeros de 1 a 60 sem repetições)

from random import randint
from time import sleep 

main = []
temp = []
cont = 0

jogos = int(input('Quantos jogos você quer gerar? '))
 

for jogo in range(0, jogos):
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
    main.append(temp[:])
    temp.clear()

for jogo in range(0, jogos):
    print(f'Palpite do {jogo + 1}º jogo: {main[jogo]}')
    sleep(2)