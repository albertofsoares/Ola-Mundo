# Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 

# O seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# O programa deve realizar as seguintes etapas para cada chamada da função:

# Analisar os valores passados (empacotados).

# Contar quantos valores foram informados ao todo.

# Identificar qual é o maior valor entre eles.

# Exibir os dados formatados (mostrando todos os números, a contagem e o resultado).
m = 0

def maior(* n):
    tam = len(n)
    for p, v in enumerate(n):
        if p == 0:
            m = v
        elif v > m:
            m = v

        print(f'Na posição {p + 1} temos {v}')
    print(f'O maior número foi {m}')
    print(f'Ao todo {tam} números foram verificados.')


maior(3, 2, 5)