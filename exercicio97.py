# Objetivo: 

# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem 
# com tamanho adaptável.

# Exemplo: escreva('Olá, Mundo!')

def escreva(texto):
    tamanho = len(texto) + 4
    print('-' * tamanho)
    print(f'  {texto}')
    print('-' * tamanho)

escreva('Python 3 com Prof. Guanabara')
escreva('Aprendendo Funções')
escreva('Até o dia 29!')