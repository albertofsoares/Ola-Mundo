# Verifique se a cor "Azul" está em uma tupla de cores e imprima "Achei".

cores = ('Vermelho', 'Verde', 'Roxo', 'Amarelo', 'Azul')

contador = 0
for cor in cores:
    contador += 1
    if cor.find('Azul') == 0:
        print('Achei')
        print('Estava na posição: ', contador)