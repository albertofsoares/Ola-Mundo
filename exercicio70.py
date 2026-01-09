#####################################
#
# EXERCICIO 70
#
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:

# A) Qual é o total gasto na compra

# B) Quantos produtos custam mais de R$1000

# C) Qual é o nome do produto mais barato

soma = 0
cont = 0

while True:
    produto = str(input('Digite o nome do Produto: '))
    valor = float(input('Digite o valor do Produto: R$'))
    maisbarato = valor
    prodbarato = produto
    soma += valor

    escolha = str(input('Deseja Continuar [S/N]? ')).upper()

    while escolha not in 'SN':
        escolha = str(input('Deseja Continuar [S/N]? ')).upper()

    if maisbarato < valor:
        maisbarato = valor
        prodbarato = produto

    if valor > 1000:
        cont += 1

    if escolha == 'N':
        print('Encerrando o Programa!')
        break
print(f'{cont} produtos custam mais de R$ 1.000 reais')
print(f'O produto {prodbarato} é o mais barato!')
print(f'O total gasto na compra é de {soma}')