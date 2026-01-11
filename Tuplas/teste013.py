# Crie uma tupla com 5 animais e imprima-os em ordem alfabética (use sorted(tupla)).

animais = ('Elefante', 'Leão', 'Girafa', 'Leopardo', 'Zebra', 'Pinguim', 'Lhama')

cont = 0
for animal in animais:
    animais1 = sorted(animais)
    print(animais1[cont], end=', ')
    cont += 1
    
print('\n')
print(f'Animais em ordem: {sorted(animais)}')