# Faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

import time

print("Seja Bem-vindo ao Tinta Calculator, informe abaixo, as medidas abaixo em metros!")

print("-" * 80)

largura = int(input("Por favor, informe a largura da parede:"))
altura = int(input("Agora, favor informar a altura da parede:"))

area = largura *  altura

tinta_litro = area / 2

print("Calculando!...")
time.sleep(2)

print("Será necessário {} litros de tinta para pintar totalmente a parede".format(tinta_litro))

print("=" * 40)

print("Obrigado por usar meu programa, volte sempre!")
