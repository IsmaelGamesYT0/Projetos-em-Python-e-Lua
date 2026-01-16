valor_em_reais = float(input("Por favor insira o valor em Reais(BRL): "))

dolar_atual = 5.34

valor_em_dolares = valor_em_reais / dolar_atual

print(f"Cotação atual: US$ {dolar_atual} \n")
print(f"Você pode comprar US$ {valor_em_dolares:.2f} dolares.")
