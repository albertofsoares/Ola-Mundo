# Exercício Python 72: 
# 
# # Crie um programa que tenha uma dupla totalmente preenchida com uma contagem 
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado 
# (entre 0 e 20) e mostrá-lo por extenso.

# extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 
#            'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
#            'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
#            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# i = int(input('Digite um número de zero a vinte: '))
# for c in range(0, 20):
#     if i < 0 or i > 20:
#         i = int(input('Digite um número de zero a vinte: '))
# print(f'O número {i} por extenso fica {extenso[i]}')


###############################################

# Solução do Guanabara

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
        'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
        'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
print(f'Você digitou o número {cont[num]}')

while True:

    escolha = str(input('Deseja continuar [S/N]? '))

    if escolha in 'Nn':
        break
    else:
        while True:
            num = int(input('Digite um número entre 0 e 20: '))
            if 0 <= num <= 20:
                break
        print(f'Você digitou o número {cont[num]}')