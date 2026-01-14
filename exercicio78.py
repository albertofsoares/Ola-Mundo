#########################################################
#                                                       #
#                   EXERCICIO 78                        #
#                                                       #
#########################################################

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

lista = []

for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))

maior = max(lista)
menor = min(lista)

print('O maior valor está nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')

print('\nO menor valor está nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')  

