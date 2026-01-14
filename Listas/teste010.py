# Crie uma lista vazia e adicione 3 cores nela, uma por uma.

cores = []

for cor in range(0, 3):
    cores.append(str(input('Digite uma cor: ')))
print(cores)