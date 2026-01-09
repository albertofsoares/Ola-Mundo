#####################################
#
# EXERCICIO 69
#
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada o programa deverá perguntar se o usuário
# quer ou não continuar.
# No final mostre:
#
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos
mulher_menor = 0
maior = 0
homens = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('[M]asculino ou [F]eminino? ')).upper()

    while sexo not in 'MF':
        sexo = str(input('[M]asculino ou [F]eminino? ')).upper()
        
    if idade < 20 and sexo == 'F':
        mulher_menor += 1
    if idade > 18:
        maior += 1

    if sexo == 'M':
        homens += 1

    escolha = str(input('Deseja continuar [S/N]? ')).upper()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).upper()

    if escolha == 'N':
        break
print(f'Existem {maior} pessoas maior de idade.')
print(f'Existem {mulher_menor} mulheres com menos de 20 anos.')
print(f'Existem {homens} homens cadastrados.')