# Exercício Python 076: 
# 
# Crie um programa que tenha uma tupla única com nomes de produtos 
# e seus respectivos preços, na sequência. 
# 
# No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

produtos = ('Notebook', 1250, 'Computador i7', 1500, 'iPhone 15', 850)
print('-'*40)
for produto in produtos:
    if type(produto) == str:
        print(f'{produto:.<30}', end='')
    if type(produto) == int:
        print(f'R${produto:>7.2f}')
print('-'*40)