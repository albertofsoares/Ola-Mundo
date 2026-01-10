#############################################
#   EXERCICIO 74 - TUPLAS - EXERCICIO 74    #
#############################################

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla

# Depois disso, mostre a listagem de números erados
# e também indique o menor e o maior valor que estão na tupla

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))

maior = -1
menor = 11

for c in range(0, len(numeros)):
    print(f'Numero da vez: ', numeros[c])

    if numeros[c] > maior:
        maior = numeros[c]

    if numeros[c] < menor:
        menor = numeros[c]
print(f'Maior: {maior} | Menor {menor}')

############################################

# from random import randint

# # Gerando a tupla
# numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
#            randint(0, 10), randint(0, 10))

# print(f'Os valores sorteados foram: ', end='')
# for n in numeros:
#     print(f'{n} ', end='')

# # A MÁGICA: Em vez de todo aquele IF e FOR de comparação...
# print(f'\nO maior valor sorteado foi {max(numeros)}')
# print(f'O menor valor sorteado foi {min(numeros)}')