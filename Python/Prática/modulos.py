from time import sleep
from math import sqrt, ceil
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


numero = int(input("Por favor, insira um número: "))
raiz = sqrt(numero)
raiz_arredondada = ceil(raiz)
clear()

print("Calculando...")
sleep(2.5)
clear()

print("Calculo Concluído!")
sleep(2)
clear()

print(f"A raiz quadrada de {numero} é {raiz:.2f} e arredondando é {raiz_arredondada}!")
