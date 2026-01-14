#########################################################
#                                                       #
#                   EXERCICIO 81                        #
#                                                       #
#########################################################

# Faça um programa que vai ler vários números e colocar em uma lista.

# Depois disso mostre:

# Quantos números foram digitados

# A lista de valores, ordenada de forma decrescente

# Se o valor 5 foi digitado e está ou não na lista

lista = []

while True:

    lista.append(int(input('Digite um número: ')))

    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()
    
    if escolha == 'N':
        break

print(f'{len(lista)} números foram digitados!')
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')