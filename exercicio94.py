#########################################################
#                                                       #
#                   EXERCICIO 94                        #
#                                                       #
#########################################################

# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário 
# e todos os dicionários em uma lista. 

# No final, mostre:

# A) Quantas pessoas foram cadastradas.

# B) A média de idade.

# C) Uma lista com as mulheres.

# D) Uma lista de pessoas com idade acima da média.

pessoas = []
mulheres = []
pessoa = {}
cadastros = 0
soma = 0
idadeav = []

while True:
    pessoa['nome'] = str(input('Digite o nome da pessoa: '))
    pessoa['sexo'] = str(input('Digite o sexo da pessoa [M/F]: '))
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    pessoas.append(pessoa.copy())
    cadastros += 1

    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S] ou [N]: ')).upper().strip()
    
    if escolha == 'N':
        break

for c in range(0, len(pessoas)):
    soma += pessoas[c]['idade']

if cadastros > 0:
    media = soma / cadastros

for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        idadeav.append(pessoas[c].copy())

    if pessoas[c]['sexo'] == 'F':
        mulheres.append(pessoas[c].copy())

print(f'{cadastros} pessoas foram cadastradas.')
print(f'A média de idade das pessoas cadastradas é de {media} anos')
print(f'Lista de Mulheres Cadastradas: \n {mulheres}')
print(f'Lista de pessoas com idade acima da média: \n {idadeav}')
