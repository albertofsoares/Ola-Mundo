# Desafio 03: 
# A Função Contador (Baseado no 098)

# Objetivo: Criar uma função chamada contador(), 
# que receba três parâmetros: Início, Fim e Passo. 

# O programa deve realizar três contagens diferentes 
# utilizando essa mesma função.

# As Três Etapas:

# Contagem Crescente Simples: De 1 até 10, de 1 em 1.

# Contagem Regressiva Simples: De 10 até 0, de 2 em 2.

# Contagem Personalizada: 
# O programa principal deve ler os valores de Início,
#  Fim e Passo do teclado e passá-los para a função.



def contador(inicio, fim, passo):
    passo = abs(passo)

    if passo == 0:
        passo = 1
    
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c} → ', end='')
        print('FIM')

    elif inicio > fim:
        for c in range(inicio, fim - 1, -passo):
            print(f'{c} → ', end='')
        print('FIM')

i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)