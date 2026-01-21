#########################################################
#                                                       #
#                   EXERCICIO 93                        #
#                                                       #
#########################################################

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 

# O programa vai ler o nome do jogador e quantas partidas ele jogou. 

# Depois vai ler a quantidade de gols feitos em cada partida. 

# No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.

dicionario = {}
tgols = []
soma = 0

dicionario['nome'] = str(input('Digite o nome do Jogador: '))
dicionario['partidas'] = int(input('Digite quantas partidas ele jogou: '))

for c in range(0, dicionario['partidas']):
    gols = int(input(f'Quantos gols ele fez na {c + 1} partida: '))
    tgols.append(gols)
    soma += tgols[c]

    dicionario['tgols'] = tgols.copy()
    dicionario['gols'] = soma

print(dicionario)
print(f'O jogador {dicionario['nome']} fez um total de {soma} gols no campeonato!')
for c in range(0, dicionario['partidas']):
    print(f'Gols na partida {c+1}: {tgols[c]}')
