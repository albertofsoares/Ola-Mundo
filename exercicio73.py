#############################################
#   EXERCICIO 73 - TUPLAS - EXERCICIO 73    #
#############################################

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do campeonato brasileiro de futebol, na ordem de colocação.
# depois mostre:

# apenas os 5 primeiros colocados

# os últimos 4 colocados na tabela

# uma lista com os times em ordem alfabética

# em que posição na tabela está o time da Chapecoense

tabela = ('Athletico Paranaense', 'Atlético-MG', 'Bahia', 
          'Botafogo', 'Chapecoense', 'Corinthians', 'Coritiba', 
          'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 
          'Internacional', 'Mirassol', 'Palmeiras', 'RedBull Bragantino', 
          'Remo', 'Santos', 'São Paulo', 'Vasco da Gama', 'Vitória')

print(f'Os 5 primeiros colocados são: ', tabela[0:5])

print(f'Os últimos 4 colocados são: ', tabela[-4:])

print(f'A lista em ordem alfabética é: ', sorted(tabela))   # já estava em ordem mas seria assim!

# A forma mais simples:
posicao = tabela.index('Chapecoense') + 1
print(f'A Chapecoense está na {posicao}ª posição.')

# A forma que eu fiz:
# contador = 0
# limite = len(tabela)

# while contador < 20:
#     contador += 1

#     if tabela[contador] == 'Chapecoense':
#         chapeco = contador
#         print(f'O time Chapecoense está em: {chapeco}')
#         break