#############################################
#   EXERCICIO 77 - TUPLAS - EXERCICIO 77    #
#############################################

# Crie um programa que tenha uma tupla com várias palavra
# (não usar acentos)
# Depois disso você deve mostrar para cada palavra quais são suas vogais

tupla = ('Alfabeto', 'Numeral', 'Analisando', 'Segunda', 'Quarta', 'Domingo',
         'Sexta', 'Quinta', 'Sabado', 'Feriado', 'Expediente', 'Folga')

for palavra in tupla: # Laço Externo: Pega uma palavra por vez
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    
    for letra in palavra: # Laço Interno: Pega cada letra da palavra atual
        if letra.lower() in 'aeiou': # Filtro completo com a letra 'u'
            print(letra.lower(), end=' ') # Imprime a vogal e continua na linha

            