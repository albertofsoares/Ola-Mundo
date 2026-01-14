# Crie uma lista com 5 preços. 
# Aplique 10% de desconto em cada um 
# e salve os novos preços em uma lista nova

preços = [50.00, 100.00, 200.00, 150.00, 500.00]
preços10 = []

for preço in preços:
    desconto = preço * 0.10
    total = preço - desconto
    preços10.append(total)
    print(f'Valor R${preço:.2f} com 10% de desconto fica R${total:.2f}')
    

print(f'Os valores com descontos ficaram {preços10}')