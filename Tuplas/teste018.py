# Encontre o maior número em uma tupla sem usar a função max().

numeros = (1, 8, 5, 4, 6)
maior = 0
for numero in numeros:
    if numero > maior:
        maior = numero
print(f'O maior número foi {maior}')