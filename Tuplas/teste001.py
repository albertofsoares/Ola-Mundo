# Básico (Tupla + For): 

# Crie uma tupla com 5 nomes de cidades. 
# Use um for simples (sem range) para mostrar a mensagem: 
# "Eu quero visitar [Nome da Cidade]".

# cidades = ('Pelotas', 'Rio Grande', 'Morro Redondo', 'Monte Bonito', 'Porto Alegre')

# for cidade in cidades:
#     print(f'Eu quero viajar para {cidade}')






























# Range (Contagem): 
# 
# Use um for com range para exibir os números de 10 até 1, 
# em ordem decrescente (Dica: use o passo -1 no range).

for c in range(10, 0, -1):
    print(c)







# Híbrido (Posição): 
# Crie uma tupla com 3 cores. 
# Use o for com range(0, len(tupla)) para mostrar: 
# "A cor na posição [índice] é [cor]".

cores = ('Amarelo', 'Vermelho', 'Laranja')

for c in range(0, len(cores), 1):
    print(f'A cor nº {c + 1} é {cores[c]}')