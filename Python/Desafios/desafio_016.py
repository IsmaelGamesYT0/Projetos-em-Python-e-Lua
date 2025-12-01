# Crie um programa que leia um número Real qualquer e mostre sua porção inteira

from time import sleep
from math import trunc, ceil
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()

numero_real = float(input("Por favor, insira qualquer número real: "))

clear()

numero_inteiro = trunc(numero_real)

numero_inteiro_arredondado = ceil(numero_real)

print("Calculando...")
sleep(2.5)
clear()

print("Concluído!")
sleep(1.5)
clear()


print(
    f"Seu número real '{numero_real}' em número inteiro é '{numero_inteiro}' e arredodando é '{numero_inteiro_arredondado}'!"
)
