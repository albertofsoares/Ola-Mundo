# Crie uma lista chamada filmes com 5 nomes de filmes e imprima a lista toda.

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

print(f'Confira o TOP 5 filmes de Janeiro!')
print(filmes)

###############################################################################

# Imprima apenas o primeiro e o último elemento da lista filmes.

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

print(filmes[0])
print(filmes[4])

###############################################################################

# Troque o nome do segundo filme da lista por "O Rei Leão".

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

print(filmes)
filmes[1] = 'O Rei Leão'
print(filmes)

###############################################################################

# Adicione um novo filme ao final da lista usando .append()

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

filmes.append('O Rei Leão')
print(filmes)

###############################################################################

# Adicione um filme na segunda posição da lista usando .insert().

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

filmes.insert(1, 'O Rei Leão')
print(filmes)

###############################################################################

# Remova o último filme da lista usando .pop().

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

filmes.pop()

print(filmes)

###############################################################################

# Remova um filme específico pelo nome usando .remove().

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']


filmes.remove('007')

print(filmes)

###############################################################################

# Crie uma lista com os números de 1 a 10 e imprima o tamanho dela usando len().

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(len(numeros))

###############################################################################

# Verifique se o filme "Matrix" está na sua lista usando if in.

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

if 'Matrix' in filmes:
    print('O filme "Matrix" está na lista')
else:
    print('O filme "Matrix" não está na lista')

###############################################################################

# Crie uma lista vazia e adicione 3 cores nela, uma por uma.

cores = []

for cor in range(0, 3):
    cores.append(str(input('Digite uma cor: ')))
print(cores)

###############################################################################

# Use um for para imprimir cada item da lista filmes em uma linha diferente.

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

for filme in filmes:
    print(filme)

###############################################################################

# Use um for com enumerate para mostrar: "Posição X: Filme Y".

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

for posição, filme in enumerate(filmes):
    print(f'O filme {filme} está na posição {posição + 1}')

###############################################################################

# Crie uma lista de números e imprima a soma de todos eles usando sum().

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'A soma da lista {numeros} é {sum(numeros)}')

###############################################################################

# Dada uma lista de números, imprima o maior (max) e o menor (min).

numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

maior = max(numeros)
menor = min(numeros)

print(f'O menor número é "{menor}" e o maior número é "{maior}".')

###############################################################################

# Crie uma lista de 5 nomes e peça ao usuário para digitar um nome. 
# Diga quantas vezes esse nome aparece (count).

nomes = ['Alberto', 'Roger', 'Bruno', 'Marcelo', 'Breno']

nome = str(input('Digite um nome: '))
vezes = nomes.count(nome)
print(f'O nome "{nome}" apareceu {vezes} vez na lista!')

###############################################################################

# Crie uma lista de números e imprima apenas os números pares usando um for e um if.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(numero, end='...')

###############################################################################

# Crie uma lista de números e crie uma nova lista 
# apenas com os números maiores que 10.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

maior10 = []

for numero in numeros:
    if numero > 10:
        maior10.append(numero)
        
print(maior10)

###############################################################################

# Dada uma lista de nomes, transforme todos os nomes 
# para letras maiúsculas dentro de um loop.

nomes = ['Alberto', 'Bruno', 'Fabio', 'Roger', 'Breno']

for nome in nomes:
    print(nome.upper(), end='...')

###############################################################################

# Crie uma lista e use o .reverse() para inverter a ordem dela.

numeros = [0, 2, 4, 6, 8, 10]

numeros.reverse()
print(numeros)

###############################################################################

# Crie uma lista de números desordenados 
# e use o .sort() para colocar em ordem crescente.

numeros = [0, 4, 2, 6, 10, 8]

numeros.sort()
print(numeros)

###############################################################################

# Peça ao usuário 5 números, um por um, e salve-os em uma lista.2

numeros = []

for numero in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
print(numeros)

###############################################################################

# Peça 5 números e, se o usuário digitar um número que já está na lista, não adicione

numeros = []

for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
print(numeros)

###############################################################################

# Leia uma lista de 5 notas e mostre a média

lista = [5.0, 8.7, 9.5, 4.8, 6.0]

total = sum(lista)
media = total / 5

print(f'A média de {lista} é: {media}')

###############################################################################

# Crie uma lista de compras. 
# Enquanto o usuário não digitar "fim", ,
# continue adicionando itens.

compras = []

while True:
    
    item = str(input('Digite o nome do item: ')).lower().strip()
    if item == 'fim':
        break
    
    while item != 'fim':
        item = str(input('Digite o nome do item: ')).lower().strip()
        if item not in compras:
            compras.append(item)

    if item == 'fim':
        break
print('Programa Finalizado!')
print('Sua lista de compras é:')
print(compras)

###############################################################################

# Dada uma lista A = [1, 2, 3] e B = [4, 5, 6], 
# crie uma lista C que seja a junção das duas.

listaA = [1, 2, 3]
listaB = [4, 5, 6]

listaC = listaA + listaB

print(listaC)

###############################################################################

# Crie uma lista com 10 números e peça ao usuário um número para remover.
# Se não existir, avise-o.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input('Digite um número: '))

if numero not in numeros:
    print('Este número não está na lista')
else:
    print(f'O número {numero} foi removido da Lista!')
    numeros.remove(numero)
    print(numeros)

###############################################################################

# Pergunte ao usuário o nome de 3 convidados e guarde numa lista. 
# Depois, mostre a lista em ordem alfabética.

convidados = []

for convidado in range(0, 3):
    convidados.append(str(input('Digite o nome do convidado: ')))

convidados.sort()
print(f'A lista de convidados em ordem é: {convidados}')

###############################################################################

# Crie uma lista com 5 preços. 
# Aplique 10% de desconto em cada um 
# e salve os novos preços em uma lista nova

preços = [50.00, 100.00, 200.00, 150.00, 500.00]
preços10 = []

for preço in preços:
    desconto = preço * 0.10
    total = preço - desconto
    preços10.append(total)
    print(f'Valor R${preço:.2f} com 10% de desconto fica R${total:.2f}')
    

print(f'Os valores com descontos ficaram {preços10}')

###############################################################################

# Crie uma lista de palavras e imprima apenas as palavras que têm mais de 5 letras.

palavras = ['Python', 'Java', 'JavaScript', 'Azure', 'Lua']

for palavra in palavras:
    if len(palavra) > 5:
        print(palavra)

###############################################################################

# Crie uma lista vazia. Peça ao usuário para digitar números até ele digitar 0. 
# Depois, mostre a lista na ordem inversa.

numeros = []

while True:

    numero = int(input('Digite um número: '))

    if numero == 0:
        break
    
    while numero not in numeros:
        numeros.append(numero)
    

print(numeros)