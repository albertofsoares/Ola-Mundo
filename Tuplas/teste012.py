# Conte quantos números negativos existem em uma tupla.

numeros = (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5)

for numero in numeros:
    if numero < 0:
        print(numero, ' → ', end='')
print('FIM')