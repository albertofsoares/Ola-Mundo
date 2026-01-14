#########################################################
#                                                       #
#                   EXERCICIO 79                        #
#                                                       #
#########################################################

# Faça um programa onde o usuário possa digitar vários valores númericos
# e cadestre-os em uma lista. Caso o número já existe lá dentro,
# ele não será adicionado.

# No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.


lista = []

while True:
    numero = int(input('Digite um número: '))

    if numero not in lista:
        lista.append(numero)

    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()
    
    if escolha == 'N':
        break
lista.sort()
print(lista)