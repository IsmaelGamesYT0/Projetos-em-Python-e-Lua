# Crie um programa que leia um número Real qualquer e mostre sua porção inteira.

from time import sleep
from math import trunc, ceil
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()


numero_real = float(input("Digite um número real: "))

numero_arredondado = trunc(numero_real)

numero_arredondado_pra_cima = ceil(numero_real)

print("\nCalculando...")

sleep(2)

clear()

print(
    f"A porção inteira de {numero_real} é {numero_arredondado} e arredondando para cima fica {numero_arredondado_pra_cima}."
)
