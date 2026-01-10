# Dada uma tupla de nomes, imprima apenas os nomes que começam com a letra "A".

nomes = ('Alberto', 'Carlos', 'Amanda', 'Antonio', 'José', 'Maria', 'Vanessa')

for nome in nomes:
    if nome[0] == 'A':
        print(nome)