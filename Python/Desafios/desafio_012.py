# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor_original = float(input("Por favor, informe o valor do produto:"))

desconto = valor_original * 0.05

valor_novo = valor_original - desconto

print("Parabéns, você ganhou um desconto de 5%, então ao invés de pagar R${} reais, você irá pagar apenas R${:.2f} reais.".format(valor_original, valor_novo))