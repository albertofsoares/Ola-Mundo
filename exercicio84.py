#########################################################
#                                                       #
#                   EXERCICIO 84                        #
#                                                       #
#########################################################

# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista, no final mostre:

# Quantas pessoas foram cadastradas

# Uma listagem com as pessoas mais pesadas

# Uma listgaem com as pessoas mais leves

dados = []
temp = list()
pesado = leve = 0

while True:

    # Armazenamos dados (nome e peso) em uma lista temporária a cada volta
    temp.append(str(input('Digite o nome: ')))
    temp.append(int(input('Digite o peso: ')))

    # Passamos os dados da lista temporária pra principal e limpamos ela
    dados.append(temp[:])
    temp.clear()

    # Estrutura Condicional para manter ou quebrar o loop.
    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()

    if escolha == 'N':
        break

for c in range(0, len(dados)):
    if c == 0:
        leve = dados[c][1]
        pesado = dados[c][1]
    else:
        if dados[c][1] > pesado:
            pesado = dados[c][1]
        
        if dados[c][1] < leve:
            leve = dados[c][1]

for peso in dados:
    if peso[1] == pesado:
        print(f'{peso[0]}', end=' ')

for peso in dados:
    if peso[1] == leve:
        print(f'{peso[0]}', end=' ')

print(f'{len(dados)} pessoas foram cadastradas no programa.')

