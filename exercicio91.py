#########################################################
#                                                       #
#                   EXERCICIO 91                        #
#                                                       #
#########################################################

# Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios.

# guarde esses resultados em um dicionário,
# no final coloque esse dicionário em ordem,
# sabendo queo vencedor tirou o maior número
# do/no dado.

from random import randint

resultados = {}
ranking = []

for c in range(0, 4):
    resultados[f'jogador{ c + 1 }'] = randint(1, 6)

maior = 0
vencedor = ''

for c in range(0, 4):
    maior = 0
    vencedor = ''
    for k, v in resultados.items():
        if v > maior:
            maior = v
            vencedor = k
    ranking.append([vencedor, maior])
    del resultados[vencedor]

for jogador, dados in enumerate(ranking):
    print(f'O jogador {jogador + 1} tirou {dados[1]}!')
#