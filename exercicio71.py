#####################################
#
# EXERCICIO 70
#
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacadado (num int)
# e o programa vai informar quantas cédulas de cada valor serão entregues.

# obs: considere que o caixa possui cédulas de 50, 20, 10 e 1 real.

cont = 0

while True:
    saque = float(input("Digite o valor a ser sacado: R$"))
    nota = 50

    while saque >= 50:
        saque -= nota
        cont += 1
    print(f'Você precisa de {cont} notas de R$50.00')

    cont = 0

    while saque >= 20:
        nota = 20
        saque -= nota 
        cont += 1
    print(f'Você precisa de {cont} notas de R$20.00')

    cont = 0

    while saque >= 10:
        nota = 10
        saque -= nota 
        cont += 1
    print(f'Você precisa de {cont} notas de R$10.00')

    cont = 0

    while saque >= 1 and saque < 10:
        nota = 1
        saque -= nota 
        cont += 1
    print(f'Você precisa de {cont} notas de R$1.00')

    cont = 0

    escolha = str(input('Deseja realizar outro saque [S/N]? ')).upper()

    while escolha not in "SN":
        escolha = str(input('Deseja realizar outro saque [S/N]? ')).upper()
    
    if escolha == 'N':
        break
print('Fim do Programa')

        
