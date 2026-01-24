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
from time import sleep 
from operator import itemgetter 

resultados = {'jogador1': randint(1, 6),
              'jogador2': randint(1, 6),
              'jogador3': randint(1, 6),
              'jogador4': randint(1, 6)}

ranking = list()

print('Valores Sorteados: ')
for key, value in resultados.items():
    sleep(1)
    print(f'{key} tirou {value} no dado.')

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

print('-' * 40)
for indice, value in enumerate(ranking):
    print(f'{indice + 1}º lugar: {value[0]} com {value[1]}.')
    sleep(1)


# aprendido sorted e itemgetter