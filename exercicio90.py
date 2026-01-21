#########################################################
#                                                       #
#                   EXERCICIO 90                        #
#                                                       #
#########################################################

# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.

# no final mostre o conteúdo da estrutura na tela.

boletim = {}

boletim['aluno'] = str(input('Digite o nome do aluno: '))
boletim['média'] = float(input('Digite a média do aluno: '))

if boletim['média'] >= 7.0:
    boletim['situação'] = 'aprovado'
else:
    boletim['situação'] = 'reprovado'

for key, value in boletim.items():
    print(f'O valor de {key} é igual a {value}')