# Crie uma lista de 5 nomes e peça ao usuário para digitar um nome. 
# Diga quantas vezes esse nome aparece (count).

nomes = ['Alberto', 'Roger', 'Bruno', 'Marcelo', 'Breno']

nome = str(input('Digite um nome: '))
vezes = nomes.count(nome)
print(f'O nome "{nome}" apareceu {vezes} vez na lista!')
