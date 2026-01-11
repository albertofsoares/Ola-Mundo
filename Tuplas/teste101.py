# Exercício Python 73: 
# 
# Crie uma tupla preenchida com os 20 primeiros colocados 
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# 
# Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

tabela = ('Athletico Paranaense', 'Atlético-MG', 'Bahia', 
          'Botafogo', 'Chapecoense', 'Corinthians', 'Coritiba', 
          'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 
          'Internacional', 'Mirassol', 'Palmeiras', 'RedBull Bragantino', 
          'Remo', 'Santos', 'São Paulo', 'Vasco da Gama', 'Vitória')

print(f'Os primeiros cinco times são {tabela[:5]}')

print(f'Os últimos colocados são {tabela[-4:]}')

print(f'Os times em ordem alfabetica ficariam: {sorted(tabela)}')

print(f'A chapecoense está em {tabela.index('Chapecoense')}º lugar!')