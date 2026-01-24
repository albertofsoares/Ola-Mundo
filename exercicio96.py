# Desafio 01: 
# Controle de Terrenos (Baseado no 096)

# Objetivo: Criar um programa que tenha uma função chamada area(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno.

# Requisito: O input deve ser feito no programa principal, 
# e a função deve receber esses valores como parâmetros.

comprimento = int(input('Digite o comprimento em metros: '))
largura = int(input('Digite a largura em metros: '))

def area(n1, n2):
    area = n1 * n2 
    return area

total = area(comprimento, largura)
print(f'A área do terreno é de {total}')