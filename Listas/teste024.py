# Crie uma lista de compras. 
# Enquanto o usuário não digitar "fim", ,
# continue adicionando itens.

compras = []

while True:
    
    item = str(input('Digite o nome do item: ')).lower().strip()
    if item == 'fim':
        break
    
    while item != 'fim':
        item = str(input('Digite o nome do item: ')).lower().strip()
        if item not in compras:
            compras.append(item)

    if item == 'fim':
        break
print('Programa Finalizado!')
print('Sua lista de compras é:')
print(compras)