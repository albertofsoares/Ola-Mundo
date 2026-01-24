# Faça um programa que leia nome e média de um aluno,
# uardando também a situação em um dicionário.

# No final, mostre o conteúdo da estrutura na tela.


aluno = {}

aluno['nome'] = str(input('Nome do Aluno: '))
aluno['média'] = float(input('Média do Aluno: '))

if aluno['média'] >= 7.0:
    print(f'O aluno {aluno["nome"]} está aprovado')
    aluno['situação'] = 'Aprovado'
elif aluno > 5.0 and aluno < 7.0:
    aluno['situação'] = 'Recuperação'
    print(f'O aluno {aluno["nome"]} está em recuperação')
else:
    aluno['situação'] = 'Reprovado'
    print(f'O aluno {aluno["nome"]} está reprovado')

for key, value in aluno.items():
    print(f'{key} é igual a {value}')