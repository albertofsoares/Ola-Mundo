#########################################################
#                                                       #
#                   EXERCICIO 89                        #
#                                                       #
#########################################################

# Crie um programa que leia o nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.

# no final mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada
# aluno individualmente

# Modelagem de Dados, lista vazia.
alunos = []

# Fonte de Alimentação da Lista
while True:

    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    media = (n1 + n2) / 2

    alunos.append([nome, [n1, n2], media])

    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()

    if escolha == 'N':
        break

# Formatação de Strings
txt = 'indice' 
txt1 = 'nome'
txt2 = 'média'

# Painel de Saída do Boletim
print('-' * 60)
print(f'{txt:<20}', end='')
print(f'{txt1:^20}', end='')
print(f'{txt2:>20}', end='')
print()

# Estrutura de Repetição para mostrar indice, aluno e média
for indice, aluno in enumerate(alunos):
    print(f'{indice:<20}', end='')
    print(f'{aluno[0]:^20}', end='')
    print(f'{aluno[2]:>20}', end='')

# Laço de Repetição para pesquisar as notas ou encerrar o programa.
while True:

    pesquisar = int(input('\nDigite o indice para pesquisar ou 999 para sair: '))

    if pesquisar == 999:
        break
    
    if pesquisar <= len(alunos) -1:
        print('Nome do Aluno: ', alunos[pesquisar][0])
        print('Notas do Aluno: ', alunos[pesquisar][1])
    else:
        print('Indice Inválido')
    

