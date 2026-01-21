#########################################################
#                                                       #
#                   EXERCICIO 95                        #
#                                                       #
#########################################################

# Aprimore o desafio 093 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 

# O programa vai ler o nome do jogador e quantas partidas ele jogou. 

# Depois vai ler a quantidade de gols feitos em cada partida. 

# No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato

time = []
jogador = {}

while True:
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input('Nº de Partidas: '))

    gols = []
    tgols = 0
    for c in range(0, jogador['partidas']):
        gol = int(input(f'Quantos gols na {c + 1} partida? '))
        gols.append(gol)
        tgols += gol
    jogador['gols'] = gols
    jogador['total de gols'] = tgols 
    
    time.append(jogador.copy())

    escolha = str(input('Deseja continuar? [S] ou [N]: ')).upper().strip()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S] ou [N]: ')).upper().strip()
    
    if escolha == 'N':
        break

print('-' * 40)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 40)

for indice, jogador in enumerate(time):
    print(f'{indice:<4} {jogador["nome"]:<15} {str(jogador["gols"]):<15} {jogador["total de gols"]:<5}')

print('-' * 40)

while True:
    
    cod = int(input('Digite o COD do jogador que quer visualizar (999 para sair): '))

    if cod == 999:
        break

    if cod >= len(time):
        print('Esse jogador não existe no time!')
    

    for indice, gols in enumerate(time[cod]["gols"]):
        print(f'No jogo {indice+1} fez {gols} gols.')
    
    