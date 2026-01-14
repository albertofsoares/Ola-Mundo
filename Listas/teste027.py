# Pergunte ao usuário o nome de 3 convidados e guarde numa lista. 
# Depois, mostre a lista em ordem alfabética.

convidados = []

for convidado in range(0, 3):
    convidados.append(str(input('Digite o nome do convidado: ')))

convidados.sort()
print(f'A lista de convidados em ordem é: {convidados}')