# Exercício Python 075: 

# Desenvolva um programa que leia quatro valores pelo teclado 
# e guarde-os em uma tupla. 

# No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

valores = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))

pares = ''
for valor in valores:
    
    if valor % 2 == 0:
        pares += str(valor) + ' '


if 3 in valores:
    print(f'O número "3" apareceu pela primeira vez no indice: ', valores.index(3))

print(f'O número "9" apareceu {valores.count(9)} vezes.')
print(f'Os valores pares são: {pares}')
