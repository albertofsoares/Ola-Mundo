# Imprima cada letra de uma string que está dentro de uma tupla.

palavras = ('Python', 'Palito', 'Java', 'Jaqueta')

for palavra in palavras:
    print(f'A palavra é: "{palavra}"')

    for letra in palavra:
        print(letra)

