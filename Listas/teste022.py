# Peça 5 números e, se o usuário digitar um número que já está na lista, não adicione

numeros = []

for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
print(numeros)