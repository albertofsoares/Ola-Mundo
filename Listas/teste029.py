# Crie uma lista de palavras e imprima apenas as palavras que têm mais de 5 letras.

palavras = ['Python', 'Java', 'JavaScript', 'Azure', 'Lua']

for palavra in palavras:
    if len(palavra) > 5:
        print(palavra)