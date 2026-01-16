# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

carteira = float(input("Insira seu saldo em R$ que você tem na carteira:"))

dolar = carteira / 5.33

print("Parabéns, com R${:.2f} reais, você consegue comprar ${:.2f} dólares!".format(carteira, dolar))
