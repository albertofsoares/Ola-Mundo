#########################################################
#                                                       #
#                   EXERCICIO 86                        #
#                                                       #
#########################################################

# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.

# no final mostre a matriz na tela
# com a formatação correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para a linha {linhas} coluna {colunas}: '))

for linhas in range(0, 3):
    for colunas in range(0, 3):
        # O :^5 faz o número ficar centralizado em um espaço de 5 caracteres
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
    print() # Esse print vazio serve para "quebrar a linha" quando a coluna termina
