#########################################################
#                                                       #
#                   EXERCICIO 82                        #
#                                                       #
#########################################################

# Faça um programa que vai ler vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores impares digitados, respectivamente

# ao final mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:

    lista.append(int(input('Digite um número: ')))

    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()
        
    if escolha == 'N':
        break

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('Primeira lista: ')
print(lista)
print('Lista dos Pares: ')
print(pares)
print('Lista dos Impares: ')
print(impares)