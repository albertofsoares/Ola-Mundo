# Crie uma lista com 10 números e peça ao usuário um número para remover.
# Se não existir, avise-o.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input('Digite um número: '))

if numero not in numeros:
    print('Este número não está na lista')
else:
    print(f'O número {numero} foi removido da Lista!')
    numeros.remove(numero)
    print(numeros)