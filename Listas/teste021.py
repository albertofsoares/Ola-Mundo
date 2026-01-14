# Peça ao usuário 5 números, um por um, e salve-os em uma lista.2

numeros = []

for numero in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
print(numeros)