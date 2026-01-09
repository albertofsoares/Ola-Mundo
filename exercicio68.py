#####################################
#
# EXERCICIO 68
#
# Faça um programa que jogue par ou impar com o computador.
# o jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

# from random import randint
# ganhou = 0

# while True:
#     escolha_pc = randint(0, 10)
#     escolha_humana = int(input('Digite um número: '))
#     par_impar = str(input('P/I')).upper()
#     par = False
#     impar = False 

#     soma = escolha_pc + escolha_humana 

#     print(f'Escolha do Computador: {escolha_pc}')
#     print(f'Sua Escolha: {escolha_humana}')
#     print(f'Total da Soma: {soma}')

#     if soma % 2 == 0:
#         print('Número Par')
#         par = True
#     else:
#         print('Numero Impar')
#         impar = True

#     if par_impar == 'P' and par == True:
#         print('Você VENCEU!')
#         ganhou += 1
#         print(f'Número de vezes que ganhou: {ganhou}')
#     elif par_impar == 'P' and par == False:
#         print('GAME OVER! Você perdeu.')
#         print(f'Número de vezes que ganhou: {ganhou}')
#         break
#     elif par_impar == 'I' and impar == True:
#         print('Você VENCEU!')
#         ganhou += 18
#         print(f'Número de vezes que ganhou: {ganhou}')
#     elif par_impar == 'I' and impar == False:
#         print('GAME OVER! Você perdeu.')
#         print(f'Número de vezes que ganhou: {ganhou}')
#         break

from random import randint

perdeu = False
contador = 0
while True:
    escolha_pc = randint(1, 10)
    escolha_hum = int(input('Digite um número de 1 a 10: '))
    par_ou_impar = str(input('Escolha [PAR] ou [IMPAR]: ')).upper()

    print('Computador Escolheu: ', escolha_pc)
    print('Você escolheu: ', escolha_hum)

    soma = escolha_pc + escolha_hum
    par = soma % 2

    print('A soma dos dois valores é de: ', soma)
    
    if par == 0:
        print('O número é par!')
    else:
        print('O número é impar!')

    if par_ou_impar == 'PAR' and par != 0:
        print('GAME OVER! Você perdeu...')
        break
    else:
        print('Você ganhou!')
    
    contador += 1
print(f'Você ganhou {contador} vezes antes de perder.')

