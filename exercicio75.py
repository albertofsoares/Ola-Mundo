#############################################
#   EXERCICIO 75 - TUPLAS - EXERCICIO 75    #
#############################################

# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla No final, mostre:

# Quantas vezes apareceu o valor 9

# Em que posição foi digitado o primeiro valor 3

# Quais foram os números pares

tulpa = (int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')), int(input('Digite um número: ')))

par = 0

for c in range(0, 4):

    if tulpa[c] % 2 == 0:
        par += 1

print(f'O número nove (9) apareceu {tulpa.count(9)} vezes')
print(f'O número 3 apareceu em: {tulpa.index(3) + 1}º lugar')
print(f'A tulpa ficou: {tulpa}.')
print(f'Existem {par} números pares.')