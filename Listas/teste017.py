# Crie uma lista de números e crie uma nova lista 
# apenas com os números maiores que 10.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

maior10 = []

for numero in numeros:
    if numero > 10:
        maior10.append(numero)
        
print(maior10)