#########################################################
#                                                       #
#                   EXERCICIO 83                        #
#                                                       #
#########################################################

# Faça um programa onde o usuário digite uma expressão qualquer que use parenteses
# seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos
# e fechados na ordem correta

lista = []

expressao = str(input('Digite uma expressão: '))

for c in expressao:
    if '(' in c:
        lista.append(c)

    if c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')') # Adicionamos um erro na lista
            break # Interrompemos pois já deu erro

if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')