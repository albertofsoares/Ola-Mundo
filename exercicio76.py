#############################################
#   EXERCICIO 76 - TUPLAS - EXERCICIO 76    #
#############################################

# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços na sequência.

# No final mostre uma listagem de preços,
# oranizando os dados em forma tabular

# O Python entende 1250.00 como número. Ele não entende 'R$ 1.250' como número.
tupla = ('Notebook', 250.00, 'Computador i5', 850.00,
         'Smartphone', 099.00, 'Smart TV LED 32', 999.99)

cont = 0
# for c in tupla:
#     if cont % 2 == 0:
#         print(f'{tupla[cont]}', end='')
#     else:
#         print(f'{tupla[cont]}')

#     cont += 1


for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        # Imprime o produto alinhado à esquerda e NÃO pula linha
        print(f'{tupla[pos]:.<30}', end='')
    else:
        # Imprime o preço alinhado à direita e PULA a linha (padrão)
        print(f'R$ {tupla[pos]:>7.2f}')

print('-' * 40)

