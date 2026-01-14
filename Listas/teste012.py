# Use um for com enumerate para mostrar: "Posição X: Filme Y".

filmes = ['Harry Potter', '007', 'O Homem da Máfia', 'V de Vingança', 'Rio']

for posição, filme in enumerate(filmes):
    print(f'O filme {filme} está na posição {posição + 1}')