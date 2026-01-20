#########################################################
#                                                       #
#                   EXERCICIO 85                        #
#                                                       #
#########################################################

# Crie um programa onde 
# o usuário possa digitar sete valores númericos
# e cadastre-os em uma lista única 
# que mantenha separados os valores
# pares e impares. 
# No final, mostre os valores pares e impares 
# em ordem crescente

valores = [[], []]

for valor in range(0, 7):
    numero = int(input('Digite um valor: '))

    if numero % 2 == 0:
        valores[0].append(numero)
    
    if numero % 2 != 0:
        valores[1].append(numero)

valores[0].sort()
valores[1].sort()

print(f'Números Pares: {valores[0]}')
print(f'Números Impares: {valores[1]}')

