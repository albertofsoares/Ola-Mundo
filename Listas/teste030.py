# Crie uma lista vazia. Peça ao usuário para digitar números até ele digitar 0. 
# Depois, mostre a lista na ordem inversa.

numeros = []

while True:

    numero = int(input('Digite um número: '))

    if numero == 0:
        break
    
    while numero not in numeros:
        numeros.append(numero)
    

print(numeros)