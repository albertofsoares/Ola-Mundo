#########################################################
#                                                       #
#                   EXERCICIO 92                        #
#                                                       #
#########################################################

# Crie um programa que leia nome, ano de nascimento 
# e carteira de trabalho e cadastre-o (com idade) em um dicionário. 

# Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. 

# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Nota: Considere 35 anos de contribuição para se aposentar.

dicionario = {}
contribuicao = 35

dicionario['nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Qual seu ano de nascimento? '))
dicionario['idade'] = (2025 - nascimento)
dicionario['CTPS'] = int(input('Digite o número da sua CTPS: '))

if dicionario['CTPS'] != 0:
    dicionario['ano de contratação'] = int(input('Digite o ano de contratação: '))
    dicionario['salário'] = int(input('Digite o seu salário: R$'))
    aposentadoria = dicionario['ano de contratação'] + 35
    idadeap = aposentadoria - nascimento
    dicionario['aposentadoria'] = idadeap
    print(f"Hoje você tem {dicionario['idade']} anos e se aposentará com {idadeap} anos.")