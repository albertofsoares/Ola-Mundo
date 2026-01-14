# Crie uma lista de números e imprima apenas os números pares usando um for e um if.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(numero, end='...')