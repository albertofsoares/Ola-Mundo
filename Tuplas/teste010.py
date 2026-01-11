# Crie uma tupla de notas (0 a 10) e diga se cada nota é "Aprovado" (>=7).

notas = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for nota in notas:
    if nota < 7:
        print(f'A nota "{nota}" é menor que 7 então está reprovada!')
    elif nota == 7:
        print(f'A nota "{nota}" é igual a 7 então está aprovada!')
    else:
        print(f'A nota "{nota}" é maior que 7 etão está aprovada!')