# Exercício Python 074: 
# 
# Crie um programa que vai gerar cinco números aleatórios 
# e colocar em uma tupla. Depois disso, mostre a listagem de números 
# gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {numeros}')

maior = -1
menor = 11

for numero in numeros:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero
print(f'O menor valor foi de {menor} e o maior valor foi de {maior}')

############# SEM LAÇOS DE REPETIÇÃO OU COMPARAÇÕES ####################

print(f'O maior número foi {max(numeros)}')
print(f'O menor número foi {min(numeros)}')