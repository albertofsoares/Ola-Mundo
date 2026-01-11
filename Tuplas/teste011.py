# Dada uma tupla de preços, aplique 10% de desconto e mostre o novo valor.

preços = (100.00, 200.00, 300.00, 400.00, 500.00)
porcentagem = 0.10

for preço in preços:
    desconto = preço * porcentagem
    novo_preço = preço - desconto
    print(f'De R${preço:.2f} com R${desconto:.2f} de desconto ficou por R${novo_preço:.2f}')