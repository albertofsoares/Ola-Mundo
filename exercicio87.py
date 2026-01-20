#########################################################
#                                                       #
#                   EXERCICIO 87                        #
#                                                       #
#########################################################

# Aprimore o desafio anterior, mostrando no final:

# A soma de todos os valores pares digitados

# A soma dos valores da terceira coluna

# O maior valor da segunda linha

# #1C     #2C     #3C
# [ ]     [ ]     [ ] # 1 linha
# [ ]     [ ]     [ ] # 2 linha
# [ ]     [ ]     [ ] # 3 linha


soma = 0
soma3coluna = 0

matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input('Digite um número: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]

for linha in range(3):
    soma3coluna += matriz[linha][2]

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]}]', end=' ')
    print()

maior = max(matriz[1])
print(f'Soma dos números pares: {soma}')
print(f'A Soma da terceira coluna é: {soma3coluna}')
print(f'O maior número da segunda linha é: {maior}')