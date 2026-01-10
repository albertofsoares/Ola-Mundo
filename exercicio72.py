#############################################
#   EXERCICIO 72 - TUPLAS - EXERCICIO 72    #
#############################################

# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contaem por extenso de zero até 20 (0, 1, 2, 3, 4, 5)

# Seu programa adeverá ler um número pelo telo entre 0 e 20
# e vai mostra-lo por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    num = int(input('Digite um número entre 0 e 20: '))

    while num < 0 or num > 20:
        num = int(input('Tente de novo! Digite um número entre 0 e 20: '))

    print(f'Você digitou o número: {numeros[num]}')
